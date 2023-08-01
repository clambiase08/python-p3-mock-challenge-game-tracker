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
