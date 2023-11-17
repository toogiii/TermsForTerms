from Code.DataEdge import DataEdge
from Code.EntityNode import EntityNode

# Represents Data Processor
class DataProcessor(EntityNode):
    def __init__(self, id, name, processed, processed_data, graph):
        self.id = id
        self.name = name
        self.processed = processed
        self.processed_data = processed_data
        self.vertex = graph.add_vertex()
        self.graph = graph
        self.processed_edges = ()
        self.processed_data_edges = ()
        
        for controller in self.processed:
            self.edges.add(self.graph.add_edge(self.vertex, controller.vertex))

        for datum in processed_data:
            new_edge = DataEdge(self.vertex, datum.vertex, (), datum.releases, self.graph)
            self.processed_data_edges.add(new_edge)

    def add_processed(self, controllers):
        for controller in controllers:
            if controller not in self.processed:
                self.processed.add(controller)
                self.edges.add(self.graph.add_edge(self.vertex, controller.vertex))

    def add_processed_data(self, data):
        for datum in data:
            if data not in self.processed_data:
                self.processed_data.add(datum)
                new_edge = DataEdge(self.vertex, datum.vertex, datum.rights, datum.releases, self.graph)
                self.processed_data_edges.add(new_edge)