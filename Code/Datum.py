from EntityNode import EntityNode

# Class representing data nodes in the graph
class Datum(EntityNode):
    def __init__(self, name, owners, controllers, dggraph, releases, rights):
        self.name = name
        self.owners = owners
        self.controllers = controllers
        self.releases = releases
        self.rights = rights
        self.dggraph = dggraph

        self.vertex = dggraph.graph.add_vertex()
        self.dggraph.node_names[self.vertex] = name
        self.dggraph.nodes[name] = self

        for owner in owners:
            owner.add_owned({self})
        for controller in controllers:
            controller.add_controlled({self})