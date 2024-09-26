from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import JobSeekerProfile, Skill
from .forms import JobSeekerProfileForm, SkillFormSet

class JobSeekerProfileCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = JobSeekerProfile
    form_class = JobSeekerProfileForm
    template_name = 'profiles/job_seeker_profile_form.html'

    def dispatch(self, request, *args, **kwargs):
        if JobSeekerProfile.objects.filter(user=request.user).exists():
            return redirect('users:show-profile', pk=JobSeekerProfile.objects.get(user=request.user).pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        formset = SkillFormSet(self.request.POST)
        if formset.is_valid():
            profile = self.object
            profile.skills.clear()
            for skill_form in formset:
                skill_name = skill_form.cleaned_data.get('name')
                if skill_name:
                    skill, created = Skill.objects.get_or_create(name=skill_name)
                    profile.skills.add(skill)
        return response

    def get_success_url(self):
        return reverse_lazy('users:show-profile', kwargs={'pk': self.object.pk})

class JobSeekerProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users:login'
    model = JobSeekerProfile
    form_class = JobSeekerProfileForm
    template_name = 'profiles/job_seeker_profile_form.html'

    def get_queryset(self):
        return JobSeekerProfile.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.POST:
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES
            })
        else:
            kwargs.update({
                'instance': self.get_object()
            })
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = SkillFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            profile = self.object
            profile.skills.clear()
            for skill_form in formset:
                skill_name = skill_form.cleaned_data.get('name')
                if skill_name:
                    skill, created = Skill.objects.get_or_create(name=skill_name)
                    profile.skills.add(skill)
        return response

    def get_success_url(self):
        return reverse_lazy('users:show-profile', kwargs={'pk': self.object.pk})

class JobSeekerProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    model = JobSeekerProfile
    template_name = 'profiles/job_seeker_profile_detail.html'
    context_object_name = 'job_seeker_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = self.object.skills.all()
        return context

    def get_queryset(self):
        return JobSeekerProfile.objects.all()

class JobSeekerProfileListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    model = JobSeekerProfile
    template_name = 'profiles/job_seeker_profile_list.html'
    context_object_name = 'job_seeker_profiles'

    def get_queryset(self):
        return JobSeekerProfile.objects.all()

class JobSeekerProfileDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users:login'
    model = JobSeekerProfile
    template_name = 'profiles/job_seeker_profile_confirm_delete.html'
    success_url = reverse_lazy('users:jobseekerprofile-list')

    def get_queryset(self):
        return JobSeekerProfile.objects.filter(user=self.request.user)
