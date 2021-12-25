import csv
import statistics
import pandas as pd
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist= False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ", population_mean)
population_standarddeviation = statistics.stdev(data)
print("Standard Deviation = ", population_standarddeviation)

#Code to find mean and standard deviation of 100 data points 
dataset = []
for i in range (0,1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
standarddeviation = statistics.stdev(dataset)
print("Mean of 1000 values ", mean)
print("Standard deviation of 1000 values", standarddeviation)