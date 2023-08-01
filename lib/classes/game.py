class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # if hasattr(value, "title"):
        #     raise Exception("Title already set")
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise Exception("Title must be a string")

    def results(self, new_result=None):
        from classes.result import Result

        pass

    def players(self, new_player=None):
        from classes.player import Player

        pass

    def average_score(self, player):
        pass

    def __repr__(self):
        return f"<Game: {self.title}>"
