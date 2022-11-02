import random, copy
import classes


def actions(shop, team):
    # shop = [[pets], [food], gold]
    actions = []
    gold = shop[2]
    pets = shop[0]
    foods = shop[1]
    if gold > 3:
        if len(team) < 5:
            pos_count = 0
            for pet in pets:
                actions.append(["buy_pet", pet, len(team), pos_count])
                pos_count += 1
        pos_count = 0
        for shop_pet in pets:
            for team_pet in team:
                if shop_pet.name == team_pet.name and team_pet.level < 3:
                    actions.append(["level", shop_pet, team_pet.pos, pos_count])
            pos_count += 1
        for food in foods:
            for pet in team:
                actions.append(["buy_food", food, pet.pos])
    for pet in team:
        actions.append(["sell", pet, pet.pos])
    # if gold > 1:
        # actions.append(["roll"])
    # actions.append(["end_of_turn"])
    return actions

def simulate_action(action, team, shop):
    # shop = [[pets], [food], gold]]
    temp_team = copy.deepcopy(team)
    temp_shop = copy.deepcopy(shop)
    gold = temp_shop[2]
    if action[0] == "buy_pet":
        gold -= 3
        pet = action[1]
        if pet.name == "otter":
            if len(temp_team) > 0:
                choices = random.sample(temp_team, 1)
                for buff_target in choices:
                    buff_target.attack = buff_target.attack + 1
                    buff_target.health = buff_target.health + 1
        for other_pet in temp_team:
            if other_pet.name == "horse":
                pet.attack = pet.attack + other_pet.level
        temp_team.append(classes.Pet(pet.name, pet.attack, pet.health, 1, 0, action[2], None))
        temp_shop[0].pop(action[3])
        import simulation
        temp_team = simulation.sort_team(temp_team)
    if action[0] == "sell":
        gold += 1
        pet = action[1]
        temp_team.pop(action[2])
        import simulation
        temp_team = simulation.sort_team(temp_team)
        if pet.name == "beaver":
            choices = random.sample(temp_team, min(len(temp_team), 2))
            for buff_target in choices:
                buff_target.health = buff_target.health + pet.level
        if pet.name == "pig":
            temp_shop[2] = temp_shop[2] + pet.level
        if pet.name == "duck":
            for shop_pet in temp_shop[0]:
                shop_pet.health = shop_pet.health + pet.level
    if action[0] == "level":
        gold -= 3
        pet = action[1]
        team_pet = temp_team[action[2]]
        if team_pet.exp < 2:
            team_pet.exp += 1
            team_pet.attack += 1
            team_pet.health += 1
        elif team_pet.exp == 2:
            team_pet.level += 1
            team_pet.exp = 0
            team_pet.attack += 1
            team_pet.health += 1
            if pet.name == "fish":
                for other_pet in temp_team:
                    if other_pet is not team_pet:
                        other_pet.health = other_pet.health + team_pet.level
                        other_pet.attack = other_pet.attack + team_pet.level
        if pet.name == "otter":
            if len(temp_team) > 1:
                friendly_pets = []
                for other_pet in temp_team:
                    if other_pet is not team_pet:
                        friendly_pets.append(other_pet)
                choices = random.sample(friendly_pets, team_pet.level)
                for buff_target in choices:
                    buff_target.attack = buff_target.attack + 1
                    buff_target.health = buff_target.health + 1

    if action[0] == "buy_food":
        gold -= 3
        food = action[1]
        if food == "apple":
            temp_team[action[2]].attack += 1
            temp_team[action[2]].health += 1
        elif food == "honey":
            temp_team[action[2]].held = "honey"
        temp_shop[1].remove(food)
    if action[0] == "roll":
        gold -= 1
    return temp_team, temp_shop[0], temp_shop[1], gold









