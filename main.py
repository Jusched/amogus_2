# Main crea el flujo de control de todo. Solo tiene el llamado a una funcion llamado main.
# Los players deben de tener colores para que sea predefinidos al igual que el numero.  
# Reducir cantidad de inputs
# Match se encarga de todo 
# Random para asignar sus y players aleatoriamente
# Sabotage y travelVent no van
# Todo es aleatorio
# Task, kill, meeting, eject, repeat

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
    match.assignColor() #Fourth.
    match.startMatch() #Conditions on which the match will be played out. 
    print(match.sus_color, match.sus_color)
    print(match.current_players)
    #sus._getColor()
    #print(sus.color)
    match.meeting() #Meeting where a random color is out. 
    sus.kill()
    print(match.colors)
