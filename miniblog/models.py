from django.db import models

class Blog(models.Model):
    posts = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200, blank=True)