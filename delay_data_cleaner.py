import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\jssos\delaypredictor\airline_delay_cause.csv")
data=data.drop(data.columns[list(range(0, 4)) + [5] + list(range(8, len(data.columns)))], axis=1)
data_sorted=data.sort_values(by="airport")
totals = data.groupby("airport")[["arr_flights", "arr_del15"]].sum()

totals["delay_rate"]=(100*totals['arr_del15']/totals['arr_flights']).round(1)


# '''Bar Chart'''
# plt.figure(figsize=(10, 6))
# plt.bar(totals.index, totals["delay_rate"], color="skyblue")
# plt.xlabel("Airport")
# plt.ylabel("Delay Rate (%)")
# plt.title("Delay Rate by Airport")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



'''Scatter plot'''

plt.figure(figsize=(10, 6))
plt.scatter(totals["arr_flights"], totals["delay_rate"], color="darkorange", edgecolors="black")

plt.xlabel("Total Arriving Flights")
plt.ylabel("Delay Rate (%)")
plt.title("Delay Rate vs Total Flights by Airport")

for airport, row in totals.iterrows():
    plt.text(row["arr_flights"], row["delay_rate"], airport, fontsize=8, ha='right')

plt.grid(True)
plt.tight_layout()
plt.show()

