from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Position(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title

class Worker(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    position = models.ForeignKey(Position)
    bio = models.TextField()

    def __str__(self):
        return self.last_name + ", " + self.first_name
