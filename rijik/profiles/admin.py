from django.contrib import admin
from .models import JobSeekerProfile, Skill, MediaUpload

# JobSeekerProfile Admin Configuration
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'availability', 'desired_salary')
    search_fields = ('user__username', 'location', 'availability')
    list_filter = ('availability', 'desired_salary')
    filter_horizontal = ('skills',)  # Makes the ManyToMany skills field easier to select in the admin

# Skill Admin Configuration
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# MediaUpload Admin Configuration
class MediaUploadAdmin(admin.ModelAdmin):
    list_display = ('user', 'upload_type', 'upload_date')
    search_fields = ('user__username', 'upload_type')
    list_filter = ('upload_type', 'upload_date')
    readonly_fields = ('upload_date',)  # Make the upload_date read-only

# Registering the models with the admin site
admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(MediaUpload, MediaUploadAdmin)
