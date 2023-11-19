from DataEdge import DataEdge
from PCEdge import PCEdge
from EntityNode import EntityNode

# Represents Data Controller
class DataController(EntityNode):
    def __init__(self, name, dggraph):
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self.name)

        self.controlled = set()
        self.controlled_edges = set()

    def add_controlled_data(self, datum):
        if datum in self.controlled:
            raise Exception("Duplicate datum.")
        
        c_releases = list(datum.c_releases).insert(0, "Controls")
        datum_edge = DataEdge(self.vertex, datum.vertex, c_releases, self.dggraph)
        self.controlled.add(datum)
        self.controlled_edges.add(datum_edge)
        return datum_edge

    def add_controlled_processor(self, processor):
        if processor in self.controlled:
            raise Exception("Duplicate processor.")
        
        processor_edge = PCEdge(self.vertex, processor.vertex, ["Sends data to"], self.dggraph)
        self.controlled.add(processor)
        self.controlled_edges.add(processor_edge)
        return processor_edge