from match import Match
import random

class Amogus():

    def doTask(self, tasks_do):
        """
        Do a random task based on the assigned list of tasks from the Match class. 

        Parameters:
            tasks_do (list): List where all the available tasks are.

        Returns:
            None
        
        """
        task_out = tasks_do.pop(random.randint(0, len(tasks_do)-1))
        print(f"{task_out} has been completed. \n")
