from django.utils import timezone
import datetime
from django.db import models
import factory
import random
import json

# Create your models here.


# Json String Object Serialization & Deserialization can be implemented using dumps() & loads() Method
"""
# Reading test JSON
with open('.\\Test JSON.json', 'r') as f:
    jsonloaddata = json.loads(f.read())
# Obtaining dictkeys--This is the logic which is used in backend for serialization & desrialization using keys.
for dictkeys in jsonloaddata['members']:
    (dictkeys['uid'], dictkeys['real_name'], dictkeys['tz'])
"""

# Members Model ( Additionally implemented)


class Members(models.Model):
    ok = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ok}"


# Users Model
class Users(models.Model):
    user_lists = models.ForeignKey(
        Members, null=True, related_name='members', on_delete=models.CASCADE)
    uid = models.CharField(max_length=100, blank=False)
    real_name = models.CharField(max_length=100, blank=False)
    tz = models.CharField(
        max_length=100, default=timezone.get_current_timezone_name)

    def __str__(self):
        return f"{self.uid}"

# Activity Period Model


class ActivityPeriod(models.Model):
    user_activities = models.ForeignKey(
        Users, null=True, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(
        auto_now=datetime.datetime.today() + datetime.timedelta(days=2))

    def __str__(self):
        return f"{self.user_activities}"

# UserFactory Model to generate Fake or Dummy Users Data for Testing


class UserFactory(factory.django.DjangoModelFactory):
    uid = factory.Faker('user_name')
    real_name = factory.Faker('name')
    tz = factory.Faker('timezone')

    class Meta:
        model = Users

# ActivityPeriodFactory Model to generate Fake or Dummy Activities Data for Testing


class ActivityPeriodFactory(factory.django.DjangoModelFactory):

    start_time = factory.Faker('date_time_this_month')
    end_time = factory.Faker('future_datetime')

    class Meta:
        model = ActivityPeriod
