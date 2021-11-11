import pandas as pd
import numpy as np

## Reading the datasets
conf, deaths, recovered = pd.read_csv("confirmed_country_month.csv"), pd.read_csv("deaths_country_month.csv"), pd.read_csv("recovered_country_month.csv")

## Merging multiple datasets
merged = pd.merge(conf, deaths, on = ['Country/Region', 'Year-Month'])
merged = pd.merge(merged, recovered, on = ['Country/Region', 'Year-Month'])

## Writing to csv
merged.to_csv("cases_country_month.csv", index = False, header = ['Country/Region', 'Year-Month', 'Confirmed', 'Deaths', 'Recovered'])