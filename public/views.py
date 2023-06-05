from django.shortcuts import render
from participant.models import Team

def index(request):
    projects = Team.objects.all()
    print(projects)
    return render(request, 'public/index.html', {'projects': projects})

def project_details(request, id):
    project = Team.objects.get(team_id=id)
    print(project)
    return render(request, 'public/project_details.html', {'project': project})
