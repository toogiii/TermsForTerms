from graph_tool.all import *

# Represents data governance graph
class DGGraph:
    def __init__(self, name, purpose):
        self.graph = Graph()
        self.name = name
        self.purpose = purpose

        self.node_names = self.graph.new_vp("string")
        self.edge_props = self.graph.new_ep("string")

        self.graph.vertex_properties["node names"] = self.node_names
        self.graph.edge_properties["edge properties"] = self.edge_props

    def add_node(self, name):
        vertex = self.graph.add_vertex()
        self.node_names[vertex] = name
        return vertex

    def add_edge(self, source_entity, dest_entity, edge_props):
        edge = self.graph.add_edge(source_entity.vertex, dest_entity.vertex)
        self.edge_props[edge] = " ".join(edge_props)
        return edge

    def render_graph(self):
        graph_draw(self.graph, 
                   vertex_text = self.graph.vertex_properties["node names"],
                   edge_text = self.graph.edge_properties["edge_props"])