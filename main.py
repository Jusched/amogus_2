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

if __name__ == "__main__":
    match = Match()

    match.choose_map()
    
    match.player_assign()
    match.giveTasks()
    #print(players[1][4])
    #match.startMatch()
    #print(match.sus_color, match.player_color) Test colors for sus and crewmates
    
    #total_sus = [("sus"+i) = Match(), for i in range(0,len(match.sus_color))]

    #total_crew = [("crew"+i) = Match(), for i in range(0,len(match.player_color))]

    #match.assignColor()

    #match.assignColor()
    #match.assignColor()
    #print(match.sus_color, match.player_color)

