class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else:
            raise Exception("Invalid username")

    def results(self, new_result=None):
        from classes.result import Result

        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [result.game for result in self.results()]

    def played_game(self, game):
        # return any([result for result in self.results() if result.game == game])
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        # players = {}
        # for player in cls.all:
        #     if player.played_game(game):
        #         total_score = sum(
        #             [result.score for result in player.results() if result.game == game]
        #         )
        #         num_scores = player.num_times_played(game)

        #         if num_scores > 0:
        #             average_score = total_score / num_scores
        #         else:
        #             average_score = 0
        #         players[player] = average_score

        # if not players:
        #     return None

        # return max(players)

        # if cls.all:
        #     max_player = None
        #     max_score = 0
        #     for player in cls.all:
        #         if game.average_score(player) > max_score:
        #             max_player = player
        #             max_score = game.average_score(player)
        #     return max_player
        # return None

        return max(cls.all, key=lambda player: game.average_score(player))

    def __repr__(self):
        return f"<Player: {self.username}>"
