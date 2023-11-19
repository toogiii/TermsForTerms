from graph_tool.all import *

class EntityEdge:
    def __init__(self, source_vertex, dest_vertex, props, dggraph):
        self.dggraph = dggraph
        self.edge = self.dggraph.add_edge(source_vertex, dest_vertex, props)

        # Properties may be either rights of owners or conditions on controlling/processing.
        self.props = props