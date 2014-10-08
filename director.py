import actors

class Director:

    def __init__(self, forest):
        self.forest = forest
        self.actors = []
        self.lumberjacks = []
        self.trees = []
        self.bears = []

    def generateBear(self, cell):
        cell.append(actors.Bear(cell.x, cell.y, self))

    def generateTree(self, cell, tag):
        cell.append(actors.Tree(cell.x, cell.y, self, tag))

    def generateLumberjack(self, cell):
        cell.append(actors.LumberJack(cell.x, cell.y, self))


    def searchTree(self, x, y):
        pass

    def searchPlant(self, cell):
        pass


    def getNeighbours(self, x, y):
        lx = max(0, x - 1)
        hx = min(self.forest.X - 1, x + 1)
        ly = max(0, y - 1)
        hy = min(self.forest.Y - 1, y + 1)

        neighbour = []
        for i in xrange(lx, hx):
            for j in xrange(ly, hy):
                if i != x or j != y:
                    neighbour.append(self.forest.dList[(i, j)])
        return neighbour

