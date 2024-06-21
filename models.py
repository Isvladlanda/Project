from django.db import models


class Users(models.Model):
    name = models.CharField(),
    email = models.CharField(),
    password = models.CharField(max_length=20)