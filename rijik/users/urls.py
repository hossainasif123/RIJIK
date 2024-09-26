from django.urls import path
from .views import SeekerSignUpView, EmailVerificationView, LoginView, EmailVerificationSentView, HomeView, LogoutView, PasswordResetRequestView, PasswordResetConfirmView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from profiles.views import JobSeekerProfileDetailView,JobSeekerProfileListView


app_name = 'users'  # This registers the namespace

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),  # Home or dashboard view after login
    path('signup/', SeekerSignUpView.as_view(), name='signup'),  # Sign-up page for new users
    path('email-verification-sent/', EmailVerificationSentView.as_view(), name='email_verification_sent'),  # Confirmation after email verification sent
    path('verify/<uidb64>/<token>/', EmailVerificationView.as_view(), name='email-verify'),  # Email verification
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view
    path('login/', LoginView.as_view(), name='login'),  # Login view
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),  # Password reset request
    path('password-reset/done/', TemplateView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),  # Password reset done confirmation
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Password reset confirmation link
   path('profiles/<int:pk>/', login_required(JobSeekerProfileDetailView.as_view()), name='show-profile'),  # Detail view of a specific pet profile
    path('list/', JobSeekerProfileListView.as_view(), name='jobseekerprofile-list'),
   


]
