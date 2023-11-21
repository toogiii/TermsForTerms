from DataSubject import DataSubject
from DataController import DataController
from DataProcessor import DataProcessor
from Datum import Datum
from DGGraph import DGGraph

# Control Case 2: Twitter
twitter_graph = DGGraph("Twitter Privacy Policy", "Twitter's data relationships as outlined in their privacy policy")

# Non-Data Entities
user = DataSubject("User", twitter_graph)
twitter = DataController("Twitter", twitter_graph)
affiliates = DataController("Affiliates", twitter_graph)
analysts = DataProcessor("Analysts", twitter_graph)

# We consider other users processors of the data, as they are governed
#   by contracts set out by Twitter and thus are not so different from
#   (mostly) not-for-profit analysts that consume data for entertainment
other_users = DataProcessor("other users", twitter_graph)


# Data
personal_data = Datum("personal data", twitter_graph)
pro_account_data = Datum("pro account data", twitter_graph)
payment_info = Datum("payment information", twitter_graph)
preferences = Datum("preferences", twitter_graph)
biometric_info = Datum("biometric information", twitter_graph)
job_info = Datum("job information", twitter_graph)
posts = Datum("posts", twitter_graph)
broadcasts = Datum("broadcasts", twitter_graph)
interactions = Datum("interactions", twitter_graph)
transactions = Datum("transactions", twitter_graph)
device = Datum("device info", twitter_graph)
location = Datum("location", twitter_graph)
log_info = Datum("logs", twitter_graph)

