from DGGraph import DGGraph

# This function should be able to compare abstract relationships defined between entities
#   in policy to definitions at the terms and conditions level, find errors in the specification,
#   and return those errors along with a suggested corrected graph (that satisfies compliance).
def graph_compare(dgg_toc, dgg_pol):
    errors = []
    for v_pol in dgg_pol.vertices():
        entity_pol = dgg_pol.nodes[dgg_pol.node_names[v_pol]]
        for v_toc in dgg_toc.vertices():
            entity_toc = dgg_toc.nodes[dgg_toc.node_names[v_toc]]
            errors.append(check_vertices(entity_pol, entity_toc))
    return errors

# Check whether rights and releases on entity_pol are a subset of those speciffied in entity_toc (compliance)
def check_vertices(entity_pol, entity_toc):
    if entity_pol == entity_toc:
        return False

# This function should be able to take specifications from two different entities
#   and merge the graphs to show the relationships that the entities in the graphs
#   have over the depicted data.
def graph_merge(dgg_1, dgg_2):
    for v_2 in dgg_2.vertices():
        entity_2 = dgg_2.nodes[dgg_2.node_names[v_2]]
        for v_1 in dgg_1.vertices():
            entity_toc = dgg_1.nodes[dgg_1.node_names[v_1]]


