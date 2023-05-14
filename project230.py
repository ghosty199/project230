import pandas as pd
dataset=loadtxt("country_vaccinations.csv",delimiter=",")
print("Shape of given dataset:",dataset.shape)
print("Count of column:",len(dataset.columns))
print("Name of parameter used:",dataset.columns)