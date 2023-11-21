from graph_tool.all import *
from DataSubject import DataSubject
from Datum import Datum

# Represents data governance graph
class DGGraph:
    def __init__(self, name, purpose):
        # Graph metadata
        self.graph = Graph()
        self.name = name
        self.purpose = purpose

        # For display: node names and properties that run along ownership/controllership/processorship edges
        self.node_names = self.graph.new_vp("string")
        self.node_rvals = self.graph.new_vp("int16_t")
        self.edge_props = self.graph.new_ep("vector<string>")
        self.edge_strings = self.graph.new_ep("string")

        self.graph.vertex_properties["node names"] = self.node_names
        self.graph.vertex_properties["node rvals"] = self.node_rvals
        self.graph.edge_properties["edge properties"] = self.edge_props
        self.graph.edge_properties["edge strings"] = self.edge_strings

    # Add node to graph with unique vertex
    def add_node(self, name, entity_type):
        vertex = self.graph.add_vertex()
        self.node_names[vertex] = name
        if entity_type == DataSubject:
            self.node_rvals[vertex] = 0
        elif entity_type == Datum:
            self.node_rvals[vertex] = 1
        else:
            self.node_rvals[vertex] = 2
        return vertex

    # Add edge between entity nodes
    def add_edge(self, source_vertex, dest_vertex, this_edge_props):
        edge = self.graph.add_edge(source_vertex, dest_vertex)
        self.edge_props[edge] = this_edge_props
        return edge

    # Draw graph
    def render_graph(self, 
                     output_size = None,
                     r = 0.01,
                     C = 100,
                     vertex_size = 30,
                     vertex_font_size = 12,
                     edge_font_size = 12,
                     filepath = None):
        edge_groups = {}
        property_number = 0

        # Get properties
        for edge in self.graph.edges():
            prop_string = ", ".join(self.edge_props[edge])
            if prop_string in edge_groups.values():
                prop_val = 0
                for key, value in edge_groups.items():
                    if value == prop_string:
                        prop_val = key
                        break
                self.edge_strings[edge] = "Property " + str(prop_val)
            else:
                property_number += 1
                edge_groups[property_number] = prop_string
                self.edge_strings[edge] = "Property " + str(property_number)

        # Write legend file
        legend_filename = self.name + "_legend.txt"
        if filepath != None:
            legend_filename = filepath[:filepath.rfind(".")] + "_legend.txt"
        with open(legend_filename, "w") as file:
            for key in edge_groups.keys():
                text = "Property " + str(key) + ": " + edge_groups[key] + "\n"
                file.write(text)
            file.close()

        # Get layout and write graph
        position = sfdp_layout(self.graph,
                               r = r,
                               C = C,
                               rmap = self.graph.vertex_properties["node rvals"])
        
        graph_draw(self.graph, 
                   pos = position,
                   output_size = output_size,
                   bg_color = "white",
                   vertex_size = vertex_size,
                   vertex_font_size = vertex_font_size,
                   edge_font_size = edge_font_size,
                   vertex_text = self.graph.vertex_properties["node names"],
                   edge_text = self.graph.edge_properties["edge strings"], 
                   output=filepath)