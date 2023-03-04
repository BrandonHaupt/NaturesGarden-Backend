from .models import NaturesGarden
from rest_framework import serializers

class NatureSerializer(serializers.HyperlinkedModelSerializer):
    model = NaturesGarden
    fields = ['id', 'url', 'name', "edible", "origin", "benefits", "description"]