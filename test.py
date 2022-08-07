import random

current_players = ["Blue", "Red", "Orange", "Green"]


unlucky = current_players.pop(random.randint(0, len(current_players)-1))
print(f"{unlucky} has been ejected. ")