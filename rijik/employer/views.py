from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EmployerProfile
from .forms import EmployerProfileForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import EmployerProfile
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JobPosting,Notification
from .forms import JobPostingForm
from django.utils import timezone
from django.views.generic import DetailView, TemplateView
class EmployerProfileCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'employer/employer_profile_form.html'

    def dispatch(self, request, *args, **kwargs):
        if EmployerProfile.objects.filter(user=request.user).exists():
            return redirect('employer:show-employer-profile', pk=EmployerProfile.objects.get(user=request.user).pk)
        
        # Check if the user is an employer
        if request.user.role != 'employer':
            return redirect('users:unauthorized')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employer:show-employer-profile', kwargs={'pk': self.object.pk})




class EmployerProfileDetailView(DetailView):
    model = EmployerProfile
    template_name = 'employer/employer_profile_detail.html'
    context_object_name = 'employer_profile'

    def get_object(self):
        # Get the employer profile by its primary key (pk) passed in the URL
        return get_object_or_404(EmployerProfile, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # You can add more context if needed, e.g., a list of the employer's job listings
     
        return context





class JobPostingListView(ListView):
    model = JobPosting
    template_name = 'employer/job_posting_list.html'  # Template for listing job postings
    context_object_name = 'job_postings'
    ordering = ['-date_posted']  # Order by latest postings using 'date_posted'

"""class JobPostingCreateView(LoginRequiredMixin, CreateView):
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'employer/job_posting_form.html'  # Create this template
    success_url = reverse_lazy('employer:job-posting-list')  # Redirect to job listing after success

    def form_valid(self, form):
        # Ensure the employer field is set to the User instance, not EmployerProfile
        form.instance.employer = self.request.user  # Assign the User instance
        return super().form_valid(form)"""




class NotificationsView(TemplateView):
    template_name = 'employer/notifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch unread notifications for the user
        unread_notifications = Notification.objects.filter(user=self.request.user, is_read=False)
        
        # Mark them as read
        unread_notifications.update(is_read=True)
        
        # Fetch all notifications for the user, including read and unread
        context['notifications'] = Notification.objects.filter(user=self.request.user).order_by('-created_at')
        context['unread_count'] = Notification.objects.filter(user=self.request.user, is_read=False).count()
        return context
    



from django.http import JsonResponse
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from .models import JobPosting, Notification

from django.contrib.auth import get_user_model

User = get_user_model()  # This retrieves your custom user model

class NotificationCreationView(View):
    def post(self, request, job_title, *args, **kwargs):
        user = request.user  # The employer who posted the job
        
        # Customize your message content
        message = f"A new job posting '{job_title}' has been created by {user.username}."
        
        # Get the channel layer
        channel_layer = get_channel_layer()

        # Notify all job seekers
        job_seekers = User.objects.filter(role='job_seeker')  # Fetch all job seekers
        for seeker in job_seekers:
            async_to_sync(channel_layer.group_send)(
                f'notifications_{seeker.username}',  # Room group name based on the job seeker's username
                {
                    'type': 'job_notification',  # Custom notification type
                    'message': message
                }
            )

            # Optionally, save the notification in the database
            Notification.objects.create(
                user=seeker,
                message=message
            )

        return JsonResponse({'status': 'Notifications sent to all job seekers'}, status=200)

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class JobPostingCreateView(LoginRequiredMixin, CreateView):
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'employer/job_posting_form.html'
    success_url = reverse_lazy('employer:job-posting-list')

    def form_valid(self, form):
        form.instance.employer = self.request.user  # Assign the User instance
        response = super().form_valid(form)  # Call the parent class's form_valid method

        # Notify all job seekers
        notification_view = NotificationCreationView.as_view()
        notification_view(self.request, job_title=form.instance.title)  # Call the notification view with job title

        return response
