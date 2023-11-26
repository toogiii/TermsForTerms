from DataEdge import DataEdge
from PCEdge import PCEdge
from EntityNode import EntityNode

# Represents Data Controller
# A data controller, here, represents a non-subject entity that uses data for a purpose
class DataController(EntityNode):
    def __init__(self, name, dggraph):
        # Add name, graph, and instantiate node
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self)
        
        self.other_entity = set()
        self.other_entity_edges = set()
        self.controlled = set()
        self.controlled_edges = set()

    # Add data that this body controls.
    def add_controlled_datum(self, datum):
        if datum in self.controlled:
            raise Exception("Duplicate datum.")
        
        # Create edge with text in c_releases and add
        datum_edge = DataEdge(self.vertex, datum.vertex, datum.c_props, self.dggraph)
        self.controlled.add(datum)
        self.controlled_edges.add(datum_edge)
        return datum_edge

    # Add processors that this controller delegates processing duties to
    def add_controlled_processor(self, processor):
        if processor in self.controlled:
            raise Exception("Duplicate processor.")
        
        # Create edge with companion processor
        processor_edge = PCEdge(self.vertex, processor.vertex, [{"contract"}], self.dggraph)
        self.controlled.add(processor)
        self.controlled_edges.add(processor_edge)
        return processor_edge