from django.shortcuts import render, redirect
from .forms import TeamForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout as user_logout

from participant.models import Team

def index(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='participant').exists():
            return render(request, 'participant/index.html')
        return render(request, 'desk/index.html')
    else:
        return redirect('login')
    


def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TeamForm(request.POST)
            team_name = form['team_name'].value()
            team_college = form['team_college'].value()
            team_department = form['team_department'].value()

            team = Team(team_name=team_name, team_college=team_college, team_department=team_department)
            team.save()

            pswd = str(team.team_id)+str(team.team_college[:3])

            print(team.team_id, pswd)

            user = User.objects.create_user(username=team.team_id, password=pswd)

            user_group = Group.objects.get(name='participant')
            user_group.user_set.add(user)
            
            user.save()

            return redirect('home')
        else:
            form = TeamForm()
            return render(request, 'desk/register.html', {'form': form})
    else:
        return redirect('login')
    
def check(request): 
    logout(request)
    return render(request, 'desk/check.html')

def logout(request):
    user_logout(request)
    return redirect('login')
