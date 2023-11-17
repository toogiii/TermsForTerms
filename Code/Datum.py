from Code.EntityNode import EntityNode

# Class representing data nodes in the graph
class Datum(EntityNode):
    def __init__(self, id, name, owners, controllers, graph, releases, rights):
        self.id = id
        self.name = name
        self.owners = owners
        self.controllers = controllers
        self.vertex = graph.add_vertex()
        self.graph = graph
        self.releases = releases
        self.rights = rights
