from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

import jsonfield

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Part(models.Model):
    power = models.IntegerField(default=0)
    name = models.CharField(max_length=60)
    level = models.IntegerField()
    part_type = models.CharField(max_length=60)
    golem_type = models.CharField(max_length=60)


class Weapon(Part):
    weapon_range = models.IntegerField(default=0)
    damage = models.IntegerField(default=1)
    speed = models.IntegerField(default=1)
    limit = models.IntegerField(default=0)


class Armor(Part):
    defense = models.IntegerField(default=1)


class Engine(Part):
    pass


class Golem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='golems', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    golem_type = models.CharField(max_length=60)
    parts = jsonfield.JSONField(default = {'engine': None,
                                           'weapons': {'r': None,
                                                       'l': None},
                                            'armors': {'legr': None,
                                                       'legl': None,
                                                       'armr': None,
                                                       'arml': None,
                                                       'cabin': None,
                                                       'head': None},
                                            })
