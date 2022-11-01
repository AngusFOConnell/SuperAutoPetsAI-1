import random, copy, sys
import classes
import shop

def turn(team_1, team_2):
    debug = 0

    team1_win = 0
    team2_win = 0
    draw = 0

    number_of_battles = 50
    for battle in range(0, number_of_battles):
        team1 = copy.deepcopy(team_1)
        team2 = copy.deepcopy(team_2)
        if debug:
            for pet in team1:
                print(pet.name)
            for pet in team2:
                print(pet.name)
            frame = 0
            print("-------------START OF BATTLE -------------")

        #End of Turn abilities
        (team1, team2) = end_of_turn(team1, team2)

        #Start of Battle abilities
        (team1, team2) = start_of_battle(team1, team2)

        while (len(team1) > 0 and len(team2) > 0):
            if debug:
                frame += 1
                print("-------------FRAME " + str(frame) + "-------------")
                print("TEAM 1: ")
                for pet in team1:
                    print(pet.name, end =" ")
                    print(pet.attack, end=" ")
                    print(pet.health, end=" ")
                print()
                print("TEAM 2: ")
                for pet in team2:
                    print(pet.name, end =" ")
                    print(pet.attack, end=" ")
                    print(pet.health, end=" ")
                print()

            #Before Attack
            (team1, team2, team1_attack, team2_attack) = before_attack(team1, team2)

            if (team1_attack and team2_attack):
                (team1, team2, team1_attack, team2_attack) = attack(team1, team2, team1_attack, team2_attack)

        if len(team1) > 0:
            team1_attack = team1[0]
        else:
            team1_attack = None

        if len(team2) > 0:
            team2_attack = team2[0]
        else:
            team2_attack = None


        if team2_attack:
            if debug:
                print("-------------LOSS-------------")
                for pet in team2:
                    if pet is not None:
                        print(pet.name, pet.attack, pet.health)
            team2_win += 1
        elif team1_attack:
            if debug:
                print("-------------WIN-------------")
                for pet in team1:
                    if pet is not None:
                        print(pet.name, pet.attack, pet.health)
            team1_win += 1
        else:
            if debug:
                print("-------------DRAW-------------")
            draw += 1
    return(float(team1_win/number_of_battles), float(team2_win/number_of_battles), float(draw/number_of_battles))
def get_pos(pet):
    return pet.pos

def get_atk(pet):
    return pet.attack

def get_hp(pet):
    return pet.health

def end_of_turn(team1, team2):
    team1_ability_copy = team1.copy()
    team2_ability_copy = team2.copy()
    ability_order = team1_ability_copy + team2_ability_copy
    ability_order.sort(key=get_pos, reverse=True)
    ability_order.sort(key=get_atk, reverse=True)

    for pet in ability_order:
        if pet.name == "parrot":
            if pet.pos != 0:
                if pet in team1:
                    pet.name = team1[pet.pos - 1].name
                elif pet in team2:
                    pet.name = team2[pet.pos - 1].name
                else:
                    print("ERROR")
    return team1, team2


def start_of_battle(team1, team2):
    team1_ability_order = team1.copy()
    team2_ability_order = team2.copy()
    ability_order = team1_ability_order + team2_ability_order
    ability_order.sort(key=get_pos, reverse=True)
    ability_order.sort(key=get_atk, reverse=True)

    for pet in ability_order:
        if pet in team1:
            (ability_repeat, tiger_level) = tiger(pet, team1)
        else:
            (ability_repeat, tiger_level) = tiger(pet, team2)

        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = pet.level
            else:
                level = tiger_level

            if pet.name == "mosquito":
                if pet in team1:
                    choices = random.sample(team2, min(level, len(team2)))
                    for team2_pet in choices:
                        team2_pet = damage(team2_pet, 1)
                        (team1, team2) = post_damage_checks(team1, team2)


                elif pet in team2:
                    choices = random.sample(team1, min(level, len(team1)))
                    for team1_pet in choices:
                        team1_pet = damage(team1_pet, 1)
                        (team1, team2) = post_damage_checks(team1, team2)

            if pet.name == "dolphin":
                if pet in team1:
                        for trigger in range(0, level):
                            if len(team2) > 0:
                                team2_copy = team2.copy()
                                team2_copy.sort(key=get_hp)
                                lowest_hp_pets = []
                                for pet in team2_copy:
                                    if pet.health == team2_copy[0].health:
                                        lowest_hp_pets.append(pet)
                                choice = random.sample(lowest_hp_pets, 1)
                                choice[0] = damage(choice[0], 3)
                                (team1, team2) = post_damage_checks(team1, team2)
                elif pet in team2:
                    for trigger in range(0, level):
                        if len(team1) > 0:
                            team1_copy = team1.copy()
                            team1_copy.sort(key=get_hp)
                            lowest_hp_pets = []
                            for pet in team1_copy:
                                if pet.health == team1_copy[0].health:
                                    lowest_hp_pets.append(pet)
                            choice = random.sample(lowest_hp_pets, 1)
                            choice[0] = damage(choice[0], 3)
                            (team1, team2) = post_damage_checks(team1, team2)

            if pet.name == "skunk":
                if pet in team1:
                    team2_copy = team2.copy()
                    team2_copy.sort(key=get_hp, reverse=True)
                    highest_hp_pets = []
                    for team2_pet in team2_copy:
                        if team2_pet.health == team2_copy[0].health:
                            highest_hp_pets.append(team2_pet)
                    choice = random.sample(highest_hp_pets, 1)
                    if level == 1:
                        choice[0].health = int(choice[0].health * 0.66)
                    elif level == 2:
                        choice[0].health = int(choice[0].health * 0.33)
                    else:
                        choice[0].health = 1
                elif pet in team2:
                    team1_copy = team1.copy()
                    team1_copy.sort(key=get_hp, reverse=True)
                    highest_hp_pets = []
                    for team1_pet in team1_copy:
                        if team1_pet.health == team1_copy[0].health:
                            highest_hp_pets.append(team1_pet)
                    choice = random.sample(highest_hp_pets, 1)
                    if level == 1:
                        choice[0].health = int(choice[0].health * 0.66)
                    elif level == 2:
                        choice[0].health = int(choice[0].health * 0.33)
                    else:
                        choice[0].health = 1

            if pet.name == "dodo":
                if pet in team1:
                    if pet.pos > 0:
                        pre_atk = team1[pet.pos - 1].attack
                        team1[pet.pos - 1].attack = team1[pet.pos - 1].attack + int((pet.attack / 2) * level)
                elif pet in team2:
                    if pet.pos > 0:
                        pre_atk = team2[pet.pos - 1].attack
                        team2[pet.pos - 1].attack = team2[pet.pos - 1].attack + int((pet.attack / 2) * level)

            #TIGER
            if pet.name == "whale":
                if pet in team1:
                    if pet.pos > 0:
                        pet.swallowed = copy.copy(team1[pet.pos - 1])
                        pet.swallowed.swallowed = None
                        pet.swallowed.held = None
                        team1[pet.pos - 1].health = 0
                        (team1, team2) = post_damage_checks(team1, team2)
                elif pet in team2:
                    if pet.pos > 0:
                        pet.swallowed = copy.copy(team2[pet.pos - 1])
                        pet.swallowed.swallowed = None
                        pet.swallowed.held = None
                        team2[pet.pos - 1].health = 0
                        (team1, team2) = post_damage_checks(team1, team2)

            if pet.name == "crocodile":
                if pet in team1:
                    for trigger in range(0, level):
                        team2_copy = team2.copy()
                        team2_copy.sort(key=get_pos, reverse=True)
                        if len(team2_copy) > 0:
                            team2_copy[0] = damage(team2_copy[0], 8)
                            (team1, team2) = post_damage_checks(team1, team2)
                elif pet in team2:
                    for trigger in range(0, level):
                        team1_copy = team1.copy()
                        team1_copy.sort(key=get_pos, reverse=True)
                        if len(team1_copy) > 0:
                            team1_copy[0] = damage(team1_copy[0], 8)
                        (team1, team2) = post_damage_checks(team1, team2)

            if pet.name == "crab":
                if pet in team1:
                    team1_copy = team1.copy()
                    team1_copy.sort(key=get_hp, reverse=True)
                    for other_pet in team1_copy:
                        if other_pet.name != pet:
                            pet.health = int((other_pet.health / 2) * level)
                            break
                if pet in team2:
                    team2_copy = team2.copy()
                    team2_copy.sort(key=get_hp, reverse=True)
                    for other_pet in team2_copy:
                        if other_pet.name != pet:
                            pet.health = int((other_pet.health / 2) * level)
                            break

            if pet.name == "leopard":
                if pet in team1:
                    choices = random.sample(team2, min(level, len(team2)))
                    for team2_pet in choices:
                        team2_pet = damage(team2_pet, int(pet.attack / 2))
                        (team1, team2) = post_damage_checks(team1, team2)
                elif pet in team2:
                    choices = random.sample(team1, min(level, len(team1)))
                    for team1_pet in choices:
                        team1_pet = damage(team1_pet, int(pet.attack / 2))
                        (team1, team2) = post_damage_checks(team1, team2)

    return team1, team2


def post_damage_checks(team1, team2):
    (team1, team2, team1_fainted, team2_fainted) = faint_check(team1, team2)
    (team1, team2) = hurt(team1, team2)
    (team1, team2) = faint(team1, team2, team1_fainted, team2_fainted)

    return team1, team2


def faint_check(team1, team2):
    team1_copy = team1.copy()
    team2_copy = team2.copy()

    team1_fainted = []
    team2_fainted = []

    for pet in team1_copy:
        if pet.health <= 0:
            fainted_pet = copy.deepcopy(pet)
            (team1, team2, team1_fainted) = before_faint(team1, team2, pet, team1_fainted)
            if pet in team1:
                team1.remove(pet)
                team1_fainted.append(fainted_pet)

    for pet in team2_copy:
        if pet.health <= 0:
            fainted_pet = copy.deepcopy(pet)
            (team1, team2, team2_fainted) = before_faint(team1, team2, pet, team2_fainted)
            if pet in team2:
                team2.remove(pet)
                team2_fainted.append(fainted_pet)

    return team1, team2, team1_fainted, team2_fainted


def hurt(team1, team2):
    team1_ability_copy = team1.copy()
    team2_ability_copy = team2.copy()
    ability_order = team1_ability_copy + team2_ability_copy
    ability_order.sort(key=get_pos, reverse=True)
    ability_order.sort(key=get_atk, reverse=True)

    for pet in ability_order:
        if pet.health > 0:
            if pet.health < pet.hurt:
                if pet in team1:
                    (ability_repeat, tiger_level) = tiger(pet, team1)
                else:
                    (ability_repeat, tiger_level) = tiger(pet, team2)

                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = pet.level
                    else:
                        level = tiger_level

                    if pet.name == "peacock":
                        pet.attack = pet.attack + (4 * level)
                        pet.hurt = pet.health
                    elif pet.name == "gorilla":
                        if pet.triggers > 0:
                            pet.held = "coconut"
                            if trigger == 0:
                                pet.triggers = pet.triggers - 1
                            pet.hurt = pet.health
                    else:
                        if pet in team1:
                            if pet.name == "blowfish":
                                if len(team2) > 0:
                                    attack_target = random.choice(team2)
                                    attack_target = damage(attack_target, (2 * level))
                                    pet.hurt = pet.health
                                    (team1, team2) = post_damage_checks(team1, team2)
                            if pet.name == "camel":
                                for friendly_pet in team1:
                                    if friendly_pet.pos == pet.pos + 1:
                                        friendly_pet.health = friendly_pet.health + (2 * level)
                                        friendly_pet.attack = friendly_pet.attack + (2 * level)
                        else:
                            if pet.name == "blowfish":
                                if len(team1) > 0:
                                    attack_target = random.choice(team1)
                                    attack_target = damage(attack_target, (2 * level))
                                    pet.hurt = pet.health
                                    (team1, team2) = post_damage_checks(team1, team2)
                            if pet.name == "camel":
                                for friendly_pet in team2:
                                    if friendly_pet.pos == pet.pos + 1:
                                        friendly_pet.health = friendly_pet.health + (2 * level)
                                        friendly_pet.attack = friendly_pet.attack + (2 * level)

    return team1, team2

def before_faint(team1, team2, pet, fainted):
    if pet in team1:
        (ability_repeat, tiger_level) = tiger(pet, team1)
    else:
        (ability_repeat, tiger_level) = tiger(pet, team2)

    for trigger in range(0, ability_repeat):
        if trigger == 0:
            level = pet.level
        else:
            level = tiger_level
        if pet.name == "badger":
            if pet in team1:
                if pet.pos == 0 and len(team1) <= 1: #Back
                    if len(team2) > 0:
                        team2[0] = damage(team2[0], int((pet.attack / 2) * level))
                elif pet.pos == 0 and len(team1) > 1: #Front
                    if len(team2) > 0:
                        team2[0] = damage(team2[0], int((pet.attack / 2) * level))
                    team1[1] = damage(team1[1], int((pet.attack / 2) * level))
                elif len(team1) != 0:
                    team1[pet.pos - 1] = damage(team1[pet.pos - 1], int((pet.attack / 2) * level))
                    team1[pet.pos + 1] = damage(team1[pet.pos + 1], int((pet.attack / 2) * level))
                if trigger == 0:
                    team1.remove(pet)
                    fainted.append(pet)
            else:
                if pet.pos == 0 and len(team2) <= 1:  # Back
                    if len(team1) > 0:
                        team1[0] = damage(team1[0], int((pet.attack / 2) * level))
                elif pet.pos == 0 and len(team2) > 1:  # Front
                    if len(team1) > 0:
                        team1[0] = damage(team1[0], int((pet.attack / 2) * level))
                    team2[1] = damage(team2[1], int((pet.attack / 2) * level))
                elif len(team2) != 0:
                    team2[pet.pos - 1] = damage(team2[pet.pos - 1], int((pet.attack / 2) * level))
                    team2[pet.pos + 1] = damage(team2[pet.pos + 1], int((pet.attack / 2) * level))
                if trigger == 0:
                    team2.remove(pet)
                    fainted.append(pet)
            (team1, team2) = post_damage_checks(team1, team2)
        if pet.name == "turtle":
            if pet in team1:
                turtle_counter = 1
                for melon_target in team1:
                    if (melon_target.pos == pet.pos + turtle_counter) and (turtle_counter <= level):
                        melon_target.held = "melon"
                        turtle_counter += 1
                team1.remove(pet)
                fainted.append(pet)
            else:
                turtle_counter = 1
                for melon_target in team2:
                    if (melon_target.pos == pet.pos + turtle_counter) and (turtle_counter <= level):
                        melon_target.held = "melon"
                        turtle_counter += 1
                team2.remove(pet)
                fainted.append(pet)

    return team1, team2, fainted



def faint(team1, team2, team1_fainted, team2_fainted):
    faint_order = team1_fainted + team2_fainted
    faint_order.sort(key=get_pos, reverse=True)
    faint_order.sort(key=get_atk, reverse=True)

    team1_summons = []
    team2_summons = []

    for pet in faint_order:
        if pet in team1_fainted:
            (ability_repeat, tiger_level) = tiger(pet, team1)
            for trigger in range(0, ability_repeat):
                if trigger == 0:
                    level = pet.level
                else:
                    level = tiger_level
                if pet.name == "ant":
                    if len(team1) > 0:
                        buff_target = random.choice(team1)
                        buff_target.attack = buff_target.attack + (2 * level)
                        buff_target.health = buff_target.health + (1 * level)
                if pet.name == "flamingo":
                    buff_targets = []
                    for buff_target in team1:
                        if (buff_target.pos == pet.pos + 1) or (buff_target.pos == pet.pos + 2):
                            buff_targets.append(buff_target)
                    for buff_target in buff_targets:
                        buff_target.attack = buff_target.attack + (1 * level)
                        buff_target.health = buff_target.health + (1 * level)
                if pet.name == "mammoth":
                    for other_pet in team1:
                        other_pet.health = other_pet.health + (2 * level)
                        other_pet.attack = other_pet.attack + (2 * level)
                if pet.name == "hedgehog":
                    for target in team1:
                        target = damage(target, (2 * level))
                    for target in team2:
                        target = damage(target, (2 * level))
                    (team1, team2) = post_damage_checks(team1, team2)
                if pet.name == "cricket":
                    if len(team1) < 5:
                        summon = classes.Pet("zombie_cricket", 1 * pet.level, 1 * level, level,
                                     (level / 3) + 1, pet.pos, None)
                        team1 = [summon] + team1
                        team1_summons = [summon] + team1_summons
                        team1 = sort_team(team1)
                if pet.name == "deer":
                    if len(team1) < 5:
                        summon = classes.Pet("bus", 5 * level, 5 * level, level,
                                     (level / 3) + 1, pet.pos, "chilli")
                        team1 = [summon] + team1
                        team1_summons = [summon] + team1_summons
                        team1 = sort_team(team1)
                if pet.name == "sheep":
                    for trigger in range(0, 2):
                        if len(team1) < 5:
                            summon = classes.Pet("ram", 2 * level, 2 * level, level,
                                         (level / 3) + 1, pet.pos, None)
                            team1 = [summon] + team1
                            team1_summons = [summon] + team1_summons
                            team1 = sort_team(team1)
                if pet.name == "rooster":
                    for trigger in range(0, level):
                        if len(team1) < 5:
                            if pet.attack < 2:
                                summon = classes.Pet("chick", 1, 1, level,
                                             (level / 3) + 1, pet.pos, None)
                            else:
                                summon = classes.Pet("chick", int(pet.attack / 2), 1, level,
                                             (level / 3) + 1, pet.pos, None)
                            team1 = [summon] + team1
                            team1_summons = [summon] + team1_summons
                            team1 = sort_team(team1)
                if pet.name == "spider":
                    if len(team1) < 5:
                        tier_3 = ["blowfish", "camel", "dog", "dolphin", "giraffe", "kangaroo", "ox", "rabbit", "sheep",
                                  "snail"]
                        summon = classes.Pet(random.choice(tier_3), 2, 2, level,
                                     (level / 3) + 1, pet.pos, None)
                        team1 = [summon] + team1
                        team1_summons = [summon] + team1_summons
                        team1 = sort_team(team1)
                #TIGER #WHALE LEVEL
                if pet.name == "whale":
                    if len(team1) < 5:
                        summon = pet.swallowed
                        if summon.name == "scorpion":
                            summon.held = "peanuts"
                        team1 = [summon] + team1
                        team1_summons + [summon] + team1_summons
                if pet.name == "rat":
                    for trigger in range(0, min(level, 5 - len(team2))):
                        for team2_pet in team2:
                            team2_pet.pos = team2_pet.pos + 1
                        summon = classes.Pet("dirty_rat", 1, 1, level,
                                     (level / 3) + 1, 0, None)
                        team2 = [summon] + team2
                        team2_summons = [summon] + team2_summons
                        team2 = sort_team(team2)

            # Friend Faints
            team1_ability_order = team1.copy()
            team1_ability_order.sort(key=get_pos, reverse=True)
            team1_ability_order.sort(key=get_atk, reverse=True)

            for other_pet in team1_ability_order:
                (ability_repeat, tiger_level) = tiger(other_pet, team1)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = other_pet.level
                    else:
                        level = tiger_level
                    if other_pet.name == "shark":
                        other_pet.attack = other_pet.attack + level
                        other_pet.health = other_pet.health + (2 * level)
                    if other_pet.name == "fly":
                        if pet.name != "zombie_fly":
                            if len(team1) < 5:
                                if other_pet.triggers > 0:
                                    summon = classes.Pet("zombie_fly", 4 * level, 4 * level,
                                                 level,
                                                 (level / 3) + 1, pet.pos, None)
                                    team1 = [summon] + team1
                                    team1_summons = [summon] + team1_summons
                                    team1 = sort_team(team1)
                                    if trigger == 0:
                                        other_pet.triggers = other_pet.triggers - 1
                    if other_pet.name == "ox":
                        if pet.pos == other_pet.pos - 1:
                            other_pet.attack = other_pet.attack + level
                            other_pet.held = "melon"

            # Mushroom + Honey
            if pet.held == "mushroom":
                if len(team1) < 5:
                    summon = classes.Pet(pet.name, 1, 1, level,
                                 (level / 3) + 1, pet.pos, None)
                    if summon.name == 'scorpion':
                        summon.held = "peanuts"
                    team1 = [summon] + team1
                    team1_summons = [summon] + team1_summons
                    team1 = sort_team(team1)
            elif pet.held == "honey":
                if len(team1) < 5:
                    summon = classes.Pet("bee", 1, 1, level,
                                 (level / 3) + 1, pet.pos, None)
                    team1 = [summon] + team1
                    team1_summons = [summon] + team1_summons
                    team1 = sort_team(team1)


        elif pet in team2_fainted:
            (ability_repeat, tiger_level) = tiger(pet, team2)
            for trigger in range(0, ability_repeat):
                if trigger == 0:
                    level = pet.level
                else:
                    level = tiger_level
                if pet.name == "ant":
                    if len(team2) > 0:
                        buff_target = random.choice(team2)
                        buff_target.attack = buff_target.attack + (2 * level)
                        buff_target.health = buff_target.health + (1 * level)
                if pet.name == "flamingo":
                    buff_targets = []
                    for buff_target in team2:
                        if (buff_target.pos == pet.pos + 1) or (buff_target.pos == pet.pos + 2):
                            buff_targets.append(buff_target)
                    for buff_target in buff_targets:
                        buff_target.attack = buff_target.attack + (1 * level)
                        buff_target.health = buff_target.health + (1 * level)
                if pet.name == "mammoth":
                    for other_pet in team2:
                        other_pet.health = other_pet.health + (2 * level)
                        other_pet.attack = other_pet.attack + (2 * level)
                if pet.name == "hedgehog":
                    for target in team2:
                        target = damage(target, (2 * level))
                    for target in team2:
                        target = damage(target, (2 * level))
                    (team1, team2) = post_damage_checks(team1, team2)
                if pet.name == "cricket":
                    if len(team2) < 5:
                        summon = classes.Pet("zombie_cricket", 1 * level, 1 * level, level,
                                     (level / 3) + 1, pet.pos, None)
                        team2 = [summon] + team2
                        team2_summons = [summon] + team2_summons
                        team2 = sort_team(team2)
                if pet.name == "deer":
                    if len(team2) < 5:
                        summon = classes.Pet("bus", 5 * level, 5 * level, level,
                                     (level / 3) + 1, pet.pos, "chilli")
                        team2 = [summon] + team2
                        team2_summons = [summon] + team2_summons
                        team2 = sort_team(team2)
                if pet.name == "sheep":
                    for trigger in range(0, 2):
                        if len(team2) < 5:
                            summon = classes.Pet("ram", 2 * level, 2 * level, level,
                                         (level / 3) + 1, pet.pos, None)
                            team2 = [summon] + team2
                            team2_summons = [summon] + team2_summons
                            team2 = sort_team(team2)
                if pet.name == "rooster":
                    for trigger in range(0, level):
                        if len(team2) < 5:
                            if pet.attack < 2:
                                summon = classes.Pet("chick", 1, 1, level,
                                             (level / 3) + 1, pet.pos, None)
                            else:
                                summon = classes.Pet("chick", int(pet.attack / 2), 1, level,
                                             (level / 3) + 1, pet.pos, None)
                            team2 = [summon] + team2
                            team2_summons = [summon] + team2_summons
                            team2 = sort_team(team2)
                if pet.name == "spider":
                    if len(team2) < 5:
                        tier_3 = ["blowfish", "camel", "dog", "dolphin", "giraffe", "kangaroo", "ox", "rabbit", "sheep",
                                  "snail"]
                        summon = classes.Pet(random.choice(tier_3), 2, 2, level,
                                     (level / 3) + 1, pet.pos, None)
                        team2 = [summon] + team2
                        team2_summons = [summon] + team2_summons
                        team2 = sort_team(team2)
                #TIGER #WHALE LEVEL
                if pet.name == "whale":
                    if len(team2) < 5:
                        summon = pet.swallowed
                        if summon.name == "scorpion":
                            summon.held = "peanuts"
                        team2 = [summon] + team2
                        team2_summons + [summon] + team2_summons

                if pet.name == "rat":
                    for trigger in range(0, min(level, 5 - len(team2))):
                        for team2_pet in team1:
                            team2_pet.pos = team2_pet.pos + 1
                        summon = classes.Pet("dirty_rat", 1, 1, level,
                                     (level / 3) + 1, 0, None)
                        team1 = [summon] + team1
                        team1_summons = [summon] + team1_summons
                        team1 = sort_team(team1)

            # Friend Faints
            team2_ability_order = team2.copy()
            team2_ability_order.sort(key=get_pos, reverse=True)
            team2_ability_order.sort(key=get_atk, reverse=True)

            for other_pet in team2_ability_order:
                (ability_repeat, tiger_level) = tiger(other_pet, team2)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = other_pet.level
                    else:
                        level = tiger_level
                    if other_pet.name == "shark":
                        other_pet.attack = other_pet.attack + level
                        other_pet.health = other_pet.health + (2 * level)
                    if other_pet.name == "fly":
                        if pet.name != "zombie_fly":
                            if len(team2) < 5:
                                if other_pet.triggers > 0:
                                    summon = classes.Pet("zombie_fly", 4 * level, 4 * level,
                                                 level,
                                                 (level / 3) + 1, pet.pos, None)
                                    team2 = [summon] + team2
                                    team2_summons = [summon] + team2_summons
                                    team2 = sort_team(team2)
                                    if trigger == 0:
                                        other_pet.triggers = other_pet.triggers - 1
                    if other_pet.name == "ox":
                        if pet.pos == other_pet.pos - 1:
                            other_pet.attack = other_pet.attack + level
                            other_pet.held = "melon"

            #Mushroom + Honey
            if pet.held == "mushroom":
                if len(team2) < 5:
                    summon = classes.Pet(pet.name, 1, 1, pet.level,
                                 (pet.level / 3) + 1, pet.pos, None)
                    if summon.name == 'scorpion':
                        summon.held = "peanuts"
                    team2 = [summon] + team2
                    team2_summons = [summon] + team2_summons
                    team2 = sort_team(team2)
            elif pet.held == "honey":
                if len(team2) < 5:
                    summon = classes.Pet("bee", 1, 1, pet.level,
                                 (pet.level / 3) + 1, pet.pos, None)
                    team2 = [summon] + team2
                    team2_summons = [summon] + team2_summons
                    team2 = sort_team(team2)


    # Friend Summoned
    ability_order = team1.copy() + team2.copy()
    ability_order.sort(key=get_pos, reverse=True)
    ability_order.sort(key=get_atk, reverse=True)

    for other_pet in ability_order:
        if other_pet not in team1_summons and other_pet not in team2_summons:
            if other_pet in team1:
                (ability_repeat, tiger_level) = tiger(other_pet, team1)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = other_pet.level
                    else:
                        level = tiger_level
                    if other_pet.name == "horse":
                        for summoned_pet in team1_summons:
                            summoned_pet.attack = summoned_pet.attack + 1 * level
                    elif other_pet.name == "dog":
                        for summoned_pet in team1_summons:
                            if (random.randint(0, 1)) == 0:
                                other_pet.attack = other_pet.attack + level
                            else:
                                other_pet.health = other_pet.health + level
                    elif other_pet.name == "turkey":
                        for summoned_pet in team1_summons:
                            summoned_pet.attack = summoned_pet.attack + (3 * level)
                            summoned_pet.health = summoned_pet.health + (3 * level)
            else:
                (ability_repeat, tiger_level) = tiger(other_pet, team2)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = other_pet.level
                    else:
                        level = tiger_level
                    if other_pet.name == "horse":
                        for summoned_pet in team2_summons:
                            summoned_pet.attack = summoned_pet.attack + 1 * level
                    elif other_pet.name == "dog":
                        for summoned_pet in team2_summons:
                            if (random.randint(0, 1)) == 0:
                                other_pet.attack = other_pet.attack + level
                            else:
                                other_pet.health = other_pet.health + level
                    elif other_pet.name == "turkey":
                        for summoned_pet in team2_summons:
                            summoned_pet.attack = summoned_pet.attack + (3 * level)
                            summoned_pet.health = summoned_pet.health + (3 * level)

    return team1, team2


def before_attack(team1, team2):
    if len(team1) > 0:
        team1_attack = team1[0]
    else:
        team1_attack = None

    if len(team2) > 0:
        team2_attack = team2[0]
    else:
        team2_attack = None

    if team1_attack.name == "elephant":
        (ability_repeat, tiger_level) = tiger(team1_attack, team1)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team1_attack.level
            else:
                level = tiger_level
            if (team1_attack.pos != (len(team1) - 1)):
                for trigger in range(0, level):
                    team1[team1_attack.pos + 1] = damage(team1[team1_attack.pos + 1], 1)
                    (team1, team2) = post_damage_checks(team1, team2)
    if team2_attack.name == "elephant":
        (ability_repeat, tiger_level) = tiger(team2_attack, team1)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team2_attack.level
            else:
                level = tiger_level
            if (team2_attack.pos != (len(team2) - 1)):
                for trigger in range(0, level):
                    team2[team2_attack.pos + 1] = damage(team2[team2_attack.pos + 1], 1)
                    (team1, team2) = post_damage_checks(team1, team2)

    if team1_attack.name == "boar":
        (ability_repeat, tiger_level) = tiger(team1_attack, team1)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team1_attack.level
            else:
                level = tiger_level
            team1_attack.attack = team1_attack.attack + (4 * level)
            team1_attack.health = team1_attack.health + (2 * level)
    if team2_attack.name == "boar":
        (ability_repeat, tiger_level) = tiger(team2_attack, team1)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team2_attack.level
            else:
                level = tiger_level
            team2_attack.attack = team2_attack.attack + (4 * level)
            team2_attack.health = team2_attack.health + (2 * level)

    if len(team1) > 0:
        team1_attack = team1[0]
    else:
        team1_attack = None

    if len(team2) > 0:
        team2_attack = team2[0]
    else:
        team2_attack = None
    return team1, team2, team1_attack, team2_attack


def attack(team1, team2, team1_attack, team2_attack):
    if team2_attack.held == "meat":
        team1_attack = damage(team1_attack, team2_attack.attack + 4)
    elif team2_attack.held == "steak":
        team1_attack = damage(team1_attack, team2_attack.attack + 20)
        team2_attack.held = None
    elif team2_attack.held == "peanuts":
        if team1_attack.held == "melon":
            if team2_attack.attack > 20:
                team1_attack = damage(team1_attack, 70)
            else:
                team1_attack = damage(team1_attack, team2_attack.attack)
        else:
            team1_attack = damage(team1_attack, 70)
    else:
        team1_attack = damage(team1_attack, team2_attack.attack)

    if team1_attack.held == "chilli":
        if len(team2) > 1:
            team2[1] = damage(team2[1], 5)


    if team1_attack.held == "meat":
        team2_attack = damage(team2_attack, team1_attack.attack + 4)
    elif team1_attack.held == "steak":
        team2_attack = damage(team2_attack, team1_attack.attack + 20)
        team1_attack.held = None
    elif team1_attack.held == "peanuts":
        if team2_attack.held == "melon":
            if team1_attack.attack > 20:
                team2_attack = damage(team2_attack, 70)
            else:
                team2_attack = damage(team2_attack, team1_attack.attack)
        else:
            team2_attack = damage(team2_attack, 70)
    else:
        team2_attack = damage(team2_attack, team1_attack.attack)

    if team2_attack.held == "chilli":
        if len(team1) > 1:
            team1[1] = damage(team1[1], 5)

    (team1, team2) = knockout(team1, team2, team1_attack, team2_attack)

    friend_ahead_attacks_list = []
    ability_order = team1.copy() + team2.copy()
    ability_order.sort(key=get_pos, reverse=True)
    ability_order.sort(key=get_atk, reverse=True)
    for other_pet in ability_order:
        if other_pet.pos == 1:
            if other_pet.name == "kangaroo" or other_pet.name == "snake":
                friend_ahead_attacks_list.append(other_pet)

    (team1, team2) = post_damage_checks(team1, team2)

    for pet in friend_ahead_attacks_list:
        if pet.name == "kangaroo":
            if pet in team1:
                (ability_repeat, tiger_level) = tiger(pet, team1)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = pet.level
                    else:
                        level = tiger_level
                    pet.attack = pet.attack + (2 * level)
                    pet.health = pet.health + (2 * level)
            elif pet in team2:
                (ability_repeat, tiger_level) = tiger(pet, team2)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = pet.level
                    else:
                        level = tiger_level
                    pet.attack = pet.attack + (2 * level)
                    pet.health = pet.health + (2 * level)
        if pet.name == "snake":
            if pet in team1:
                (ability_repeat, tiger_level) = tiger(pet, team1)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = pet.level
                    else:
                        level = tiger_level
                    choice = random.choice(team2)
                    choice = damage(choice, (5 * level))
                    (team1, team2) = post_damage_checks(team1, team2)
            elif pet in team2:
                (ability_repeat, tiger_level) = tiger(pet, team2)
                for trigger in range(0, ability_repeat):
                    if trigger == 0:
                        level = pet.level
                    else:
                        level = tiger_level
                    choice = random.choice(team1)
                    choice = damage(choice, (5 * level))
                    (team1, team2) = post_damage_checks(team1, team2)

    return team1, team2, team1_attack, team2_attack


def knockout(team1, team2, team1_attack, team2_attack):
    team1_copy = team1.copy()
    team2_copy = team2.copy()

    team1_fainted = []
    team2_fainted = []

    for pet in team1_copy:
        if pet.health <= 0:
            fainted_pet = copy.deepcopy(pet)
            team1_fainted.append(fainted_pet)

    for pet in team2_copy:
        if pet.health <= 0:
            fainted_pet = copy.deepcopy(pet)
            team2_fainted.append(fainted_pet)

    if team1_attack.name == "hippo" and team1_attack not in team1_fainted:
        (ability_repeat, tiger_level) = tiger(team1_attack, team1)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team1_attack.level
            else:
                level = tiger_level
            for trigger in team2_fainted:
                team1_attack.attack = team1_attack.attack + (3 * team1_attack.level)
                team1_attack.health = team1_attack.health + (3 * team1_attack.level)
    if team2_attack.name == "hippo" and team2_attack not in team2_fainted:
        (ability_repeat, tiger_level) = tiger(team2_attack, team2)
        for trigger in range(0, ability_repeat):
            if trigger == 0:
                level = team2_attack.level
            else:
                level = tiger_level
            for trigger in team1_fainted:
                team2_attack.attack = team2_attack.attack + (3 * team2_attack.level)
                team2_attack.health = team2_attack.health + (3 * team2_attack.level)

    if team1_attack.name == "rhino" and team1_attack not in team1_fainted:
        (ability_repeat, tiger_level) = tiger(team1_attack, team1)
        team1_rhino = 0
        while (team1_rhino != len(team2_fainted)):
            for trigger in range(0, (len(team2_fainted) - team1_rhino) * ability_repeat):
                if trigger < (len(team2_fainted) - team1_rhino):
                    level = team1_attack.level
                else:
                    level = tiger_level
                for pet in team2:
                    if pet.health > 0:
                        pet = damage(pet, (4 * level))
                        (team1, team2) = post_damage_checks(team1, team2)
                        break
            team1_rhino = len(team2_fainted)
            team2_fainted = []
            for pet in team2_copy:
                if pet.health <= 0:
                    fainted_pet = copy.deepcopy(pet)
                    team2_fainted.append(fainted_pet)



    if team2_attack.name == "rhino" and team2_attack not in team2_fainted:
        (ability_repeat, tiger_level) = tiger(team2_attack, team2)
        team2_rhino = 0
        while (team2_rhino != len(team1_fainted)):
            for trigger in range(0, (len(team1_fainted) - team2_rhino) * ability_repeat):
                if trigger < (len(team1_fainted) - team2_rhino):
                    level = team2_attack.level
                else:
                    level = tiger_level
                for pet in team1:
                    if pet.health > 0:
                        pet = damage(pet, (4 * level))
                        break
            team2_rhino = len(team1_fainted)
            team1_fainted = []
            for pet in team1_copy:
                if pet.health <= 0:
                    fainted_pet = copy.deepcopy(pet)
                    team1_fainted.append(fainted_pet)

        (team1, team2) = post_damage_checks(team1, team2)

    return team1, team2


def sort_team(team):
    team.sort(key=get_pos)
    i = 0
    for pet in team:
        pet.pos = i
        i += 1
    return team

def damage(pet, damage):
    if pet.held == "coconut":
        pet.held = None
    elif pet.held == "melon":
        pet.held = None
        if damage > 20:
            pet.health = pet.health - (damage - 20)
    elif pet.held == "garlic":
        pet.health = pet.health - max(1, (damage - 3))
    else:
        pet.health = pet.health - damage


    return pet

def tiger(pet, team):
    if (pet.pos < len(team) - 1 and (len(team) > 1)):
        if team[pet.pos + 1].name == "tiger":
            return 2, team[pet.pos + 1].level
    if pet.pos < len(team):
        if team[pet.pos].name == "tiger" and pet.name != "tiger":
            return 2, team[pet.pos].level
    return 1, None

def simulate_shop(team, turn, frozen_pets, frozen_food, can_count):
    import leaderboard
    gold = 10
    if frozen_pets is not None:
        pet_shop = frozen_pets
    else:
        pet_shop = []

    if frozen_food is not None:
        food_shop = frozen_food
    else:
        food_shop = []

    (team, pet_shop, food_shop) = start_of_turn(team, turn)

    end_of_turn = False
    while (end_of_turn is False):
        actions = shop.actions([pet_shop, food_shop, gold], team)
        action = random.choice(actions)

        if action[0] == "end_of_turn":
            end_of_turn = True
            team_str = ""
            team_str = team_str + str(turn) + " "
            for pet in team:
                team_str = team_str + str(pet.name) + " "
                team_str = team_str + str(pet.attack) + " "
                team_str = team_str + str(pet.health) + " "
                team_str = team_str + str(pet.level) + " "
                team_str = team_str + str(pet.exp) + " "
                team_str = team_str + str(pet.pos) + " "
                team_str = team_str + str(pet.held) + " "
            team_score = leaderboard.add_to_leaderboard(team_str)
            print(team_str, team_score)
            break
        elif action[0] == "roll":
            (team, pet_shop, food_shop, gold) = shop.simulate_action(action, team, [pet_shop, food_shop, gold])
            (pet_shop, food_shop) = roll_shop(turn)
        else:
            (team, pet_shop, food_shop, gold) = shop.simulate_action(action, team, [pet_shop, food_shop, gold])

def start_of_turn(team, turn):
    team = sort_team(team)
    for pet in team:
        if pet.name == "swan":
            gold += pet.level
    (pet_shop, food_shop) = roll_shop(turn)
    return team, pet_shop, food_shop,

def roll_shop(turn):
    tier_1_pets = [("ant", (2, 1)), ("beaver", (3, 2)), ("cricket", (1, 2)), ("duck", (2, 3)), ("fish", (2, 2)),
                   ("horse", (2, 1)), ("mosquito", (2, 2)), ("otter", (1, 2)), ("pig", (4, 1))]
    tier_1_food = ["apple", "honey"]
    tier_2_pets = [("rat", (4, 5)), ("shrimp", (2, 3)), ("hedgehog", (3, 2)), ("flamingo", (4, 2)), ("spider", (2, 2)),
                   ("swan", (1, 3)), ("peacock", (2, 5)), ("dodo", (2, 3)), ("elephant", (3, 5)), ("crab", (3, 1))]
    tier_2_food = ["pill", "cupcake", "meat"]

    if turn < 3:
        pet_space = 3
        food_space = 1
        shop_pets = tier_1_pets
        shop_food = tier_1_food
    pet_shop = []
    food_shop = []
    for space in range(0, pet_space):
        pet = random.choice(shop_pets)
        pet_shop.append(classes.ShopPet(pet[0], pet[1][0], pet[1][1]))
    for space in range(0, food_space):
        food_shop.append(random.choice(shop_food))
    return pet_shop, food_shop

