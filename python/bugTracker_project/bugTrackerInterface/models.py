from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Bug(models.Model):
    application = models.CharField(max_length=150)
    description = models.TextField()
    snippet = models.CharField(max_length=100, default='No Snippet Available')
    datePosted = models.DateTimeField(default=timezone.now)
    finished = models.BooleanField(default=False)
    addedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.application

    def get_absolute_url(self):
        return reverse('bug-detail', kwargs={'pk': self.pk})

