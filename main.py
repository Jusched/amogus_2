# Main crea el flujo de control de todo. Solo tiene el llamado a una funcion llamado main.
# Los players deben de tener colores para que sea predefinidos al igual que el numero.  
# Reducir cantidad de inputs
# Match se encarga de todo 
# Random para asignar sus y players aleatoriamente
# Sabotage y travelVent no van
# Todo es aleatorio
# Task, kill, meeting, eject, repeat

from match import Match

if __name__ == "__main__":
    match = Match()

    print(match.choose_map())
    print(match.giveTasks())
    players = match.player_assign()
    print(players[1][4])
    #match.startMatch()
    