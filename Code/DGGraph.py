from graph_tool.all import *
# Represents data governance graph
class DGGraph:
    def __init__(self, name, purpose):
        self.graph = Graph()
        self.name = name
        self.purpose = purpose

    def render_graph(self):
        graph_draw(self.graph)