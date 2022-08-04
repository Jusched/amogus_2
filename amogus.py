from match import Match
import random

class Amogus():

    def __init__(self, color, task_list):
        self.color = str
        self.task_list = []

    def doTask(self):
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

    
    
    