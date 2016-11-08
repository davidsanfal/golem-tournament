from django.db import models
from django.conf import settings


class Part(models.Model):
    power = models.IntegerField(default=0)
    name = models.CharField(max_length=60)
    level = models.IntegerField()
    part_type = models.CharField(max_length=60)
    golem_type = models.CharField(max_length=60)


class Weapon(Part):
    weapon_range = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    speed = models.IntegerField(default=1)
    limit = models.IntegerField(default=0)


class Armor(Part):
    defense = models.IntegerField(default=0)


class Engine(Part):
    pass


class Golem(models.Model):
    owner = models.ForeignKey('auth.User',
                              related_name='golems',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    golem_type = models.CharField(max_length=60)
    engine = models.IntegerField(default=0)
    right_weapon = models.IntegerField(default=0)
    left_weapon = models.IntegerField(default=0)
    right_leg = models.IntegerField(default=0)
    left_leg = models.IntegerField(default=0)
    right_arm = models.IntegerField(default=0)
    left_arm = models.IntegerField(default=0)
    cabin = models.IntegerField(default=0)
    helm = models.IntegerField(default=0)

    def can_be_equipped(self, part):
        return part.golem_type == self.golem_type

    def equip_item(self, part):
        setattr(self, part.part_type, part.id)

    def equipment(self):
        return {'engine': Engine.objects.get(pk=self.engine),
                'weapons': {'right': Weapon.objects.get(pk=self.right_weapon),
                            'left': Weapon.objects.get(pk=self.right_weapon)},
                'armors': {'right_leg': Armor.objects.get(pk=self.right_leg),
                           'left_leg': Armor.objects.get(pk=self.left_leg),
                           'right_arm': Armor.objects.get(pk=self.right_arm),
                           'left_arm': Armor.objects.get(pk=self.left_arm),
                           'cabin': Armor.objects.get(pk=self.cabin),
                           'head': Armor.objects.get(pk=self.head)}}
