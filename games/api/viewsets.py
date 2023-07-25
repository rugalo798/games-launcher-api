from rest_framework import viewsets
from games.api import serializers
from games import models

class GamesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GamesSerializer
    queryset = models.Games.objects.all()