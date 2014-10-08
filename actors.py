import random


class Actor:

    def __init__(self, x, y, director):
        self.x = x
        self.y = y
        self.director = director

###_________________________________________________________________________________________________


class Tree(Actor):

    SAPLING = 0
    TREE = 1
    ELDER_TREE = 2

    def __init__(self, x, y, director, tree_tag = 0):
        super(Tree, self).__init__(x, y, director)
        self.type = "tree"
        self.age = 0
        self.treeTag = tree_tag

    def act(self):
        self.__grow()
        self.__sprawl()

    def __grow(self):
        self.age += 1
        if self.age > 9:
            self.treeTag = self.TREE

        if self.age > 119:
            self.treeTag = self.ELDER_TREE

    def __sprawl(self):
        if self.treeTag > random.randint(10):
            neighbours = self.director.getNeighbours(self.x, self.y)
            nneighbours = [i for i in neighbours if self.director.searchPlant is False]
            self.director.generateTree((nneighbours[random.randint(0, len(nneighbours))]), 0)


#### _________________________________________________________________________________________________



class LumberJack(Actor):

    log = 0

    def __init__(self, x, y, director):
            super(LumberJack, self).__init__(x, y, director)
            self.type = "lumberjack"
            self.speed = 3

    def act(self):
        self.__search()

    def __search(self):
        i = 0
        treeFound = self.director.searchTree(self.x, self.y)
        while treeFound is False and i < self.speed:
            self.__move()
            i += 1
            treeFound = self.director.searchTree(self.x, self.y)
        self.__cut()

    def __move(self):
        self.director.getNeighbours()


###_________________________________________________________________________________________________


class Bear(Actor):

    accident = 0

    def __init__(self, x, y, director):
        super(Bear, self).__init__(x, y, director)
        self.type = "BEAR"

    def act(self):
        self.__move()

    def __move(self):
        pass