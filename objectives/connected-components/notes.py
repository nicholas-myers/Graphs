# a set of nodes connects to one another
# for each component
# is it connected to another component
# keep track of visited
# do a search

# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("nonexistant vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

def island_counter(bin_arr):
    for arr in bin_arr:
        for i in arr:
            print(i)

island_counter(islands) # returns 4