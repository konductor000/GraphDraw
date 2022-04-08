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

        self.edges = edges_
        self.g = [[] for i in range(self.n + 1)]

        for x, y in edges_:
            self.g[x].append(y)
            self.g[y].append(x)

    def area(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

    def intersect(self, a, b, c, d):
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return max(a, c) <= min(b, d)

    def count_single(self, a, b, c, d):
        if a.x == c.x and a.y == c.y and (b.x != d.x or b.y != d.y) \
                or a.x == d.x and a.y == d.y and (b.x != c.x or b.y != c.y) \
                or b.x == c.x and b.y == c.y and (a.x != d.x or a.y != d.y) \
                or b.x == d.x and b.y == d.y and (a.x != c.x or a.y != c.y):
            return False

        return \
            self.intersect(a.x, b.x, c.x, d.x) \
            and self.intersect(a.y, b.y, c.y, d.y) \
            and self.area(a, b, c) * self.area(a, b, d) <= 0 \
            and self.area(c, d, a) * self.area(c, d, b) <= 0

    def count_each(self):
        cnt = 0
        for i in range(len(self.edges)):
            for j in range(i + 1, len(self.edges)):
                pass
                cnt += self.count_single(
                    self.nodes[self.edges[i][0]],
                    self.nodes[self.edges[i][1]],
                    self.nodes[self.edges[j][0]],
                    self.nodes[self.edges[j][1]]
                )
        return cnt



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

g = Build(n, edges)

print(g.count_each())

for i in range(1, n + 1):
    print(g.nodes[i].x, g.nodes[i].y)