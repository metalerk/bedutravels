from rest_framework import serializers
from tours.models import (
    User as tours_user,
    Zone,
    Tour,
)

class TourUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tours_user
        fields = (
            'id', 
            'name', 
            'last_name', 
            'nickname', 
            'email', 
            'birthday', 
            'gender', 
            'key', 
            'type',
            'timestamp',
        )


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class TourSerializer(serializers.HyperlinkedModelSerializer):
    takeoff_zone = ZoneSerializer(read_only=True)
    arrival_zone = ZoneSerializer(read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'