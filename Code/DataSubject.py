from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Subject
# Here, a Data Subject is an entity who owns data that is collected for some purpose
class DataSubject(EntityNode):
    def __init__(self, name, dggraph):
        # Name, graph, vertex instantiation
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self)

        self.other_entity = set()
        self.other_entity_edges = set()
        self.owned = set()
        self.owned_edges = set()

    # Add data that the subject owns
    def add_owned(self, datum):
        if datum in self.owned:
            raise Exception("Duplicate datum.")
        
        # Rights represent users rights over their data as specified in a given document
        datum_edge = DataEdge(self.vertex, datum.vertex, datum.s_props, self.dggraph)
        self.owned.add(datum)
        self.owned_edges.add(datum_edge)
        return datum_edge