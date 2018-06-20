from django.shortcuts import render

from .models import User, Team, Project, Interest

def index(request):
    context = {}
    return render(request, 'spc_main/index.html', context)

def teams(request):
    return HttpResponse("Teams")

def users(request):
    return HttpResponse("Users")
