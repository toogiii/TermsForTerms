from DGGraph import DGGraph

def graph_compare(dgg_toc, dgg_pol):
    errors = []
    for v_pol in dgg_pol.vertices():
        entity_pol = dgg_pol.nodes[dgg_pol.node_names[v_pol]]
        for v_toc in dgg_toc.vertices():
            entity_toc = dgg_toc.nodes[dgg_toc.node_names[v_toc]]
            errors.append(check_vertices(entity_pol, entity_toc))
    return errors

def check_vertices(entity_pol, entity_toc):
    # Check whether rights and releases on entity_pol are a subset of those speciffied in entity_toc
    if entity_pol == entity_toc:
        return False

def graph_merge(dgg_1, dgg_2):
    # Add rights and releases specified in pol to toc for relationships specified
    for v_2 in dgg_2.vertices():
        entity_2 = dgg_2.nodes[dgg_2.node_names[v_2]]
        for v_1 in dgg_1.vertices():
            entity_toc = dgg_1.nodes[dgg_1.node_names[v_1]]


