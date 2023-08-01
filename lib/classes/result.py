from classes.player import Player
from classes.game import Game


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, int) and 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception("Score must be an integer between 0 and 5000")

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be a Player object")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(self, Game):
            self._game = game
        else:
            raise Exception("Game must be a Game object")
