import random

class Match():
    
    def __init__(self):

        self.colors = ["Cyan", "Green", "Red", "Black", "Brown", "White", "Purple", "Lime", "Blue", "Pink"]
        self.map_choice = []
        self.tasks = []
        self.tasks_do = []
        self.sus_color = []
        self.player_color = []
        self.is_over = False
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
        None

        Returns:
        self.choice: string chosen randomnly based on the map_options dictionary, which is used later for assigning the tasks.        
        """
        self.map_choice = random.choice(list(self.map_options.keys()))
        self.tasks = self.map_options[self.map_choice]


    def giveTasks(self):
        """
        Selects the tasks which each crewmates will have.

        Parameters:
        None

        Returns:
        self.tasks_do: List containing 4 randomnly chosen tasks based on self.choice map. 
        """
        total_tasks = self.tasks.copy()
        while self.counter <= 4:
            removed = total_tasks.pop(random.randint(0,len(total_tasks)-1))
            self.tasks_do.append(removed)
            self.counter += 1
        self.counter = 0



    def player_assign(self):
        """
        Player assignment.

            Gives the players and impostors a color.

        Parameters:
            None
        
        Returns:
            None
        """
            
        counter = 1
        while counter <= 2:
            self.sus_color.append(self.colors.pop(random.randint(0,len(self.colors)-1)))
            counter += 1

        self.player_color = self.colors.copy()
        print(self.player_color, self.sus_color)

        
    def startMatch(self):
        """
        Starts the match with the selected map, impostors and crewmates. 

        Parameters:
        None

        Returns:
        None
        """
        print(f"The match will start on the map {self.map_choice} with {self.sus_color} as the impostors and {self.player_color} as the crewmates.")

    def meeting(self):
        """
        Starts a meeting where a random player is ejected. 

        Parameters:
        None

        Returns:
        New list without the ejected player.
        """
        
        unlucky = self.colors.pop(random.randint(0, len(self.colors)-1))
        print(f"{unlucky} has been ejected. \n")
        print(self.sus_color, self.player_color)

    def endMatch(self, task_done):

        if len(self.sus_color) < len(self.player_color) and task_done < 5:
            self.is_over = False

        elif len(self.sus_color) == 0:
            print("The match has ended and the crewmates have won. ")
            self.is_over = True

        elif len(self.sus_color) == len(self.player_color):
            print("The match has ended and the impostors have won. ")
            self.is_over = True
        
        elif task_done == 5:
            print("The match has ended and the crewmates have won. ")
            self.is_over = True