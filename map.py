import pygame,math,cell


class Map:

    X = 0
    Y = 0

    def __init__(self, x=10, y=10):
        self.X = x
        self.Y = y
        self.dList = []
        for i in xrange():
            self.dlist.append(cell.Cell())


    def __getitem__(self, (x, y)):
        return self.dList[(y * self.X) + x]

    def __setitem__(self, (x, y), value):
        self.dList[(y * self.X) + x] = value