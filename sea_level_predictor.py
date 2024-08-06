import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    Year = df['Year']
    Adj_sea_level = df['CSIRO Adjusted Sea Level']
    plt.scatter(x=Year,y=Adj_sea_level)
    
    # Create first line of best fit
    line1 = linregress(Year,Adj_sea_level)
    x = np.arange(Year.min(),2051)
    y = line1.intercept + line1.slope * x
    plt.plot(x,y,'r')

    # Create second line of best fit
    filtered_year = df[df['Year'] >= 2000]
    line2 = linregress(filtered_year['Year'],filtered_year['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051)
    y2 = line2.intercept + line2.slope * x2
    plt.plot(x2,y2,'orange')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
