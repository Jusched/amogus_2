from match import Match
import random

class Amogus():

    def __init__(self):
        pass


    def doTask(self, tasks_do):
        """
        Do a random task based on the assigned list of tasks from the Match class. 

        Parameters:
            None

        Returns:
            task_do (list): Task list with 1 random task less than before. 
        
        """
        task_out = tasks_do.pop(random.randint(0, len(tasks_do)-1))
        print(f"{task_out} has been completed. \n")

    def callMeeting(self):
        """
        Calls the meeting on the Match class to eject someone.
        
        Parameters:
            None

        Returns:
            None
        """
        Match.meeting()

