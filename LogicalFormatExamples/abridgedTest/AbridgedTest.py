from termsforterms import *

# Abridged Tests: Graph, Merge, and Compare with Toy Examples

# Control: Create network for Alice's ice cream shop
alice_graph = DGGraph("Alice's Ice Cream Parlor",
    "Analyzing relationships between entities that interact with Alice's Ice Cream Parlor.")

# Entities in this network
customer = DataSubject("Customer", alice_graph)
employee = DataSubject("Employee", alice_graph)
other_customers = DataProcessor("Other Customers", alice_graph)
aws = DataProcessor("AWS", alice_graph)
alice = DataController("Alice", alice_graph)

other_customers.add_controller(alice)
aws.add_controller(alice)

# Data
customer_personal = Datum("Personal Info", alice_graph)
customer_demog = Datum("Demographic Vector", alice_graph)
customer_prefs = Datum("Ice Cream Preference", alice_graph)
customer_n_per_week = Datum("Visits per Week", alice_graph)
customer_dates = Datum("Dates of Visits", alice_graph)
customer_data = [customer_personal,  customer_prefs, customer_n_per_week, customer_dates]

employee_personal = Datum("Employee Personal Info", alice_graph)
employee_hours = Datum("Employee Hours Logged", alice_graph)
employee_days_absent = Datum("Employee Absence", alice_graph)
employee_data = [employee_personal, employee_hours, employee_days_absent]

# Customer data properties
customer_s_props = {("consent control", "accuracy", "security", "restriction of processing")}
customer_c_props = {("consent", "contractual obligation",
    "inform subject of details of processing")}
customer_p_props = {("transparency", "security", "contractual obligation",
    "controller authorization", "controller compliance", "controller notification"), 
    ("transparency", "security", "legal obligation")}

for datum in customer_data:
    datum.add_s_props(customer_s_props)
    datum.add_c_props(customer_c_props)
    datum.add_p_props(customer_p_props)

# Demographic data properties (sensitive)
customer_demog_s_props = {("consent control", "accuracy", "security",
    "restriction of processing", "necessity")}
customer_demog_c_props = {("consent", "contractual obligation",
    "inform subject of details of processing", "non-profit security")}
customer_demog.add_s_props(customer_demog_s_props)
customer_demog.add_c_props(customer_demog_c_props)
customer_demog.add_p_props(customer_p_props)

employee_s_props = {("consent control", "accuracy", "security",
    "restriction of processing")}
employee_c_props = {("consent", "contractual obligation",
    "inform subject of details of processing")}
employee_p_props = {("transparency", "security", "contractual obligation", 
    "controller authorization", "controller compliance", "controller notification"), 
    ("legal obligation", "security")}

# Add Ownership
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

# Draw graph
alice_graph.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,                              
                        filepath = "./control/alice.png")

# Control: Create network for franchiser's perspective
franchise_graph = DGGraph("Ice Cream Parlor Inc.", 
    "Analyzing relationships between the larger company and Alice's employees")

# Entities
franchise_owner = DataController("Company", franchise_graph)
employee_fr = DataSubject("Employee", franchise_graph)
other_franchises = DataSubject("Other Franchises", franchise_graph)
payroll_processor = DataProcessor("Payroll Processor", franchise_graph)

# Data
employee_fr_hours = Datum("Employee Hours Logged", franchise_graph)
employee_fr_days_absent = Datum("Employee Absence", franchise_graph)
employee_fr_data = [employee_fr_hours, employee_fr_days_absent]

other_franchise_data = Datum("Other Franchise Data", franchise_graph)

payroll_processor.add_controller(franchise_owner)

# Use previous props
for datum in employee_fr_data:
    datum.add_s_props(employee_s_props)
    datum.add_c_props(employee_c_props)
    datum.add_p_props(employee_p_props)
    datum.add_owner(employee_fr)
    datum.add_controller(franchise_owner)
    datum.add_processor(payroll_processor)

# Add ownership
other_franchise_data.add_s_props(customer_s_props)
other_franchise_data.add_c_props(customer_c_props)
other_franchise_data.add_owner(other_franchises)
other_franchise_data.add_controller(franchise_owner)

# Graph
franchise_graph.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,
                        filepath = "./control/company.png")


# Merge franchiser and franchisee (Alice's) graphs
merged = graph_merge(alice_graph, franchise_graph)

merged.render_graph(output_size = (2500, 1500),
                    filepath = "./control/merged.png")

# Evaluate generated graphs using .tfts against controls
generated_alice = parse_format("./tfts/alice.tft")
generated_company = parse_format("./tfts/company.tft")
generated_merged = graph_merge(generated_alice, generated_company)

# Generate legal policy graph
generated_policy = parse_format("./tfts/policy.tft")

generated_alice.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,                               
                        filepath = "./generated/alice.png")

generated_company.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,
                        filepath = "./generated/company.png")

generated_merged.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/merged.png")

generated_policy.render_graph(output_size = (2000, 1200),
                        vertex_font_size=20,
                        edge_font_size=20,
                        filepath = "./generated/policy.png")

# Define analogous pairings
company_to_policy_map = {
    "Company": ["Corporation"],
    "Payroll Processor": ["Payor"],
    "Employee Hours Logged": ["Employee Data"],
    "Employee Absences": ["Employee Data"]
}

# Compare company policy to legal policy
error_list = graph_compare(generated_company, generated_policy, company_to_policy_map)