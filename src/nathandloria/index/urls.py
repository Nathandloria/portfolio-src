from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('resume', views.pdf_view, name='resume'),
    path('projects', views.projects, name='projects'),
]
