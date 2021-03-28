import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np

filepath = "F:\Computer Programming\Python-dev\HistoricalQuotes.csv"

df = pd.read_csv(filepath)

print(df.head())

#plt.pyplot.hist(df["Open"])

print(df.describe())