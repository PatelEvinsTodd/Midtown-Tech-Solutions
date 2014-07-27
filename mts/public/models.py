from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
