from termsforterms import *

# This file contains the generation and operations over real-world privacy policies.

# Parse document formats
gdpr = parse_format("./tfts/gdpr.tft")
canvas = parse_format("./tfts/canvas.tft")
kaiser = parse_format("./tfts/kp.tft")
x_privpol = parse_format("./tfts/x_privpol.tft")
x_tos = parse_format("./tfts/x_tos.tft")

# Test merge and compare
x_docs = graph_merge(x_privpol, x_tos)
canvas_compliance = graph_compare(canvas, gdpr)

# Visualize
gdpr.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")
canvas.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")
kaiser.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")
x_privpol.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")
x_tos.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")

x_docs.render_graph(output_size = (2500, 1500),
                    filepath = "./generated/gdpr.png")