from django.contrib import admin

from .models import User, Team, Project, Interest

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Interest)
