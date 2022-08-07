from amogus import Amogus
from match import Match
import random

class Sus(Amogus):

    def __init__(self):
        self.name = str
        self.color = str

    def _getColor(self):
        """
        Gets a color out of the ones available for the impostors.

        Parameters:
        None

        Returns:
        self.color (str) = Random color assigned at the start of the match for 1 of the 2 impostor instances available.
        
        """
        self.color.append(Match.sus_color(random.randint(0, len(Match.sus_color)-1)))
        return self.color

    def kill(self):
        pass #Not working as of today. 
        dead = Match.colors.pop(random.randint(0, len(Match.colors)-1))
        Match.colors.remove(dead)
        print(f"{dead} has been killed. ")
        Match.endMatch()
        return Match.colors