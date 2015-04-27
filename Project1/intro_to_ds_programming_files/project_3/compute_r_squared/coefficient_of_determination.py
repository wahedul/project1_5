import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys
from prediction import predictions


def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    average=np.average(data)
    l=len(data)
    for i in range(l):
        a= np.square(data-predictions).sum()
        b= np.square(data-average).sum()
     
    r_squared=1-(a/b)
    
    # your code here
    
    return r_squared

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values)
    print r_squared

# MemoryError please look at udacity webside probelm set3 question7 for solution

#Your calculated R^2 value is: 0.318137233709
