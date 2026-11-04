def check_empty(txt):
    txt = txt.strip()
    if not txt:
        print("must be none empty")
        return False
    return True

def validate_num(num):
    try:
        num = int(num)
    except ValueError:
        print("must be an number")
        return False
    if num <= 0:
        print("number must be grater than 0")
        return False
    return True



def team_exists(team,teams):
    for t in teams:
        if t["name"].lower() == team.lower():
            return False
    return True

def validate_team(team,teams):
    team = team.strip()
    if not team:
        return(False,"cannot except empty input")
    if not team_exists(team,teams):
        return(False,"name team already exists")
    return True,None

def id_exists(num,teams):
    for n in teams:
        if n["id"] == num:
            return False
    return True

def validate_id(num,teams):
    try:
        num = int(num)
    except ValueError:
        return(False,"team id must be an number")
    if num <= 0:
        return(False,"id must be a positive number")
    if not id_exists(num,teams):
        return(False,"id team already exists")
    return True,None
        
