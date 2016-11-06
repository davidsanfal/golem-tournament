from django.contrib.auth.models import User
from rest_framework import serializers
from golem_tournament.models import Armor, Golem, Engine, Weapon


class UserSerializer(serializers.ModelSerializer):
    golems = serializers.PrimaryKeyRelatedField(many=True, queryset=Golem.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'golems')


class GolemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Golem
        fields = ('id',
                  'name',
                  'level',
                  'parts',
                  'owner',
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
