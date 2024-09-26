from django.urls import path
from .views import (
    JobSeekerProfileCreateView, JobSeekerProfileUpdateView, 
    JobSeekerProfileDeleteView, JobSeekerProfileListView, 
    JobSeekerProfileDetailView
)

app_name = 'profiles'  # Namespace for profiles app

urlpatterns = [
    # Create a new job seeker profile
    path('create/', JobSeekerProfileCreateView.as_view(), name='jobseekerprofile-create'),

    # Update an existing job seeker profile by its primary key (pk)
    path('update/<int:pk>/', JobSeekerProfileUpdateView.as_view(), name='jobseekerprofile-update'),

    # Delete a job seeker profile by its pk
    path('delete/<int:pk>/', JobSeekerProfileDeleteView.as_view(), name='jobseekerprofile-delete'),

    # List all job seeker profiles
    

    # Detail view of a specific job seeker profile by pk
    
]
