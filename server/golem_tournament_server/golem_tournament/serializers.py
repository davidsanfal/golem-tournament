from django.contrib.auth.models import User
from rest_framework import serializers
from golem_tournament.models import Armor, Golem, Engine, Weapon


class UserSerializer(serializers.ModelSerializer):
    golems = serializers.PrimaryKeyRelatedField(many=True, queryset=Golem.objects.all(), default=[])

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'golems')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, obj):
        return {'username': obj.username}


class GolemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Golem
        fields = ('id',
                  'name',
                  'golem_type',
                  'owner',
                  )

    def to_representation(self, obj):
        return {
            'name': obj.name,
            'golem_type': obj.golem_type,
            'owner': obj.owner.username,
            'equip': obj.equipment,

        }


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
