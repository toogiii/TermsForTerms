from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Subject
class DataSubject(EntityNode):
    def __init__(self, name, owned, dggraph):
        self.name = name
        self.owned = owned
        self.dggraph = dggraph

        self.vertex = dggraph.graph.add_vertex()
        self.dggraph.node_names[self.vertex] = name
        self.dggraph.nodes[self.name] = self

        self.owned_edges = set()

        for datum in owned:
            new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.dggraph)
            self.owned_edges.add(new_edge)

    def add_owned(self, data):
        for datum in data:
            if datum not in self.owned:
                self.owned.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.dggraph)
                self.owned_edges.add(new_edge)