class Pet:
    def __init__(self, name, attack, health, level, exp, pos, held):
        self.name = name
        self.health = health
        self.attack = attack
        self.level = level
        self.exp = exp
        self.held = held
        self.pos = pos
        self.hurt = health
        self.swallowed = None
        if name == "gorilla":
            self.triggers = level
        elif name == "fly":
            self.triggers = 3
        else:
            self.triggers = None

class ShopPet:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
        self.frozen = None

class Tree:
    def __init__(self, action, score):
        self.action = action
        self.score = score
        self.children = []

    def addChild(self, tree):
        self.children.append(tree)

    def __str__(self, level=0):
        if self.action != None:
            if self.action[0] == "buy_food":
                ret = "\t" * level + self.action[0] + " " + self.action[1] + " " + str(self.score) + "\n"
            else:
                ret = "\t" * level + self.action[0] + " " + self.action[1].name + " " + str(self.score) + "\n"
        else:
            ret = "\t" * level + str(self.action) + " " + str(self.score) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret