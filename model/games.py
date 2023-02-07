import json
import random

games_data = []
games_list = [
    {"car1": "0.17"},
    {"car2": "0.16"},
    {"car3": "0.09"},
    {"car4": "0.22"},
]

def getgame():
    return (games_data)

def getgame_a():
    return (games_data[id])

def getvar1():
    r = str(games_list[0]["car1"])
    return r

def getvar2():
    r = str(games_list[1]["car2"])
    return r

def getvar3():
    r = str(games_list[2]["car3"])
    return r

def getvar4():
    r = str(games_list[3]["car4"])
    return r