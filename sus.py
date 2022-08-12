from amogus import Amogus
import random

class Sus(Amogus):

    def kill(self, player_color, sus_color):
        """
        Kills a random crewmate from the ones alive. 

        Parameters:
        player_color (list): List of crewmates in order to remove a random one.
        sus_color (list): List of impostors used to make a print of the remaining ones. 
    
        Returns:
        None        
        """
        dead = player_color.pop(random.randint(0, len(player_color)-1))
        print(f"{dead} has been killed. \n")
        print(player_color, sus_color)
