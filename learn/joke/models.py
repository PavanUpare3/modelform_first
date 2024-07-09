from django.db import models

class Stureg(models.Model):
    name = models.CharField(max_length=23)
    surname = models.CharField(max_length=34)
    email = models.EmailField()
    password = models.CharField(max_length=23)
