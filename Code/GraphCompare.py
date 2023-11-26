from graph_tool.all import *
from DGGraph import DGGraph
from DataSubject import DataSubject
from Datum import Datum

# This function should be able to compare abstract relationships defined between entities
#   in policy to definitions at the terms and conditions level, find errors in the specification,
#   and return those errors along with a suggested corrected graph (that satisfies compliance).
def graph_compare(dgg_toc, dgg_pol, analogous_entity_map={}):
    for name in dgg_toc.node_names.values():
        if name not in analogous_entity_map.keys():
            analogous_entity_map[name] = name
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
def graph_merge(dgg_1, dgg_2, analogous_entity_map={}):
    for name in dgg_2.node_names.values():
        if name not in analogous_entity_map.keys():
            analogous_entity_map[name] = name

    intersection = dgg_2.graph.new_vp("int16_t")
    for v_1 in dgg_1.graph.vertices():
        name_1 = dgg_1.node_names[name_1]
        for v_2 in dgg_2.graph.vertices():
            name_2 = dgg_2.node_names[name_2]
            if name_1 == analogous_entity_map[name_2]:
                intersection[v_2] = v_1

    merged = graph_union(dgg_1.graph, dgg_2.graph, intersection=intersection)
    merged.render_graph(output_size = (2000, 2000),
                        filepath = "/Users/gsgaur/Documents/GitHub/TermsForTerms/merged.png")
    return merged
