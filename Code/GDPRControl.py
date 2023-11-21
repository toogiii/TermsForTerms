from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum
from DGGraph import DGGraph

# Control Case 1: GDPR
gdpr_graph = DGGraph("GDPR Data Regulation", "Represent data governance as specified by the GDPR")

# Non-Data Entities
subject = DataSubject("data subject", gdpr_graph)
child_subject = DataSubject("child subject", gdpr_graph)
controller = DataController("data controller", gdpr_graph)
processor = DataProcessor("data processor", gdpr_graph)

processor.add_controller(controller)

# Data
personal_sub = Datum("personal data", gdpr_graph)
revealing_sub = Datum("revealing data", gdpr_graph)
genetic_sub = Datum("genetic data", gdpr_graph)
biometric_sub = Datum("biometric data", gdpr_graph)
health_sub = Datum("health data", gdpr_graph)
crime_sub = Datum("criminal data", gdpr_graph)

data = [personal_sub, revealing_sub, genetic_sub, biometric_sub, health_sub, crime_sub]
sensitive_data = data[1:]

personal_child = Datum("personal data", gdpr_graph)
revealing_child = Datum("revealing data", gdpr_graph)
genetic_child = Datum("genetic data", gdpr_graph)
biometric_child = Datum("biometric data", gdpr_graph)
health_child = Datum("health data", gdpr_graph)
crime_child = Datum("criminal data", gdpr_graph)

child_data = [personal_child, revealing_child, genetic_child, biometric_child, health_child, crime_child]
sensitive_child_data = child_data[1:]

general_rights = {"control over consent", "safety", "security", "accuracy", "knowledge of purpose", "access", "rectification", "erasure", "restriction of processing", "portability", "objection"}
general_p_releases = {"transparency", "security", "contractual obligation", "legal obligation", "controller authorization", "controller compliance", "controller notification"}
general_c_releases = {"consent", "necessity", "contractual obligation", "legal obligation", "public interest", "security", "details of self provided", "purpose provided", "location of processing provided", "recipients of data provided", "period of storage provided", "informance of user rights", "contract"}
for datum in data:
    datum.add_rights(general_rights)
    datum.add_c_releases(general_c_releases)
    datum.add_p_releases(general_p_releases)
for child_datum in child_data:
    child_datum.add_rights(general_rights)
    child_datum.add_c_releases(general_c_releases)
    child_datum.add_p_releases(general_p_releases)

    child_datum.add_rights({"parental control over consent"})
    child_datum.add_c_releases({"verified parental consent"})

sensitive_rights = {"necessity"}
sensitive_c_releases = {"non-profit security", "medical purposes", "employment law"}
sensitive_p_releases = {"verifiable security"}
for datum in sensitive_data:
    datum.add_rights(sensitive_rights)
    datum.add_c_releases(sensitive_c_releases)
    datum.add_p_releases(sensitive_p_releases)
for child_datum in sensitive_child_data:
    child_datum.add_rights(sensitive_rights)
    child_datum.add_c_releases(sensitive_c_releases)
    child_datum.add_p_releases(sensitive_p_releases)
    
crime_sub.add_rights({"government mediation"})
crime_sub.add_c_releases({"Union law mediation"})
crime_child.add_rights({"government mediation"})
crime_child.add_c_releases({"Union law mediation"})

for datum in data:
    datum.add_owner(subject)
    datum.add_processor(processor)
    datum.add_controller(controller)

for datum in child_data:
    datum.add_owner(child_subject)
    datum.add_processor(processor)
    datum.add_controller(controller)

gdpr_graph.render_graph(output_size = (2000, 2000),
                        filepath = "/Users/gsgaur/Documents/GitHub/TermsForTerms/LogicalFormatExamples/controlFigs/gdpr.png")