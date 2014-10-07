import map,cell,actors

class gameDirector:
    def __init__(self, map):
        self.map = map
        self.actors = []
        self.lumberjacks = []
        self.trees = []
        self.bears = []