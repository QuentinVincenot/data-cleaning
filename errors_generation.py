import pandas as pd
import numpy as np

def introduce_error_category_NaN(dataframe):
	errors_indices = np.random.choice(50, 12, replace=False)
	for index in errors_indices:
		dataframe.iloc[index, [0]] = np.random.choice(['NaN', 'null', '???', 'UNKWN'], 1, p=[0.25, 0.25, 0.25, 0.25])

def introduce_error_height_NaN(dataframe):
	errors_indices = np.random.choice(50, 7, replace=False)
	dataframe.iloc[errors_indices, [1]] = np.nan

def introduce_error_date_NaN(dataframe):
	errors_indices = np.random.choice(50, 5, replace=False)
	dataframe.iloc[errors_indices, [2]] = np.nan

def introduce_error_country(dataframe):
	possible_countries = ['USA', 'uSa', 'Brasil', 'brUsil', 'France', 'Fr', 'South Africa', 'SAF', 'China', 'CHinA']
	countries_probabilities = [0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05]
	return possible_countries, countries_probabilities
