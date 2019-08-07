from django.db import models
from datetime import datetime

class Blog(models.Model):
    posts = models.CharField(max_length=200)
    file_name = models.FileField(blank=True)
    pubdate = models.DateTimeField(default=datetime.now, blank=True)