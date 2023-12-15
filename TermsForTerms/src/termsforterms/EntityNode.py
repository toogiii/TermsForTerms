from .EntityEdge import EntityEdge

# Abstract class representing entities governing data in the graph
class EntityNode:
    def __init__(self, name, dggraph):
        # Name, graph, and vertex instantiation
        self.name = name
        self.dggraph = dggraph
        self.other_entity = set()
        self.other_entity_edges = set()
        self.vertex = self.dggraph.add_node(self)

    def connect(self, other_ent, props):
        if other_ent in self.other_entity:
            raise Exception("Duplicate edge.")
        
        edge = EntityEdge(self.vertex, other_ent.vertex, props, self.dggraph)
        self.other_entity.add(other_ent)
        self.other_entity_edges.add(edge)
        other_ent.other_entity.add(self)
        other_ent.other_entity.add(edge)