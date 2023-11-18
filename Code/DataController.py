from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Controller
class DataController(EntityNode):
    def __init__(self, name, controlled, dggraph):
        self.name = name
        self.controlled = controlled
        self.dggraph = dggraph

        self.vertex = dggraph.graph.add_vertex()
        self.dggraph.node_names[self.vertex] = name
        self.dggraph.nodes[self.name] = self
        
        self.controlled_edges = set()

        for datum in controlled:
            new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.dggraph)
            self.controlled_edges.add(new_edge)

    def add_controlled(self, data):
        for datum in data:
            if datum not in self.controlled:
                self.controlled.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.dggraph)
                self.controlled_edges.add(new_edge)