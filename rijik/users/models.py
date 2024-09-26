from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    JOB_SEEKER = 'job_seeker'
    EMPLOYER = 'employer'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (JOB_SEEKER, 'Job Seeker'),
        (EMPLOYER, 'Employer'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=JOB_SEEKER)
    email = models.EmailField(unique=True)  # Ensure the email is unique

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    def save(self, *args, **kwargs):
        # Ensure that superusers always have the ADMIN role
        if self.is_superuser:
            self.role = self.ADMIN
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        # Allow only users with the ADMIN role and superusers to have permissions
        if self.role == self.ADMIN or self.is_superuser:
            return super().has_perm(perm, obj)
        return False

    def has_module_perms(self, app_label):
        # Allow only users with the ADMIN role and superusers to access the admin panel
        if self.role == self.ADMIN or self.is_superuser:
            return super().has_module_perms(app_label)
        return False
