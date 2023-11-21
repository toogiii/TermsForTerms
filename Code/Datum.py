from EntityNode import EntityNode

# Class representing data nodes in the graph
class Datum(EntityNode):
    def __init__(self, name, dggraph):
        # Name, graph, vertex instantiation
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self.name, type(self))

        # User rights and conditions on controlling and processing
        self.rights = set()
        self.c_releases = set()
        self.p_releases = set()

        self.owners = set()
        self.owner_edges = set()

        self.controllers = set()
        self.controller_edges = set()

        self.processors = set()
        self.processor_edges = set()

    # Add user rights over data to the data
    def add_rights(self, rights):
        self.rights = self.rights.union(rights)

    # Add controller conditions over data
    def add_c_releases(self, c_releases):
        self.c_releases = self.c_releases.union(c_releases)
    
    # Add processor conditions over data
    def add_p_releases(self, p_releases):
        self.p_releases = self.p_releases.union(p_releases)

    # Assign existing owner to data
    def add_owner(self, owner):
        new_edge = owner.add_owned(self)
        self.owners.add(owner)
        self.owner_edges.add(new_edge)

    # Assign controller to data
    def add_controller(self, controller):
        new_edge = controller.add_controlled_datum(self)
        self.controllers.add(controller)
        self.controller_edges.add(new_edge)

    # Assign processor to data
    def add_processor(self, processor):
        new_edge = processor.add_processed(self)
        self.processors.add(processor)
        self.processor_edges.add(new_edge)