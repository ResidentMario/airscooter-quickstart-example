from zipfile import ZipFile
from calendar import monthrange
import os
import pandas as pd

z = ZipFile("nyc-east-river-bicycle-counts.zip", "r")
z.extractall()

xlsx_list = sorted([file for file in os.listdir(".") if "xls" in file.rsplit(".")[-1]])

data_by_month = []

for i, xlsx in enumerate(xlsx_list):
    days_in_month = monthrange(2016, i + 4)[1]
    data = (pd.read_excel("04 April 2016 Cyclist Numbers for Web.xlsx", skiprows=4, header=1)
            .iloc[:days_in_month, 1:-1])
    data_by_month.append(data)

unified_data = pd.concat(data_by_month)
unified_data = unified_data[unified_data['Date'] != 'T = trace of precipitation']
unified_data.reset_index(drop=True, inplace=True)
unified_data.to_csv("nyc-east-river-bicycle-counts.csv")

for fp in [file for file in os.listdir(".") if "xls" in file.rsplit(".")[-1]]:
    os.remove(fp)
os.remove("Bicycle Counts for East River Bridges Metadata.docx")
os.remove("nyc-east-river-bicycle-counts.zip")