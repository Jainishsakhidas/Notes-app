from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes(models.Model):
    note_title = models.CharField(max_length=40)
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title
