import random
from match import Match
from amogus import Amogus
from sus import Sus

if __name__ == "__main__":
    
    match = Match()
    amogus = Amogus()
    sus = Sus()

    match.choose_map() #First thing to do when starting the game. 
    match.player_assign() #Second things to do.
    match.giveTasks() #Third thing to do. 
    print("\n")
    match.startMatch() #Conditions on which the match will be played out. 
    print(match.player_color, match.sus_color, "\n")

    task_done = 0

    while not match.is_over:

        input("Press enter to continue the game. ")

        kill_chance = random.randint(0, 1)
        if kill_chance == 1:
            sus.kill(match.player_color, match.sus_color)
            match.meeting()

        amogus.doTask(match.tasks_do)
        task_done += 1
        match.endMatch(task_done)

        if match.is_over == True:
            print("Thank your playing. ")
        
        
