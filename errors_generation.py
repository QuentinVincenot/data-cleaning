import pandas as pd
import numpy as np

def introduce_error_missing_NaN(dataframe):
	errors_indices = np.random.choice(50, 38, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Missing')]] = np.nan

def introduce_error_category_null_values(dataframe):
	errors_indices = np.random.choice(50, 12, replace=False)
	for index in errors_indices:
		dataframe.iloc[index, [dataframe.columns.get_loc('Category')]] = np.random.choice(['NaN', 'null', '???', 'UNKWN'], 1, p=[0.25, 0.25, 0.25, 0.25])[0]

def introduce_error_height_NaN(dataframe):
	errors_indices = np.random.choice(50, 7, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Height')]] = np.nan

def introduce_error_salary_heterogeneous(dataframe):
	errors_indices = np.random.choice(50, 3, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Salary')]] = np.multiply(1000, np.random.randint(low=450, high=500, size=3))

def introduce_error_date_NaN(dataframe):
	errors_indices = np.random.choice(50, 5, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Date')]] = np.nan

def introduce_error_country():
	possible_countries = ['USA', 'uSa', 'Brasil', 'brUsil', 'France', 'Fr', 'South Africa', 'SAF', 'China', 'CHinA']
	countries_probabilities = [0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05]
	return possible_countries, countries_probabilities

def introduce_error_email():
	possible_suffixes = ['@gmail.com', '@hotmail.com', '@laposte.net', '@darkmagic', '@test.xxx', '@weneverknow.com']
	suffixes_probabilities = [0.41, 0.3, 0.2, 0.03, 0.03, 0.03]
	return possible_suffixes, suffixes_probabilities
