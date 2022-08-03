import random

class Match():
    
    def __init__(self):

        self.colors = ["Cyan", "Green", "Red", "Black", "Brown", "White", "Purple", "Lime", "Blue", "Pink"]
        self.choice = []
        self.tasks = []
        self.tasks_do = []
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
        self.choice = random.choice(list(self.map_options.keys()))
        self.tasks = self.map_options[self.choice]
        return self.choice

    def giveTasks(self):
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
                players (int): Number of crewmates the game will have. 8 default. 
                sus (int): Number of impostors the game will have. 2 default since there are 8 crewmates. 

        """
        
        sus_color = []
            
        counter = 1
        while counter <= 2:
            sus_color.append(self.colors.pop(random.randint(0,len(self.colors)-1)))
            counter += 1

        player_colors = self.colors
        #help(player_assign)
        return sus_color, player_colors

