#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    taboo = Game("taboo")
    clue = Game("clue")
    scattergories = Game("scattergories")

    xtina = Player("xtina")
    sean = Player("sean")
    bob = Player("bob")
    mary = Player("mary")

    result1 = Result(xtina, scattergories, 300)
    result2 = Result(sean, clue, 1000)
    result3 = Result(xtina, taboo, 40)

    ipdb.set_trace()
