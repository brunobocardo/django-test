from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

SENTIMENTAL_LEVEL = [
    (1, 'Unhappy'),
    (2, 'Not Happy'),
    (3, 'Neutral'),
    (4, 'Happy'),
    (5, 'Very Happy'),
    ]


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.group_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class HappinessLevel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    level = models.IntegerField(choices = SENTIMENTAL_LEVEL)
    date = models.DateField(default=datetime.today().date())
