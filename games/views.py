from django.shortcuts import render
from .models import Games
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class game_details(APIView):
    def delete(self, request, id=None):
        games = Games.objects.filter(id_game=id)
        games.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)