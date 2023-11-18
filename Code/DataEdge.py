from graph_tool.all import *

class DataEdge:
    def __init__(self, source, dest, rights, releases, dggraph):
        self.edge = dggraph.graph.add_edge(source, dest)
        self.rights = rights
        self.releases = releases
        dggraph.edge_rights[self.edge] = rights
        dggraph.edge_releases[self.edge] = releases
        self.dggraph = dggraph