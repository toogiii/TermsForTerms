from Code.DataEdge import DataEdge
from Code.EntityNode import EntityNode

# Represents Data Subject
class DataSubject(EntityNode):
    def __init__(self, id, name, owned, graph):
        self.id = id
        self.name = name
        self.owned = owned
        self.vertex = graph.add_vertex()
        self.graph = graph
        self.owned_edges = ()

        for datum in owned:
            new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.graph)
            self.owned_edges.add(new_edge)

    def add_owned(self, data):
        for datum in data:
            if data not in self.owned:
                self.owned.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.graph)
                self.owned_edges.add(new_edge)