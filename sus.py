from amogus import Amogus
from match import Match
import random

class Sus(Amogus):

    def __init__(self):

        self.task_list = None

    def kill(self, player_color, sus_color):
        dead = player_color.pop(random.randint(0, len(player_color)-1))
        print(f"{dead} has been killed. \n")
        print(player_color, sus_color)

        return 