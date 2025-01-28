from django.contrib import admin
from django.urls import path, include
from accounts.views import home, edit_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('edit_profile/', edit_profile, name='edit_profile'),  # Add this for a direct route
    path('', home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:  # Only serve media in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)