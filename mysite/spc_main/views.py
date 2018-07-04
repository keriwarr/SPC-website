from django.shortcuts import render

from .models import User, Team, Project, Interest

def index(request):
    context = {}
    return render(request, 'spc_main/index.html', context)

def about(request):
    context = {}
    return render(request, 'spc_main/about.html', context)

def faq(request):
    context = {}
    return render(request, 'spc_main/faq.html', context)

def past_projects(request):
    context = {}
    return render(request, 'spc_main/past_projects.html', context)

def get_involved(request):
    context = {}
    return render(request, 'spc_main/get_involved.html', context)

def partners(request):
    context = {}
    return render(request, 'spc_main/partners.html', context)

def teams(request):
    return HttpResponse("Teams")

def users(request):
    return HttpResponse("Users")
