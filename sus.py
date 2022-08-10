from amogus import Amogus
from match import Match
import random

class Sus(Amogus):

    def __init__(self):
        self.name = str
        self.colors = []
        self.task_list = None

    def kill(self, player_color):
        #Not working as of today. 
        dead = player_color.pop(random.randint(0, len(player_color)-1))
        print(f"{dead} has been killed. ")
        #Match.endMatch(self)
        print(player_color)
        return 