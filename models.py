import datetime

from django.db import models
from django.utils import timezone


class Team(models.Model):
    team_name = models.CharField(max_length=20, default='team')

    def __str__(self):
        return self.team_name


class Ticket(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='unknown')
    lvl = models.IntegerField(default=1)
    category = models.CharField(max_length=20, default='unknown')
    tag = models.CharField(max_length=20, default='unknown')
    agent = models.CharField(max_length=20, default='unknown')
    last_update = models.DateTimeField('last update', default=timezone.now)  # change to date creation
    last_action = models.CharField(max_length=20, default='unknown')
    user = models.CharField(max_length=20, default='unknown')
    close_at = models.DateTimeField('close at', default=timezone.now)
    text = models.TextField(max_length=200)

    def __str__(self):
        return str(self.text)

    def was_published_recently(self):
        return self.last_update >= timezone.now() - datetime.timedelta(days=1)
