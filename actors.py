import random

class Actor:

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY


###_________________________________________________________________________________________________



class Tree(Actor):


    def __init__(self):

        SAPLING = 0
        TREE = 1
        ELDER_TREE = 2

        self.type = "tree"
        self.age = 0
        self.treeTag = SAPLING

    def act(self):
        self.grow
        self.sprawl

    def __grow(self):
        self.age += 1
        if self.age > 9 and self.treeTag == self.SAPLING:
            self.treeTag = self.TREE
            self.age = 0

        if self.age > 119 and self.treeTag == self.TREE:
            self.treeTag = self.ELDER_TREE
            self.age = 0

    def __sprawl(self):
        if (self.treeTag * 10) > random.randint(0, 100):
            pass # sceglie una casella libera accanto a se e pianta un germoglio

###_________________________________________________________________________________________________



class LumberJack(Actor):

    log = 0

    def __init__(self):
            self.type = "LUMBERJACK"

    def act(self):
        self.move

    def __move(self):
        pass


###_________________________________________________________________________________________________



class Bear(Actor):

    accident = 0

    def __init__(self):
        self.type = "BEAR"

    def act(self):
        self.move

    def __move(self):
        pass