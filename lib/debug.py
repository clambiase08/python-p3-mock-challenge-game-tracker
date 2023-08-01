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

    ipdb.set_trace()
