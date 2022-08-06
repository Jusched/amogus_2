from match import Match
import random

class Amogus():

    def __init__(self):
        self.color = str
        self.task_list = []

    def __getColor(self):
        """
        Gets a color out of the ones available for the crewmates.
        
        Parameters:
        None

        self.color (str) = Random color assigned at the start of the match for 1 of the 8 crewmates instances available.

        """
        self.color.append(Match.sus_color(random.randrange(0, len(Match.sus_color)-1)))
        return self.color

    def __doTask(self):
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
        pass
        Match.meeting()

    
    
    