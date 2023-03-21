from django.shortcuts import render
from .models import NaturesGarden
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NatureSerializer

# Create your views here.
class NaturegardenViewSet(viewsets.ModelViewSet):
    queryset = NaturesGarden.objects.all()
    
    serializer_class = NatureSerializer
    
    permission_classes = [permissions.AllowAny]