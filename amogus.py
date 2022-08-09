from match import Match
import random

class Amogus():

    def __init__(self):
        #self.colour = []
        self.task_list = []

    def getName(self):
        self.name = str(input("Type the name you want to have for your player. "))

    def getColor(self):
        """
        Gets a color out of the ones available for the crewmates.
        
        Parameters:
        None

        self.color (str) = Random color assigned at the start of the match for 1 of the 8 crewmates instances available.

        """
        self.colour.append(self.player_color(random.randint(0, len(self.player_color)-1)))
        return self.color

    def _doTask(self):
        """
        Do a random task based on the assigned list of tasks from the Match class. 

        Parameters:
            None

        Returns:
            self.task_list (list): Task list with 1 random task less than before. 
        
        """
        self.task_list.remove(random.randint(0, len(self.task_list)-1))

    def callMeeting(self):
        """
        Calls the meeting on the Match class to eject someone.
        
        Parameters:
            None

        Returns:
            None
        """
        Match.meeting()

    
    
    