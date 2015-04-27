import pandas as pd
import numpy as np

turnstile_master = pd.read_csv("turnstile_data_master_with_weather.csv")
dummy_units = pd.get_dummies(turnstile_master['UNIT'], prefix='unit')

features = turnstile_master[['rain', 'precipi', 'Hour', 'meantempi']]#.join(dummy_units)
values = turnstile_master[['ENTRIESn_hourly']]
m = len(values)
num_iterations=6
alpha = 0.1
theta=np.zeros(len(features.columns))
print theta
prediction_value=np.dot(features,theta)
print prediction_value
a=prediction_value-values
print a
b= m*np.dot(a,features)
print b

for i in range(num_iterations):
        prediction_value=np.dot(features,theta)
        x=m*np.dot((prediction_value-values),features)
        print x
        #theta=theta-(alpha/x)
        
        


