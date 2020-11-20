from django.contrib import admin
from solo.admin import SingletonModelAdmin

from django import forms
from .models import *

class AboutMeForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

class AboutMeAdmin(SingletonModelAdmin):
    form = AboutMeForm

admin.site.register(AboutMe, AboutMeAdmin)

class SocialIconAdmin(admin.ModelAdmin):
     list_display = ('name', 'img_loc', 'link')

admin.site.register(SocialIcon, SocialIconAdmin)

class ProjectForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    form = ProjectForm

admin.site.register(Project, ProjectAdmin)

class ContactResponseForm(forms.ModelForm):
    main_text = forms.CharField(widget=forms.Textarea)

class ContactResponseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'main_text', 'date')
    form = ContactResponseForm

admin.site.register(ContactResponse, ContactResponseAdmin)
