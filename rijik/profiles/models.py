from django.db import models
from django.conf import settings
import os

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'job_seeker'}
    )
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)  # Link to online portfolio
    skills = models.ManyToManyField('Skill', blank=True)
    experience = models.TextField(blank=True, null=True)  # Job experience
    education = models.TextField(blank=True, null=True)   # Educational background
    location = models.CharField(max_length=255, blank=True, null=True)  # Job seeker's location
    availability = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'Full-time', 'Part-time'
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

# Skill model for linking skills to JobSeekerProfile
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class MediaUpload(models.Model):
    UPLOAD_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('prescription', 'Prescription'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_type = models.CharField(max_length=15, choices=UPLOAD_TYPE_CHOICES)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    video = models.FileField(upload_to='uploads/videos/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Delete image and video from filesystem when model is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        if self.video:
            if os.path.isfile(self.video.path):
                os.remove(self.video.path)
        super().delete(*args, **kwargs)  # Call the parent class's delete method

    def __str__(self):
        return f'{self.upload_type} upload by {self.user}'
