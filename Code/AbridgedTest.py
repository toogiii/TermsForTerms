from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum
from DGGraph import DGGraph

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
customer_data = [customer_personal, customer_demog, customer_prefs, customer_n_per_week, customer_dates]

employee_personal = Datum("Personal Info", ice_cream_network)
employee_hours = Datum("Employee Hours Logged", ice_cream_network)
employee_days_absent = Datum("Employee Absence", ice_cream_network)
employee_data = [employee_personal, employee_hours, employee_days_absent]

customer_rights = {"consent control", "accuracy", "security", "restriction of processing"}
customer_c_releases = {"consent", "contractual obligation", "inform of details of processing"}
customer_p_releases = {"transparency", "security", "contractual obligation", "legal obligation", "controller authorization", "controller compliance", "controller notification"}

for datum in customer_data:
    datum.add_rights(customer_rights)
    datum.add_c_releases(customer_c_releases)
    datum.add_p_releases(customer_p_releases)

customer_demog.add_rights({"necessity"})
customer_demog.add_c_releases({"non-profit security"})

employee_rights = {"consent control", "accuracy", "security", "restriction of processing"}
employee_c_releases = {"consent", "contractual obligation", "inform of details of processing"}

for datum in employee_data:
    datum.add_rights(employee_rights)
    datum.add_c_releases(employee_c_releases)

for datum in customer_data:
    datum.add_owner(customer)
    datum.add_processor(other_customers)
    datum.add_processor(aws)
    datum.add_controller(alice)

for datum in employee_data:
    datum.add_owner(employee)
    datum.add_controller(alice)

ice_cream_network.render_graph(output_size = (2000, 2000),
                        filepath = "/Users/gsgaur/Documents/GitHub/TermsForTerms/abridged_example.png")