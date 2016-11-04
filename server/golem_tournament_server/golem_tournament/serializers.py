from rest_framework import serializers
from golem_tournament.models import Armor, Golem, Engine, Weapon


class GolemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Golem
        fields = ('id',
                  'name',
                  'level',
                  'parts',
                  )


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('id',
                  'power',
                  'name',
                  'level',
                  'part_type',
                  'golem_type',
                  )


class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = ('id',
                  'power',
                  'name',
                  'level',
                  'part_type',
                  'golem_type',
                  'defense',
                  )


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('id',
                  'power',
                  'name',
                  'level',
                  'part_type',
                  'golem_type',
                  'weapon_range',
                  'damage',
                  'speed',
                  'limit',
                  )
