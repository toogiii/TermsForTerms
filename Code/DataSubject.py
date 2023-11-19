from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Subject
class DataSubject(EntityNode):
    def __init__(self, name, dggraph):
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self.name)

        self.owned = set()
        self.owned_edges = set()

    def add_owned(self, datum):
        if datum in self.owned:
            raise Exception("Duplicate datum.")
        
        rights = list(datum.rights).insert(0, "Owns")
        datum_edge = DataEdge(self.vertex, datum.vertex, rights, self.dggraph)
        self.owned.add(datum)
        self.owned_edges.add(datum_edge)
        return datum_edge