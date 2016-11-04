from django.db import models
import jsonfield


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
