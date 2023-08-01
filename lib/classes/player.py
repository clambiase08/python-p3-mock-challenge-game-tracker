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

    def games_played(self, new_game=None):
        from classes.game import Game

        return [result.game for result in self.results() if result.player == self]

    def played_game(self, game):
        return any(
            [
                result
                for result in self.results()
                if result.player == self and result.game == game
            ]
        )

    def num_times_played(self, game):
        return len(
            [
                result
                for result in self.results()
                if result.player == self and result.game == game
            ]
        )

    @classmethod
    def highest_scored(cls, game):
        players = {}
        for player in cls.all:
            if player.played_game(game):
                total_score = sum(
                    [result.score for result in player.results() if result.game == game]
                )
                num_scores = player.num_times_played(game)

                if num_scores > 0:
                    average_score = total_score / num_scores
                else:
                    average_score = 0
                players[player] = average_score

        if not players:
            return None

        return max(players)

    def __repr__(self):
        return f"<Player: {self.username}>"
