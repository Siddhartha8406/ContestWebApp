from django.urls import path
from . import views

urlpatterns = [
    path('project_details', views.project_details, name='project_details'),
    path('demo_video', views.demo_video, name='demo_video'),
    path('source_code', views.source_code, name='source_code'),
]
