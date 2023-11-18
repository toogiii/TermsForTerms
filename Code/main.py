from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum
from DGGraph import DGGraph

test_toc = DGGraph("initial graph", "terms/conditions")
user = DataSubject("user", set(), test_toc)
amzn = DataProcessor("amazon", set(), set(), test_toc)
name = Datum("name", {user}, set(), test_toc, set(), set())
comp = DataController("do-it", {name}, test_toc)

amzn.add_processed({comp})
amzn.add_processed_data({name})

test_toc.render_graph()
