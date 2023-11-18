from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Processor
class DataProcessor(EntityNode):
    def __init__(self, name, processed, processed_data, dggraph):
        self.name = name
        self.processed = processed
        self.processed_data = processed_data
        self.dggraph = dggraph

        self.vertex = dggraph.graph.add_vertex()
        self.dggraph.node_names[self.vertex] = name
        self.dggraph.nodes[self.name] = self
        
        self.processed_edges = set()
        self.processed_data_edges = set()
        
        for controller in self.processed:
            self.processed_edges.add(self.dggraph.graph.add_edge(self.vertex, controller.vertex))

        for datum in processed_data:
            new_edge = DataEdge(self.vertex, datum.vertex, set(), datum.releases, self.dggraph)
            self.processed_data_edges.add(new_edge)

    def add_processed(self, controllers):
        for controller in controllers:
            if controller not in self.processed:
                self.processed.add(controller)
                self.processed_edges.add(self.dggraph.graph.add_edge(controller.vertex, self.vertex))

    def add_processed_data(self, data):
        for datum in data:
            if data not in self.processed_data:
                self.processed_data.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.dggraph)
                self.processed_data_edges.add(new_edge)