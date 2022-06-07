from random import random, randint
from Draw import Draw
from math import exp


class DrawGraph:
    # data structure that stores point coordinates
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return str(self.x) + ' ' + str(self.y)

    def __init__(self, n_, edges_, param=1000):
        # number of iterations of build function, more param, better quality
        self.param = param
        # number of nodes in graph
        self.num_of_nodes = n_
        # number of edges in graph
        self.m = len(edges_)
        nodes_ = [i for i in range(self.num_of_nodes + 1)]
        for i in range(1, self.num_of_nodes + 1):
            nodes_[i] = self.Point(random(), random())

        # array of points
        self.nodes = nodes_
        # array of edges (number_of_first_point, number_of_second_point)
        self.edges = edges_
        # graph - adjacency list
        self.graph = [[] for i in range(self.num_of_nodes + 1)]

        for x, y in edges_:
            self.graph[x].append(y)
            self.graph[y].append(x)

        # each node has number of intersections of its edges
        self.intersection_vals = [0 for i in range(self.num_of_nodes + 1)]
        # each node has average sine of its edges
        self.angle_vals = [0 for i in range(self.num_of_nodes + 1)]
        # each node has average length of ints edges
        self.length_vals = [0 for i in range(self.num_of_nodes + 1)]

        # creating graph
        self.build_graph()
        self.draw_graph()
        print(self.intersection_vals)
        print(self.angle_vals)

    def build_graph(self):
        # calculating number of intersections and average sine of every node
        intersections, angle = self.count_each_val()
        # calculating the value
        best_ans = intersections - angle / 4
        # annealing
        t = 1
        for i in range(self.param):
            t *= 0.99
            a, x, y = randint(1, self.num_of_nodes), random(), random()
            old = self.nodes[a]
            self.nodes[a] = self.Point(x, y)

            intersections, angle = self.count_each_val()
            value = intersections - angle / 4

            if value < best_ans or random() < exp((best_ans - value) / t):
                best_ans = value
                self.intersection_vals[a] = intersections
                self.angle_vals[a] = angle
            else:
                self.nodes[a] = old

        print(best_ans)

    def draw_graph(self):
        d = Draw(self.nodes, self.edges)
        d.draw()

    def area_of_triangle(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) + 0

    def intersect(self, a, b, c, d):
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c

        return max(a, c) <= min(b, d)

    def len_of_segment(self, a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def sin_of_two_segments(self, a, b, c, d):
        if str(a) == str(c):
            c = d
        elif str(b) == str(c):
            a, b, c = b, a, d
        elif str(b) == str(d):
            a, b = b, a

        square = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        sine = square / self.len_of_segment(a, b) / self.len_of_segment(a, c)

        return abs(sine)

    def count_single_intersection(self, a, b, c, d):
        if str(a) == str(c) or str(a) == str(d) or str(b) == str(c) or str(b) == str(d):
            return False
        return \
            self.intersect(a.x, b.x, c.x, d.x) \
            and self.intersect(a.y, b.y, c.y, d.y) \
            and self.area_of_triangle(a, b, c) * self.area_of_triangle(a, b, d) <= 0 \
            and self.area_of_triangle(c, d, a) * self.area_of_triangle(c, d, b) <= 0

    def count_each_val(self):
        for node in range(1, self.num_of_nodes + 1):
            cnt_intersections = 0
            cnt_angle = 0
            num_of_angles = 0
            for edge_node in self.graph[node]:

                for edge1, edge2 in self.edges:
                    seg1 = sorted([{float(i) for i in str(self.nodes[node]).split()},
                                   {float(i) for i in str(self.nodes[edge_node]).split()}])
                    seg2 = sorted([{float(i) for i in str(self.nodes[edge1]).split()},
                                   {float(i) for i in str(self.nodes[edge2]).split()}])

                    if seg1 == seg2:
                        continue

                    elif seg1[0] in seg2 or seg1[1] in seg2 or seg2[0] in seg1 or seg2[1] in seg1:
                        num_of_angles += 1
                        cnt_angle += self.sin_of_two_segments(
                            self.nodes[node],
                            self.nodes[edge_node],
                            self.nodes[edge1],
                            self.nodes[edge2]
                        )
                    else:
                        cnt_intersections += self.count_single_intersection(
                            self.nodes[node],
                            self.nodes[edge_node],
                            self.nodes[edge1],
                            self.nodes[edge2],
                        )

            self.intersection_vals[node] = cnt_intersections
            self.angle_vals[node] = cnt_angle / num_of_angles

        return sum(self.intersection_vals), \
            sum(self.angle_vals)

    def count_for_one(self, node):
        cnt_intersections = 0
        cnt_angle = 0
        num_of_angles = 0
        for edge_node in self.graph[node]:

            for edge1, edge2 in self.edges:
                seg1 = sorted([{float(i) for i in str(self.nodes[node]).split()},
                               {float(i) for i in str(self.nodes[edge_node]).split()}])
                seg2 = sorted([{float(i) for i in str(self.nodes[edge1]).split()},
                               {float(i) for i in str(self.nodes[edge2]).split()}])

                if seg1[0] in seg2 and seg1[1] in seg2:
                    continue

                elif seg1[0] in seg2 or seg1[1] in seg2:
                    num_of_angles += 1
                    cnt_angle += self.sin_of_two_segments(
                        self.nodes[node],
                        self.nodes[edge_node],
                        self.nodes[edge1],
                        self.nodes[edge2]
                    )
                else:
                    cnt_intersections += self.count_single_intersection(
                        self.nodes[node],
                        self.nodes[edge_node],
                        self.nodes[edge1],
                        self.nodes[edge2],
                    )

        return self.intersection_vals[node] - cnt_intersections, \
            self.angle_vals[node] - cnt_angle / num_of_angles
