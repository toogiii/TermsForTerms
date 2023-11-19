from graph_tool.all import *
from EntityEdge import EntityEdge

# Class representing an edge between a processor and controller.
# Note that there is no specification for a SC edge (or subject-controller), as
#   we assume that there should be no exchanging of responsibilities between these
#   two entities. (If there is, in the case of something like MPC, we consider this
#   to be a new processor rather than a direct subject-controller interaction.)
class PCEdge(EntityEdge):
    def __init__(self, source_vertex, dest_vertex, props, dggraph):
        self.dggraph = dggraph
        self.edge = self.dggraph.add_edge(source_vertex, dest_vertex, props)

        # Properties may be either rights of owners or conditions on controlling/processing.
        self.props = props