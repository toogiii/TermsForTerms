from graph_tool.all import *

# Abstract class representing entities governing data in the graph
class EntityNode:
    def __init__(self, name, dggraph):
        # Name, graph, and vertex instantiation
        self.name = name
        self.dggraph = dggraph
        self.dggraph.add_node(self.name)