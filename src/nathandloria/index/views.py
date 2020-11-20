from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render
from django.template import loader

from django.contrib.staticfiles.storage import staticfiles_storage

from django.conf import settings
from .models import *
from .forms import *

from datetime import datetime

def index(request):
    template = loader.get_template('index/index.html')
    bio = AboutMe.get_solo().bio
    icons = SocialIcon.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cr = ContactResponse()
            cr.main_text = request.POST.get('main_text')
            cr.first_name = request.POST.get('first_name')
            cr.last_name = request.POST.get('last_name')
            cr.email = request.POST.get('email')
            cr.date = datetime.now()
            cr.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    context = {
        'bio': bio,
        'icons': icons,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def pdf_view(request):
    template = loader.get_template('index/resume.html')
    icons = SocialIcon.objects.all()
    context = {
        'icons': icons,
    }
    return HttpResponse(template.render(context, request))

def projects(request):
    template = loader.get_template('index/projects.html')
    projects = Project.objects.all()
    icons = SocialIcon.objects.all()
    context = {
        'projects': projects,
        'icons': icons,
    }
    return HttpResponse(template.render(context, request))
