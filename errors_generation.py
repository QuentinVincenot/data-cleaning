import pandas as pd
import numpy as np

def introduce_error_name_NaN(dataframe, length):
	errors_indices = np.random.choice(length, 20, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Name')]] = np.nan

def introduce_error_missing_NaN(dataframe, length):
	errors_indices = np.random.choice(length, 38, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Missing')]] = np.nan

def introduce_error_category_null_values(dataframe, length):
	errors_indices = np.random.choice(length, 12, replace=False)
	for index in errors_indices:
		dataframe.iloc[index, [dataframe.columns.get_loc('Category')]] = np.random.choice(['NaN', 'null', '???', 'UNKWN'], 1, p=[0.25, 0.25, 0.25, 0.25])[0]

def introduce_error_height_NaN(dataframe, length):
	errors_indices = np.random.choice(length, 7, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Height')]] = np.nan

def introduce_error_salary_heterogeneous(dataframe, length):
	errors_indices = np.random.choice(length, 3, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Salary')]] = np.multiply(1000, np.random.randint(low=450, high=500, size=3))

def introduce_error_date(dataframe, length):
	years = np.random.randint(low=1950, high=2020, size=length)
	months = np.random.randint(low=1, high=12, size=length)
	days = np.random.randint(low=1, high=30, size=length)
	dates_array = []
	for i in range(length):
		date_string = '{} {}-{}'.format(months[i], years[i], days[i])
		dates_array += [date_string]
	return dates_array

def introduce_error_country():
	possible_countries = ['USA', 'uSa', 'Brasil', 'brUsil', 'France', 'Fr', 'South Africa', 'SAF', 'China', 'CHinA']
	countries_probabilities = [0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05, 0.15, 0.05]
	return possible_countries, countries_probabilities

def introduce_error_email():
	possible_suffixes = ['@gmail.com', '@hotmail.com', '@laposte.net', '@darkmagic', '@test.xxx', '@weneverknow.com']
	suffixes_probabilities = [0.41, 0.3, 0.2, 0.03, 0.03, 0.03]
	return possible_suffixes, suffixes_probabilities
