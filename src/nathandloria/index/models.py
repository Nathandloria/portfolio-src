from django.db import models
from solo.models import SingletonModel

class AboutMe(SingletonModel):
    bio = models.CharField(default="", max_length=10000)

class SocialIcon(models.Model):
    name = models.CharField(default="", max_length=255)
    img_loc = models.CharField(default="", max_length=255)
    link = models.CharField(default="", max_length=255)

class Project(models.Model):
    title = models.CharField(default="", max_length=255)
    desc = models.CharField(default="", max_length=10000)

class ContactResponse(models.Model):
    main_text = models.CharField(default="", max_length=10000)
    first_name = models.CharField(default="", max_length=255)
    last_name = models.CharField(default="", max_length=255)
    email = models.CharField(default="", max_length=255)
    date = models.DateTimeField(default=None)
