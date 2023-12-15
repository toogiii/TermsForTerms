from EntityEdge import EntityEdge

# Class representing the edge between a datum and a non-datum entity
class DataEdge(EntityEdge):
    def __init__(self, source_vertex, dest_vertex, props, dggraph):
        self.dggraph = dggraph

        # Necessary sets of properties are represented as individual sets, of which there
        #   may be many. At least one of these sets must be fully satisfied for compliance.
        self.props = props
        self.edge = self.dggraph.add_edge(self, source_vertex, dest_vertex)