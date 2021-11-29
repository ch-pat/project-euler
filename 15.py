"""Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# 1x1 grid -> 2 routes
# 2x2 grid -> 6 routes
# 3x3 grid -> 20 routes
# 4x4 grid -> 70 routes
# nxn grid -> 

class Graph():
    def __init__(self, size: int):
        self.vertices = (size + 1) ** 2
        self.nodes = [[i + (size + 1) * j for i in range(size + 1)] for j in range(size + 1)]
        self.adjacents = {}
        for i in range(self.vertices):
            self.adjacents[i] = []
            if not i % (size + 1) == size:
                self.adjacents[i] += [i + 1]
            if i + size + 1 < self.vertices:
                self.adjacents[i] += [i + size + 1]

    def calculate_paths(self):
        start = 0
        end = self.vertices - 1
        paths = 0
        stack = [start]
        while stack:
            current = stack.pop()
            if current == end:
                paths += 1
            else:
                for neighbour in self.adjacents[current]:
                    stack.append(neighbour)
        return paths


def choose(n, k):
    from math import factorial
    return  factorial(n) / (factorial(k) * factorial(n - k))


print(choose(2*20, 20))

g = Graph(5)
print(g.nodes)
print(g.adjacents)
print(g.calculate_paths())