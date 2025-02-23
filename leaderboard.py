from collections import defaultdict
from operator import itemgetter
import ast
import simulation
import classes

def add_to_leaderboard(team):
    team_turn = int(team.split()[0])
    team_data = team.split()[1:]

    leaderboard_dict = file_to_dict()
    on_file = False

    if team_turn in leaderboard_dict.keys():
        teams = leaderboard_dict[team_turn]
        if team_turn < 3:
            loss_weight = 1
        elif team_turn < 5:
            loss_weight = 2
        else:
            loss_weight = 3
        count = 0
        team1 = []
        team1_score = 0
        for data in team_data:
            if count == 0:
                name = data
                count += 1
            elif count == 1:
                attack = data
                count += 1
            elif count == 2:
                health = data
                count += 1
            elif count == 3:
                level = data
                count += 1
            elif count == 4:
                exp = data
                count += 1
            elif count == 5:
                pos = data
                count += 1
            elif count == 6:
                if data == "None":
                    held = None
                else:
                    held = data
                count = 0

                team1.append(classes.Pet(name, int(health), int(attack), int(level), int(exp), int(pos), held))
        for team in teams:
            team2_data = team[:-1]
            team2_score = float(team[-1])
            count = 0
            team2 = []
            for data in team2_data:
                if count == 0:
                    name = data
                    count += 1
                elif count == 1:
                    attack = data
                    count += 1
                elif count == 2:
                    health = data
                    count += 1
                elif count == 3:
                    level = data
                    count += 1
                elif count == 4:
                    exp = data
                    count += 1
                elif count == 5:
                    pos = data
                    count += 1
                elif count == 6:
                    if data == "None":
                        held = None
                    else:
                        held = data
                    count = 0
                    team2.append(classes.Pet(name, int(health), int(attack), int(level), int(exp), int(pos), held))
            if team1 == team2:
                team1_score = team2_score
                on_file = True
                break
            (team1_win, team2_win, draw) = simulation.turn(team1, team2)
            team1_score = team1_score + team1_win - (team2_win * loss_weight)
            team2_score = team2_score + team2_win - (team1_win * loss_weight)
            team[-1] = team2_score
        if not on_file:
            team_data.append(team1_score)
            leaderboard_dict[team_turn].append(team_data)
    else:
        team_data.append("0")
        leaderboard_dict[team_turn] = [team_data]
        team1_score = 0

    if not on_file:
        with open("leaderboard.txt", "w") as f:
            for key in leaderboard_dict.keys():
                teams = leaderboard_dict[key]
                leaderboard_dict[key] = sorted(teams, reverse=True, key=itemgetter(-1))

            file_data = list(leaderboard_dict.items())
            f.write(str(file_data))
            f.close()


    return team1_score

def file_to_dict():
    with open("leaderboard.txt", "r") as f:
        contents = f.read()
        if contents:
            leaderboard_data = ast.literal_eval(contents)
            leaderboard_dict = dict(leaderboard_data)
        else:
            leaderboard_data = []
            leaderboard_dict = dict(leaderboard_data)
        f.close()
    return leaderboard_dict

