import pandas as pd
import numpy as np
from csv import writer
import json

df_payload = pd.read_csv('./data/last_payload.csv')
df_payload = df_payload.head(1000)
df_payload.sort_values(by=['Time'], inplace=True)

initial_time = 1592665552000
last_time = 1592665745400 + 5000

values = {
    "481714f496e4",
    "6f2c053265f6",
    "78034b84ad0f",
    "8d2d383ac982"
}
dictValues = dict.fromkeys(values, 0)

for property, value in dictValues.items():
    for i in df_payload[property]:
        if i > value:
            dictValues[property] = i

print(dictValues)

times = [1592665703000, 1592665700000, 1592665705000, 1592665704000]


with open('./data/last_payload.csv', 'a+', newline='') as csvfile:
    csv_writer = writer(csvfile)

    for property, value in dictValues.items():
        if property == "481714f496e4":
            time = 1592665703000
            time = time + 5000
            while time < last_time:
                csv_writer.writerow([time, value, '', '', ''])
                time = time + 5000
        elif property == "6f2c053265f6":
            time = 1592665700000
            time = time + 5000
            while time < last_time:
                csv_writer.writerow([time, '', value, '', ''])
                time = time + 5000
        elif property == "78034b84ad0f":
            time = 1592665705000
            time = time + 5000
            while time < last_time:
                csv_writer.writerow([time, '', '', value, ''])
                time = time + 5000
        elif property == "8d2d383ac982":
            time = 1592665704000
            time = time + 5000
            while time < last_time:
                csv_writer.writerow([time, '', '', '', value])
                time = time + 5000
