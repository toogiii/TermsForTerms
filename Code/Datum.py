from EntityNode import EntityNode

# Class representing data nodes in the graph
class Datum(EntityNode):
    def __init__(self, name, dggraph):
        self.name = name
        self.dggraph = dggraph
        self.vertex = self.dggraph.add_node(self.name)

        self.rights = set()
        self.c_releases = set()
        self.p_releases = set()

        self.owners = set()
        self.owner_edges = set()

        self.controllers = set()
        self.controller_edges = set()

        self.processors = set()
        self.processor_edges = set()

    def add_rights(self, rights):
        self.rights.union(rights)

    def add_c_releases(self, c_releases):
        self.c_releases.union(c_releases)
    
    def add_p_releases(self, p_releases):
        self.p_releases.union(p_releases)

    def add_owner(self, owner):
        new_edge = owner.add_owned(self)
        self.owners.add(owner)
        self.owner_edges.add(new_edge)

    def add_controller(self, controller):
        new_edge = controller.add_controlled(self)
        self.controllers.add(controller)
        self.controller_edges.add(new_edge)

    def add_processor(self, processor):
        new_edge = processor.add_processed(self)
        self.processors.add(processor)
        self.processor_edges.add(new_edge)