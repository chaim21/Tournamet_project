teams=[]
from Validation import *

def add_team():
    valid_name = False
    while not valid_name:
        name = input("enter team name: \n")
        if val_empty_input(name) and check_if_name_exist(name,teams):
            valid_name = True
    valid_id = False
    while not valid_id:
        id_team = input("enter team id: \n")
        if convert_str_to_int(id_team) and check_if_id_exists(id_team,teams):
            valid_id = True
    
    team = {"id": id_team, "name": name,"played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0}
    teams.append(team)
    return team

def print_menu():
    print("========== TOURNAMENT MANAGER ==========")
    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10. Check championship potential")
    print("0. Exit")
    user_choice = input("choose an action"/n)

def main():
    add_team()
    print(teams[0])
