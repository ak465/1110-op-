import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
population_mean=statistics.mean(data)
Sampling=statistics.mean(data)
print("population mean is : ",population_mean)
print("Sampling mean: ",Sampling)


def random_set_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig = ff.create_distplot([df], ['temp'], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()




