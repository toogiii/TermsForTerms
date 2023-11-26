from graph_tool.all import *
from EntityEdge import EntityEdge

# Class representing the edge between a datum and a non-datum entity
class DataEdge(EntityEdge):
    def __init__(self, source_vertex, dest_vertex, props, dggraph):
        self.dggraph = dggraph

        # Properties may be either necessary (superset) or one-of (subset).
        self.props = props
        self.edge = self.dggraph.add_edge(self, source_vertex, dest_vertex)