from .models import NaturesGarden
from rest_framework import serializers

class NatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NaturesGarden
        fields = ['id', 'url', 'name', "edible", "origin", "benefits", "description"]