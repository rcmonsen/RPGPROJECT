#Robert Monsen
#Character file for RPG game
#CIT144

class character(object):
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

        self.dead = False

    def attack(self, other):
        pass

    def update(self):
        if self.hp < 0:
            self.dead = True
            
