from EntityNode import EntityNode
from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor

# Class representing data nodes in the graph
class Datum(EntityNode):
    def __init__(self, name, dggraph):
        # Name, graph, vertex instantiation
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self)

        # User rights and conditions on controlling and processing
        self.s_props = set()
        self.c_props = set()
        self.p_props = set()

        self.owners = set()
        self.owner_edges = set()

        self.controllers = set()
        self.controller_edges = set()

        self.processors = set()
        self.processor_edges = set()

        self.other_entity = set()
        self.other_entity_edges = set()

    # Add subject properties to the data
    def add_s_props(self, props):
        self.s_props = self.s_props.union(props)

    # Add controller properties to the data
    def add_c_props(self, props):
        self.c_props = self.c_props.union(props)

    # Add processor properties to the data
    def add_p_props(self, props):
        self.p_props = self.p_props.union(props)
    
    # Assign existing owner to data
    def add_owner(self, owner):
        if owner in self.owners:
            return
        new_edge = owner.add_owned(self)
        self.owners.add(owner)
        self.owner_edges.add(new_edge)

    # Assign controller to data
    def add_controller(self, controller):
        if controller in self.controllers:
            return
        new_edge = controller.add_controlled_datum(self)
        self.controllers.add(controller)
        self.controller_edges.add(new_edge)

    # Assign processor to data
    def add_processor(self, processor):
        if processor in self.processors:
            return
        new_edge = processor.add_processed(self)
        self.processors.add(processor)
        self.processor_edges.add(new_edge)