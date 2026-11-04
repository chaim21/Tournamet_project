from Validation import *
from inputs import *
teams=[{"id": 1, "name": "Maccabi", "played": 4,
     "wins": 2, "draws": 1, "losses": 1,
     "goals_for": 6, "goals_against": 4, "points": 7},
    {"id": 2, "name": "Hapoel", "played": 4,
     "wins": 0, "draws": 0, "losses": 4,
     "goals_for": 2, "goals_against": 8, "points": 0}]
matches = [{"home_team_id": 1, "away_team_id": 2,
            "home_goals": 3, "away_goals": 1}]

def add_team():
    valid_name = False
    while not valid_name:
        name = ask_input("enter team name: \n")
        is_valid , msg = validate_team(name,teams)
        if not is_valid:
            print(msg)
        else:
            valid_name = True
    valid_id = False
    while not valid_id:
        id_team = ask_input("enter id team: \n")
        is_valid , msg = validate_id(id_team,teams)
        if not is_valid:
            print(msg)
        else:
            valid_id = True
    
    team = {"id": id_team, "name": name,"played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0}
    teams.append(team)
    return team

def show_teams(teams):
    if not teams:
        print("No teams to display")
    else:
        for team in teams:
            print(f"id: {team["id"]}, name: {team["name"]}, played: {team["played"]}, points: {team["points"]}\n",end="")

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
    user_choice = input("choose an action\n")
    return user_choice

def add_match(matches):
    while True:
        home_team = ask_input("enter home team id: \n")
        if not check_empty(home_team):
            continue
        if not validate_num(home_team):
            continue
        if not id_exists(int(home_team),teams):
            break
        else:
            print("team not exist")
    while True:
        away_team = ask_input("enter away team id: \n")
        if not check_empty(away_team):
            continue
        if not validate_num(away_team):
            continue
        if away_team == home_team:
            print("team cannot play again itself")
            continue
        if not id_exists(int(away_team),teams):
            for match in matches:
                id_teams = (match["home_team_id"],match["away_team_id"])
                if home_team in id_teams and away_team in id_teams:
                    print("They have already played together ")
                    continue
            break
        else:
            print("team not exist")
    while True:
        home_goals = ask_input("enter home goals: \n")
        if not check_empty(home_goals):
            continue
        if not validate_num(home_goals):
            continue
        break
    while True:
        away_goals = input("enter away goals: \n")
        if not check_empty(away_goals):
            continue
        if not validate_num(away_goals):
            continue
        break
    match = {"home_team_id": home_team, "away_team_id": away_team,
            "home_goals": home_goals, "away_goals": away_goals}    
    matches.append(match)
    if home_goals > away_goals:
        pass
def update_team_data(team_id,goals_for,goals_against,status):
    for team in teams:
        if team["team id"] == team_id:
            team["goals_for"] += goals_for
            team["goals_against"] += goals_against
            team["played"] += 1
            team[status] += 1

def game_flow():
    while True:
        choose = print_menu()
        if choose == "1":
            add_team()
        elif choose == "2":
            show_teams(teams)
def main():
    game_flow()
add_team()