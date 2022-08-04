import random

class Match():
    
    def __init__(self):

        self.colors = ["Cyan", "Green", "Red", "Black", "Brown", "White", "Purple", "Lime", "Blue", "Pink"]
        self.choice = []
        self.tasks = []
        self.tasks_do = []
        self.sus_color = []
        self.player_color = []
        self.counter = 0
        self.map_options = {
            "Skeld":["Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Key turn"
            ],
            "Mira HQ":["Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Key turn"
            ],
            "Polus":["Data", "Artifacts", "Reactor", "Calibrate",
            "Toilet", "Decontaminate", "Key turn"
            ]
        }

    def choose_map(self):
        """
        Selects the map in which the game is going to be played based on map_options attribute.

        Parameters:
        Nothing

        Returns:
        self.choice: string chosen randomnly based on the map_options dictionary, which is used later for assigning the tasks.        
        """
        self.choice = random.choice(list(self.map_options.keys()))
        self.tasks = self.map_options[self.choice]
        return self.choice

    def giveTasks(self):
        """
        Selects the tasks which each crewmates will have.

        Parameters:
        None

        Returns:
        self.tasks_do: List containing 4 randomnly chosen tasks based on self.choice map. 
        """
        total_tasks = self.tasks.copy()
        while self.counter <= 3:
            removed = total_tasks.pop(random.randint(0,len(total_tasks)-1))
            self.tasks_do.append(removed)
            self.counter += 1
        self.counter = 0
        return self.tasks_do



    def player_assign(self):
        """
            Player assignment.

                Gives the players and impostors a color.

            Parameters:
                colors (list): Colors for the players available for the game. Max 10
            
            Returns:
                self.sus_color (list): Colors the impostors will have available (2)
                self.player_color (list): Colors the crewmates will have available (8)
        """
        
        self.sus_color = []
            
        counter = 1
        while counter <= 2:
            self.sus_color.append(self.colors.pop(random.randint(0,len(self.colors)-1)))
            counter += 1

        self.player_color = self.colors
        #help(player_assign)
        return

    def assignColor(self):
        """
        Assigns a color based if it was chosen to be a impostor or crewmate. 

        Parameters:
        None

        Returns:
        color (str): Color which is assigned randomnly after assigning randomnly if the player will be a impostor or crewmate.
        
        """
        luck = random.randint(1,2)
        if luck == 1:
            color = random.randint(0, len(self.sus_color)-1)
            self.sus_color.pop(color)
            
        if self.sus_color == []:
            luck = 2
        else:
            color = random.randint(0, len(self.player_color)-1)
            self.player_color.pop(color)
        
    def startMatch(self, choice, tasks_do):
        pass

    def meeting(self):
        pass