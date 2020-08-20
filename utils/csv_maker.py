import csv
import pandas as pd
from coin_gecko import *


colnames = ['number', 'date']
jump = 2
df = pd.read_csv('../data/days.csv', names=colnames)
lenght = len(df)

with open('../data/bitcoin.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eight'])
    for i in range(lenght-7):
        writer.writerow([df.loc[i, "date"], df.loc[i+1, "date"], df.loc[i+2, "date"], df.loc[i+3, "date"],
                         df.loc[i+4, "date"], df.loc[i+5, "date"], df.loc[i+6, "date"], df.loc[i+7, "date"]])
