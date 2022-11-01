import leaderboard

def team_data(team_1, turn_number):
    original_stdout = sys.stdout
    with open('team_data.txt', 'a') as f:
        sys.stdout = f
        print(turn_number, end=" ")
        for pet in team_1:
            print(pet.name, end=" ")
            print(pet.attack, end=" ")
            print(pet.health, end=" ")
            print(pet.level, end=" ")
            print(pet.exp, end=" ")
            print(pet.pos, end=" ")
            print(pet.held, end=" ")
        print()
        sys.stdout = original_stdout
        f.close()

def sort_data():
    new = []
    with open("team_data.txt", "r") as f:
        for line in f:
            stripped = line.strip("\n")
            new.append(stripped)

    new.sort(key=sort_turn_number)
    with open("team_data.txt", "w") as file:
        for k in new:
            file.write(k + "\n")

def sort_turn_number(line):
    return int(line.split()[0])

def team_data_to_leaderboard():
    with open("team_data.txt", "r") as team_data:
        for line in team_data:
            stripped = line.strip("\n")
            leaderboard.add_to_leaderboard(stripped)
        team_data.close()

team_data_to_leaderboard()