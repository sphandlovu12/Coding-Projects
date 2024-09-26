# game_manager/views.py

from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def play_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'play_game.html', {'game': game})