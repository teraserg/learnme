from django.db import models


class Word(models.Model):
    text = models.CharField(max_length=200)
