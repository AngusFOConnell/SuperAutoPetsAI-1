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