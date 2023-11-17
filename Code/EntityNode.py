from graph_tool.all import *

# Class representing entities governing data in the graph
class EntityNode:
    def __init__(self, id, name, graph):
        self.id = id
        self.name = name
        self.vertex = graph.add_vertex()
        self.graph = graph