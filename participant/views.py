from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from participant.models import Team
from .forms import ProjectForm 

def index(request):
    return render(request, 'participant/index.html')

def project_details(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        return HttpResponse(form.errors)
    else:
        form = ProjectForm()
        return render(request, 'participant/project_details.html', {'form': form})

def demo_video(request):
    if request.method == 'POST':
        url = request.POST.get('video_url')
        print(request.user.id)
        project = Team.objects.get(team_id = request.user.username)
        project.project_video_url = url
        project.save()

        return redirect('home')
    else:
        return redirect(request, 'participant/index.html')

def source_code(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'participant/index.html')