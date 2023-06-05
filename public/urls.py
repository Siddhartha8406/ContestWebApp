from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='participant_home'),
    path('project_details/<int:id>', views.project_details, name='project_details'),
]