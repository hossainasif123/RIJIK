from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')), 
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('employer/', include('employer.urls', namespace='employer')), # Include URLs from the 'users' app
   
]

# Add static file URL configuration
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add media file URL configuration (important for development)
if settings.DEBUG:  # Ensure this is only active in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)