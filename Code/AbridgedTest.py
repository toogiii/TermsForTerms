from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum
from DGGraph import DGGraph
from GraphCompare import *

# Control Case 0: Example Proof of Concept
# Here, we create a possible hypothetical for the users of an ice-cream store.
#   This will likely be used for the writeup.

ice_cream_network = DGGraph("Alice's Ice Cream Parlor", "Analyzing relationships between entities that interact with Alice's Ice Cream Parlor.")

customer = DataSubject("Customer", ice_cream_network)
employee = DataSubject("Employee", ice_cream_network)
other_customers = DataProcessor("Other Customers", ice_cream_network)
aws = DataProcessor("AWS", ice_cream_network)
alice = DataController("Alice", ice_cream_network)

other_customers.add_controller(alice)
aws.add_controller(alice)

customer_personal = Datum("Personal Info", ice_cream_network)
customer_demog = Datum("Demographic Vector", ice_cream_network)
customer_prefs = Datum("Ice Cream Preference", ice_cream_network)
customer_n_per_week = Datum("Visits per Week", ice_cream_network)
customer_dates = Datum("Dates of Visits", ice_cream_network)
customer_data = [customer_personal,  customer_prefs, customer_n_per_week, customer_dates]

employee_personal = Datum("Employee Personal Info", ice_cream_network)
employee_hours = Datum("Employee Hours Logged", ice_cream_network)
employee_days_absent = Datum("Employee Absence", ice_cream_network)
employee_data = [employee_personal, employee_hours, employee_days_absent]

customer_s_props = {("consent control", "accuracy", "security", "restriction of processing")}
customer_c_props = {("consent", "contractual obligation", "inform of details of processing")}
customer_p_props = {("transparency", "security", "contractual obligation", "controller authorization", "controller compliance", "controller notification"), ("transparency", "security", "legal obligation")}

for datum in customer_data:
    datum.add_s_props(customer_s_props)
    datum.add_c_props(customer_c_props)
    datum.add_p_props(customer_p_props)

customer_demog_s_props = {("consent control", "accuracy", "security", "restriction of processing", "necessity")}
customer_demog_c_props = {("consent", "contractual obligation", "inform of details of processing", "non-profit security")}
customer_demog.add_s_props(customer_demog_s_props)
customer_demog.add_c_props(customer_demog_c_props)
customer_demog.add_p_props(customer_p_props)

employee_s_props = {("consent control", "accuracy", "security", "restriction of processing")}
employee_c_props = {("consent", "contractual obligation", "inform of details of processing")}

for datum in employee_data:
    datum.add_s_props(employee_s_props)
    datum.add_c_props(employee_c_props)

customer_data.append(customer_demog)

for datum in customer_data:
    datum.add_owner(customer)
    datum.add_processor(other_customers)
    datum.add_processor(aws)
    datum.add_controller(alice)

for datum in employee_data:
    datum.add_owner(employee)
    datum.add_controller(alice)

ice_cream_network.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,                               
                        filepath = "../LogicalFormatExamples/controlFigs/alice.png")

franchise_network = DGGraph("Ice Cream Parlor's Inc.", "Analyzing relationships between the larger company and Alice's employees")

franchise_owner = DataController("Company", franchise_network)
employee_fr = DataSubject("Employee", franchise_network)
other_franchises = DataSubject("Other Franchises", franchise_network)

employee_fr_hours = Datum("Employee Hours Logged", franchise_network)
employee_fr_days_absent = Datum("Employee Absence", franchise_network)
employee_fr_data = [employee_fr_hours, employee_fr_days_absent]

other_franchise_data = Datum("Other Franchise Data", franchise_network)

for datum in employee_fr_data:
    datum.add_s_props(employee_s_props)
    datum.add_c_props(employee_c_props)
    datum.add_owner(employee_fr)
    datum.add_controller(franchise_owner)

other_franchise_data.add_s_props(customer_s_props)
other_franchise_data.add_c_props(customer_c_props)
other_franchise_data.add_owner(other_franchises)
other_franchise_data.add_controller(franchise_owner)

franchise_network.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,
                        filepath = "../LogicalFormatExamples/controlFigs/company.png")

merged = graph_merge(ice_cream_network, franchise_network)

merged.render_graph(output_size = (2500, 1500),
                    filepath = "../LogicalFormatExamples/controlFigs/merged.png")