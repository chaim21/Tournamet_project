def val_empty_input(txt):
    txt = txt.strip()
    if not txt:
        print("cannot except empty input")
        return False
    return True
def check_if_name_exist(team,teams):
    for t in teams:
        if t["name"].lower() == team.lower():
            print("name team already exists")
            return False
    return True
def check_if_id_exists(num,teams):
    for n in teams:
        if n["id"] == num:
            print("id team already exists")
            return False
    return True
def convert_str_to_int(num):
    try:
        num = int(num)
        if num < 0:
            print("id must be a positive number")
            return False
        return True
    except ValueError:
        print("team id must be an number")
        return False

