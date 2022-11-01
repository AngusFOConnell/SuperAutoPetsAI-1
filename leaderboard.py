import copy
from collections import defaultdict
from operator import itemgetter
import ast
import classes

def add_to_leaderboard(team):
    team_turn = int(team.split()[0])
    team_data = team.split()[1:]

    leaderboard_dict = leaderboard_file_to_dict()
    #teams_dict = teams_file_to_dict()
    scores_dict = scores_file_to_dict()
    on_file = False

    if team_turn in leaderboard_dict.keys():
        if team_data in leaderboard_dict[team_turn]:
            on_file = True

    print(on_file)
    if on_file is False:
        if team_turn in leaderboard_dict.keys():
            teams = copy.deepcopy(leaderboard_dict[team_turn])
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
                    team1.append(classes.Pet(name, int(attack), int(health), int(level), int(exp), int(pos), held))
            for team in teams:
                team2_data = team
                score_key = tuple([team_turn] + team)
                team2_score = scores_dict[score_key]
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
                        team2.append(classes.Pet(name, int(attack), int(health), int(level), int(exp), int(pos), held))
                import simulation
                (team1_win, team2_win, draw) = simulation.turn(team1, team2)

                team1_score = team1_score + team1_win - team2_win
                team2_score = team2_score + team2_win - team1_win
                scores_dict[score_key] = team2_score

                score_key = tuple([team_turn] + team_data)
                scores_dict[score_key] = team1_score
            leaderboard_dict[team_turn].append(team_data)
        else:
            leaderboard_dict[team_turn] = [team_data]
            team1_score = 0
            score_key = tuple([team_turn] + team_data)
            scores_dict[score_key] = team1_score

        with open("leaderboard.txt", "w") as f:
            file_data = list(leaderboard_dict.items())
            f.write(str(file_data))
            f.close()

        with open("scores.txt", "w") as f:
            file_data = list(scores_dict.items())
            file_data = sorted(file_data, key=lambda x: (x[0][0], x[1]))
            f.write(str(file_data))
            f.close()
        return team1_score
    else:
        score_key = tuple([team_turn] + team_data)
        score = scores_dict[score_key]
        return score


def leaderboard_file_to_dict():
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

def teams_file_to_dict():
    with open("teams.txt", "r") as f:
        contents = f.read()
        if contents:
            teams_data = ast.literal_eval(contents)
            teams_dict = dict(teams_data)
        else:
            teams_data = []
            teams_dict = dict(teams_data)
        f.close()
    return teams_dict

def scores_file_to_dict():
    with open("scores.txt", "r") as f:
        contents = f.read()
        if contents:
            scores_data = ast.literal_eval(contents)
            scores_dict = dict(scores_data)
        else:
            scores_data = []
            scores_dict = dict(scores_data)
        f.close()
    return scores_dict


