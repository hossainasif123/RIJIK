from django.urls import path
from .views import EmployerProfileCreateView, EmployerProfileDetailView, JobPostingListView, JobPostingCreateView,NotificationCreationView,NotificationsView
    


app_name = 'employer'

urlpatterns = [
    # Employer Profile URLs
    path('employer/create/', EmployerProfileCreateView.as_view(), name='employerprofile-create'),
    path('employer/<int:pk>/', EmployerProfileDetailView.as_view(), name='employerprofile-detail'),
    path('list/', JobPostingListView.as_view(), name='job-posting-list'),
    path('create/', JobPostingCreateView.as_view(), name='job-posting-create'),
    path('notifications/create/', NotificationCreationView.as_view(), name='notification-create'), 
    path('notifications/', NotificationsView.as_view(), name='notifications'), # Optional
]
