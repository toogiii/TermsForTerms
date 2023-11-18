from graph_tool.all import *

# Represents data governance graph
class DGGraph:
    def __init__(self, name, purpose):
        self.graph = Graph()
        self.name = name
        self.purpose = purpose

        self.node_names = self.graph.new_vp("string")
        self.edge_rights = self.graph.new_ep("vector<string>")
        self.edge_releases = self.graph.new_ep("vector<string>")

        self.graph.vertex_properties["node names"] = self.node_names
        self.graph.edge_properties["edge rights"] = self.edge_rights
        self.graph.edge_properties["edge releases"] = self.edge_releases

    def render_graph(self):
        graph_draw(self.graph, 
                   vertex_text = self.graph.vertex_properties["node names"])