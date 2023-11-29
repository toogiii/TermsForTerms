from DataEdge import DataEdge
from EntityNode import EntityNode

# Represents Data Processor
# Here, a Data Processor represents a body given data by a controller to process over that it
#   does not collect.
class DataProcessor(EntityNode):
    def __init__(self, name, dggraph):
        # Name, graph, and instantiate node
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self)

        self.other_entity = set()
        self.other_entity_edges = set()
        self.controllers = set()
        self.controllers_edges = set()
        self.processed = set()
        self.processed_edges = set()

    # Add companion controller
    def add_controller(self, controller):
        # Have controller node add processor edge, then add controller.
        if controller in self.controllers:
            return
        controllers_edge = controller.add_controlled_processor(self)
        self.controllers.add(controller)
        self.controllers_edges.add(controllers_edge)
        
    # Add data this entity processes
    def add_processed(self, datum):
        if datum in self.processed:
            raise Exception("Duplicate datum.")
        
        # Create edge with p_releases, which represents conditions/responsibilities on processing
        datum_edge = DataEdge(self.vertex, datum.vertex, datum.p_props, self.dggraph)
        self.processed.add(datum)
        self.processed_edges.add(datum_edge)
        return datum_edge