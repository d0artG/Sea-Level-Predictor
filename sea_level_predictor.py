import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    first=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    ax.plot(range(1880, 2051, 1), first.intercept + first.slope*range(1880, 2051, 1))

    # Create second line of best fit
    df_second=df[df["Year"]>=2000]
    second=linregress(df_second["Year"],df_second["CSIRO Adjusted Sea Level"])
    ax.plot(range(df_second["Year"].min(), 2051, 1), second.intercept + second.slope*range(df_second["Year"].min(), 2051, 1))

    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)',title="Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
