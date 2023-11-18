from graph_tool.all import *

# Class representing entities governing data in the graph
class EntityNode:
    def __init__(self, name, dggraph):
        self.name = name
        self.vertex = dggraph.graph.add_vertex()
        self.dggraph = dggraph

        self.dggraph.node_names[self.vertex] = name
        self.dggraph.nodes[name] = self