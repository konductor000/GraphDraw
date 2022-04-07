from random import random, randint


class Build:

    class Pt:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self, n_, edges_):
        self.n = n_
        self.m = len(edges_)
        nodes_ = [i for i in range(self.n + 1)]

        for i in range(1, self.n + 1):
            nodes_[i] = self.Pt(random(), random())

        self.nodes = nodes_

    def count_each(self):
        


n = 6
edges = [
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (2, 4),
    (3, 5),
    (3, 6),
    (5, 6)
]
