from graph_tool.all import *
from DGGraph import DGGraph
from Datum import Datum
from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor

# This function should be able to compare abstract relationships defined between entities
#   in policy to definitions at the terms and conditions level, find errors in the specification,
#   and return those errors along with a suggested corrected graph (that satisfies compliance).
def graph_compare(dgg_toc, dgg_pol, analogous_entity_map={}):
    # Identity mappings
    for name in dgg_toc.node_names.values():
        if name not in analogous_entity_map.keys():
            analogous_entity_map[name] = name

    # Analyze all entity pairs
    errors = []
    for v_toc in dgg_toc.graph.vertices():
        entity_toc = dgg_toc.nodes[v_toc]
        for v_pol in dgg_pol.graph.vertices():
            entity_pol = dgg_pol.nodes[v_pol]
            if entity_pol.name == analogous_entity_map[entity_toc.name]:
                edge_comps = get_analogous_edge_props(entity_toc, entity_pol, dgg_toc, dgg_pol, analogous_entity_map)
                for vertices in edge_comps.keys():
                    props = edge_comps[vertices]
                    if not props[0].subset(props[1]):
                        error_string = "The edge between " + dgg_toc.nodes[vertices[0]].name + " and " 
                        error_string += dgg_toc.nodes[vertices[1]] + " has properties\n\t" + props[0]
                        error_string += "in the first policy and properties\n\t" + props[1] + "\nin the other policy"
    return errors

# Check whether rights and releases on entity_pol are a subset of those specified in entity_toc (compliance)
def get_analogous_edge_props(entity_toc, entity_pol, dgg_toc, dgg_pol, analogous_entity_map):
    v_toc = entity_toc.vertex
    v_pol = entity_pol.vertex
    analogous_edge_props = []
    for e_toc, v_target_toc in zip(v_toc.in_edges(), v_toc.in_neighbors()):
        target_toc = dgg_toc.nodes[v_target_toc]
        found = False

        for e_pol, v_target_pol in zip(v_pol.in_edges(), v_pol.in_neighbors()):
            target_pol = dgg_toc.nodes[v_target_pol]
            if target_pol.name == analogous_entity_map[target_toc.name]:
                found = True
                analogous_edge_props[(v_toc, v_pol)] = (dgg_toc.graph.edge_props[e_toc], dgg_pol.graph.edge_props[e_pol])

        if not found:
            raise Exception("No analog in second policy for edge between " + target_toc.name + " and " + entity_toc.name + ".")
    return analogous_edge_props

# This function should be able to take specifications from two different entities
#   and merge the graphs to show the relationships that the entities in the graphs
#   have over the depicted data.
def graph_merge(dgg_1, dgg_2, name="Merged Graph", purpose="Merging governances for graphs provided"):
    # Create node map by name and map for whether a v_2 has been created and doesn't need merging
    #   (v_2_mapped[n] == 0), needs merging (v_2_mapped[n] == 1), or has been mapped (v_2_mapped[n] == 2)
    merged_dgg = DGGraph(name=name, purpose=purpose)
    created_nodes = {}
    v_2_mapped = {}

    # First, create nodes to merge and indicate what v_2 analogs have been created
    for v_1 in dgg_1.graph.vertices():
        name_1 = dgg_1.node_names[v_1]
        created_nodes[name_1] = create_node(dgg_1.nodes[v_1], merged_dgg)
        for v_2 in dgg_2.graph.vertices():
            name_2 = dgg_2.node_names[v_2]
            if name_1 == name_2:
                v_2_mapped[v_2] = 1

    # Create unmapped v_2's
    for v_2 in dgg_2.graph.vertices():
        name_2 = dgg_2.node_names[v_2]
        if v_2 not in v_2_mapped.keys():
            created_nodes[name_2] = create_node(dgg_2.nodes[v_2], merged_dgg)
            v_2_mapped[v_2] = 0

    # Merge and/or map all created nodes
    for v_1 in dgg_1.graph.vertices():
        name_1 = dgg_1.node_names[v_1]
        mapped = False

        for v_2 in dgg_2.graph.vertices():
            name_2 = dgg_2.node_names[v_2]

            # If v_2 unmapped (datum) and doesn't need merge
            if v_2_mapped[v_2] == 0 and type(created_nodes[name_2]) == Datum:
                populate_datum_props(created_nodes[name_2], dgg_2.nodes[v_2])
                add_datum_edges(created_nodes[name_2], dgg_2.nodes[v_2], created_nodes)
                v_2_mapped[v_2] = 2
                
            # If v_2 needs merge
            elif v_2_mapped[v_2] == 1 and name_1 == name_2 and type(created_nodes[name_1]) == Datum:
                populate_datum_props(created_nodes[name_1], dgg_1.nodes[v_1])
                populate_datum_props(created_nodes[name_2], dgg_2.nodes[v_2])
                add_datum_edges(created_nodes[name_1], dgg_1.nodes[v_1], created_nodes)
                add_datum_edges(created_nodes[name_2], dgg_2.nodes[v_2], created_nodes)
                v_2_mapped[v_2] = 2
                mapped = True

            # If v_2 unmapped (processor) and doesn't need merge
            if v_2_mapped[v_2] == 0 and type(created_nodes[name_2]) == DataProcessor:
                add_processor_edges(created_nodes[name_2], dgg_2.nodes[v_2], created_nodes)
                v_2_mapped[v_2] = 2
                
            # If v_2 needs merge
            elif v_2_mapped[v_2] == 1 and name_1 == name_2 and type(created_nodes[name_1]) == DataProcessor:
                add_processor_edges(created_nodes[name_1], dgg_1.nodes[v_1], created_nodes)
                add_processor_edges(created_nodes[name_2], dgg_2.nodes[v_2], created_nodes)
                v_2_mapped[v_2] = 2
                mapped = True
        
        # If v_1 has not been mapped yet
        if not mapped and type(created_nodes[name_1]) == Datum:
            populate_datum_props(created_nodes[name_1], dgg_1.nodes[v_1])
            add_datum_edges(created_nodes[name_1], dgg_1.nodes[v_1], created_nodes)
        elif not mapped and type(created_nodes[name_1]) == DataProcessor:
            add_processor_edges(created_nodes[name_1], dgg_1.nodes[v_1], created_nodes)

    return merged_dgg


# Create node in new graph according to analog in previous graph 
def create_node(node, dgg):
    if type(node) == Datum:
        return Datum(node.name, dgg)
    elif type(node) == DataSubject:
        return DataSubject(node.name, dgg)
    elif type(node) == DataController:
        return DataController(node.name, dgg)
    elif type(node) == DataProcessor:
        return DataProcessor(node.name, dgg)
    else:
        raise Exception("Unrecognized node type.")
    
# Populate datum properties for new node for merge
def populate_datum_props(datum, old_datum):
    datum.add_s_props(old_datum.s_props)
    datum.add_c_props(old_datum.c_props)
    datum.add_p_props(old_datum.p_props)

# Add back datum edges for new node for merge according to analogs
def add_datum_edges(datum, old_datum, all_nodes):
    for owner in old_datum.owners:
        datum.add_owner(all_nodes[owner.name])
    for controller in old_datum.controllers:
        datum.add_controller(all_nodes[controller.name])
    for processor in old_datum.processors:
        datum.add_processor(all_nodes[processor.name])

# Add back processor edges for new node for merge according to analogs
def add_processor_edges(processor, old_processor, all_nodes):
    for controller in old_processor.controllers:
        processor.add_controller(all_nodes[controller.name])