from Code.DataEdge import DataEdge
from Code.EntityNode import EntityNode

# Represents Data Controller
class DataController(EntityNode):
    def __init__(self, id, name, controlled, graph):
        self.id = id
        self.name = name
        self.controlled = controlled
        self.vertex = graph.add_vertex()
        self.graph = graph
        self.controlled_edges = ()

        for datum in controlled:
            new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.graph)
            self.controlled_edges.add(new_edge)

    def add_controlled(self, data):
        for datum in data:
            if datum not in self.controlled:
                self.controlled.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.graph)
                self.controlled_edges.add(new_edge)


