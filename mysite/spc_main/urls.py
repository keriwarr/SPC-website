from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('past_projects/', views.past_projects, name='past_projects'),
    path('get_involved/', views.get_involved, name='get_involved'),
    path('partners/', views.partners, name='partners'),
    path('teams/', views.teams, name='teams'),
    path('users/', views.users, name='users'),
]
