#importing pandas package

import pandas as pd

#making data frame from csv file
data = pd.read_csv("county_demographics.csv", index_col = "State")

#retrieving rows by loc method
rows = data.loc["TX"]

# priting the data having rows
print(rows)

#saving the file to csv
rows.to_csv("TexasData.csv")

