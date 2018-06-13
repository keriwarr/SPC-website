from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("A surprise to be sure, but a welcome one.")
