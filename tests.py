from DrawGraph import DrawGraph
from random import randint


def test1():
    n = 6
    edges = [
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 4), (3, 5), (3, 6), (5, 6)
    ]
    DrawGraph(n, edges)


def test2():
    n = 11
    edges = [
        (1, 4), (1, 8), (1, 11), (2, 3), (2, 4),
        (3, 4), (3, 5), (4, 5), (4, 7),
        (5, 6), (6, 7), (6, 9), (7, 8), (7, 9),
        (8, 9), (8, 11), (9, 10), (10, 11),
    ]
    DrawGraph(n, edges)


def test3():
    def tree(edges, v, p, n):
        if v > n:
            return
        if p != -1:
            edges.append((p, v))

        tree(edges, v * 2, v, n)
        tree(edges, v * 2 + 1, v, n)

    n = 25
    edges = []

    tree(edges, 1, -1, n)

    DrawGraph(n, edges)


def test4():
    n = 20
    edges = []

    for i in range(1, n + 1):
        b = i + 1
        while b <= n + 1:
            b = randint(b, n + 1)
            edges.append((i, b))
            b += 1

    DrawGraph(n + 1, edges)

    print(edges)


test1()
test2()
test3()
test4()
