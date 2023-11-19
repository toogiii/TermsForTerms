from DGGraph import DGGraph
from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum

# This function includes the methods that allow for translation from the .tft logical format into
#   the DGG.
def parse_format(filename):
    # Open file
    file = open(filename, "r")
    data = [line.rstrip() for line in file.readlines()]
    file.close()
    new_graph = DGGraph()
    
    # Get title and purpose
    new_graph.name = data[0]
    new_graph.purpose = data[1]

    # Get all non-data entities and add to graph
    subject_names = data[4].split(": ")[1].split(", ")
    subjects = []
    for name in subject_names:
        subjects.append(DataSubject(name, new_graph))

    controller_names = data[5].split(": ")[1].split(", ")
    controllers = []
    for name in controller_names:
        controllers.append(DataController(name, new_graph))

    processor_names = data[6].split(": ")[1].split(", ")
    processors = []
    for name in processor_names:
        processors.append(DataProcessor(name, new_graph))
    
    # Parse data and relationships between entities
    data = parse_data(data[7:], subjects, controllers, processors, new_graph)

    # Render and return graph
    new_graph.render_graph()
    return new_graph

# Associate data with some property specifications and establish relationships among objects
def parse_data(data_lines, subjects, controllers, processors, graph):
    data_properties = get_data_declarations(data_lines, graph)
    data = establish_relationships(data_properties, subjects, controllers, processors, graph)
    return data

# Find all data objects and associate them with their descriptions
def get_data_declarations(data_lines, graph):
    data_properties = {}
    i = 0
    curr_names = []
    curr_properties = []
    while i < len(data_lines):
        line = data_lines[i]
        # If a new data segment is found, create the previous data segment 
        #   and associate it with its expressions. Then, start over
        if "Data " in line:
            for name in curr_names:
                data_properties[Datum(name, graph)] = curr_properties

            curr_names = line[5:line.index(" is")].split(", ")
            curr_properties = []
        # Associate the descriptor (line i) to the current data object
        else:
            curr_properties.append(line)
        i += 1

    # For the final data segment
    for name in curr_names:
        data_properties[Datum(name, graph)] = curr_properties
    return data_properties

def establish_relationships(data_properties, subjects, controllers, processors, graph):
    # For each piece of data
    for datum in data_properties.keys():
        props = data_properties[datum]
        # Establish owner, controller, and processor data
        get_owners(datum, subjects, props[0], graph)
        get_controllers(datum, controllers, props[1], graph)
        get_processors(datum, processors, controllers, props[2], graph)
    # Return data objects
    return data_properties.keys()

# Get and associate a datum with its owners and owner rights
def get_owners(datum, subjects, expression, graph):
    rights = set(expression[expression.index(" with rights to ") + 16:].split(", "))
    datum.add_rights(rights)

    owner_names = expression[expression.index("owned by ") + 8: expression.index(" with rights to ")].split(", ")
    for name in owner_names:
        subject = get_entity_with_name(name, subjects)
        datum.add_owner(subject)

# Get and associate a datum with its controllers and control conditions
def get_controllers(datum, controllers, expression, graph):
    c_releases = set(expression[expression.index(" under conditions of ") + 21:].split(", "))
    datum.add_c_releases(c_releases)

    controller_names = expression[expression.index("controlled by ") + 14: expression.index(" under conditions of ")].split(", ")
    for name in controller_names:
        controller = get_entity_with_name(name, controllers)
        datum.add_controller(controller)

# Get and associate a datum with its processors and processing conditions
def get_processors(datum, processors, controllers, expression, graph):
    p_releases = set(expression[expression.index(" under conditions of ") + 21:].split(", "))
    datum.add_p_releases(p_releases)

    processor_names = expression[expression.index("processed by ") + 13: expression.index(" under conditions of ")].split(", ")

    for name in processor_names:
        processor = get_entity_with_name(name, processor)
        datum.add_processor(processor)

        # Associate the processors with all the controllers also associated with the data
        for controller in datum.controllers:
            processor.add_controller(controller)

# Given an list of EntityNodes, find the one with a given name
def get_entity_with_name(name, entity_list):
    for entity in entity_list:
        if entity.name == name:
            return entity