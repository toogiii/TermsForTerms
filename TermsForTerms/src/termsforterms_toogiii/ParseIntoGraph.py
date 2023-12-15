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
    data = [line.rstrip().lstrip() for line in file.readlines()]
    file.close()
    new_graph = DGGraph(data[0], data[1])

    # Get all non-data entities and add to graph
    subject_names = data[3][data[3].index(": ") + 2:].split(", ")
    subjects = {}
    for name in subject_names:
        subjects[name] = DataSubject(name, new_graph)

    controller_names = data[4][data[4].index(": ") + 2:].split(", ")
    controllers = {}
    for name in controller_names:
        controllers[name] = DataController(name, new_graph)

    processor_names = data[5][data[5].index(": ") + 2:].split(", ")
    processors = {}
    for name in processor_names:
        processors[name] = DataProcessor(name, new_graph)
    
    # Parse data and relationships between entities
    parse_data(data[6:], subjects, controllers, processors, new_graph)

    # Return graph
    return new_graph

# Associate data with some property specifications and establish relationships among objects
def parse_data(data_lines, subjects, controllers, processors, graph):
    data = []

    for i in range(len(data_lines)):
        line = data_lines[i]
        if "Processor-Controllers: " in line:
            processor_names = line[line.index("Processor-Controllers: ") + 23:line.index(" are controlled by ")].split(", ")
            c_processors = [processors[i] for i in processor_names]
            controller_names = line[line.index(" are controlled by ") + 19:-1].split(", ")
            p_controllers = [controllers[i] for i in controller_names]

            for processor in c_processors:
                for controller in p_controllers:
                    processor.add_controller(controller)

        elif "Data: " in line:
            data_names = line[line.index("Data: ") + 6:line.index(" are")].split(", ")
            data = [Datum(i, graph) for i in data_names]

        elif "owned by " in line:
            subject_names = line[line.index("owned by ") + 9:line.index(" with rights to")].split(", ")
            prop_list = set()
            i += 1
            while line[-1] != ".":
                line = data_lines[i]
                props = tuple([i for i in line[:-1].split(", ")])
                prop_list.add(props)
                i += 1
            for datum in data:
                datum.add_s_props(prop_list)
                for name in subject_names:
                    datum.add_owner(subjects[name])

        elif "controlled by " in line:
            controller_names = line[line.index("controlled by ") + 14:line.index(" under conditions of")].split(", ")
            prop_list = set()
            i += 1
            while line[-1] != ".":
                line = data_lines[i]
                props = tuple([i for i in line[:-1].split(", ")])
                prop_list.add(props)
                i += 1
            for datum in data:
                datum.add_c_props(prop_list)
                for name in controller_names:
                    datum.add_controller(controllers[name])
                    
        elif "processed by " in line:
            processor_names = line[line.index("processed by ") + 13:line.index(" under conditions of")].split(", ")
            prop_list = set()
            i += 1
            while line[-1] != ".":
                line = data_lines[i]
                props = tuple([i for i in line[:-1].split(", ")])
                prop_list.add(props)
                i += 1
            for datum in data:
                datum.add_p_props(prop_list)
                for name in processor_names:
                    datum.add_processor(processors[name])