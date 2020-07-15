# List of all key in character dict
from math import floor
from random import random

nameKey = "name"
hpKey = "hpKey"
attackKey = "attack"
defenseKey = "defense"


def createCharacter(nom, pv, attack, defense):
    return {
        nameKey: nom,
        hpKey: pv,
        attackKey: attack,
        defenseKey: defense
    }


player = createCharacter("me", 1000, 10, 10)
monster = createCharacter("monster", 50, 5, 5)

print(max(int(floor((50 - 100) * (random()/2 + 0.5))),0))