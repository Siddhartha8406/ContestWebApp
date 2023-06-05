from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reg_desk import views as reg_desk_views
from login_system import views as login_system_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg_desk.urls')),
    path('', include('login_system.urls')),
    path('', include('participant.urls')),
    path('', include('public.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
