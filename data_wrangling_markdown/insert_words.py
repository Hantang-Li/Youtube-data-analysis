import pandas as pd

ca_2017 = pd.read_csv("./CAvideos.csv")

ca_2017["trending_date"] = "20"+ca_2017["trending_date"]

ca_2017["trending_date"] = pd.to_datetime(ca_2017["trending_date"], format="%Y.%d.%m", errors='ignore', utc=True)

ca_2017.to_csv("CAvideos2.csv", index=False)
