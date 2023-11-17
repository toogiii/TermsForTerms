from graph_tool.all import *

class DataEdge:
    def __init__(self, source, dest, rights, releases, graph):
        self.edge = graph.add_edge(source, dest)
        self.rights = rights
        self.releases = releases
        self.graph = graph
