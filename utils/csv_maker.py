import csv
import pandas as pd
from coin_gecko import *
import time


colnames = ['number', 'date']
jump = 2
df = pd.read_csv('../data/days.csv', names=colnames)
lenght = len(df)
i = 3860
a = [0, 0, 0, 0, 0, 0, 0, 0]
n = 0           # acumulated values in a
w = 0           # wroten useful rows(0-7)
j = 1

with open('../data/ethereum-answers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eight'])
    while i < lenght-7:
        try:
            b = get_single_price('ethereum', df.loc[i, "date"])
            try:
                a[n] = b
                n = n + 1
            except IndexError:
                if w == 0:
                    writer.writerow([a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 1:
                    writer.writerow([a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[0]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 2:
                    writer.writerow([a[2], a[3], a[4], a[5], a[6], a[7], a[0], a[1]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 3:
                    writer.writerow([a[3], a[4], a[5], a[6], a[7], a[0], a[1], a[2]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 4:
                    writer.writerow([a[4], a[5], a[6], a[7], a[0], a[1], a[2], a[3]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 5:
                    writer.writerow([a[5], a[6], a[7], a[0], a[1], a[2], a[3], a[4]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 6:
                    writer.writerow([a[6], a[7], a[0], a[1], a[2], a[3], a[4], a[5]])
                    a[w] = b
                    print(j)
                    j += 1
                elif w == 7:
                    writer.writerow([a[7], a[0], a[1], a[2], a[3], a[4], a[5], a[6]])
                    a[w] = b
                    w = -1
                    print(j)
                    j += 1
                w = w+1

        except KeyError:
            n = 0

        except:
            i = i - 1
            print("Sleeping")
            time.sleep(60)
        i = i + 1
