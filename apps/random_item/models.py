from django.db import models


class Dictionary(models.Model):
    item = models.CharField(max_length=256)
    translation = models.CharField(max_length=1024)
