import pandas as pd
import numpy as np
import math

def introduce_error_name_NaN(dataframe, length, name_errors):
	number_of_errors = math.floor(round(name_errors*length, 0))
	errors_indices = np.random.choice(length, number_of_errors, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Name')]] = np.nan

def introduce_error_missing_NaN(dataframe, length, missing_errors):
	number_of_errors = math.floor(round(missing_errors*length, 0))
	errors_indices = np.random.choice(length, number_of_errors, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Missing')]] = np.nan

def introduce_error_category_null_values(dataframe, length, category_errors):
	number_of_errors = math.floor(round(category_errors*length, 0))
	errors_indices = np.random.choice(length, number_of_errors, replace=False)
	for index in errors_indices:
		dataframe.iloc[index, [dataframe.columns.get_loc('Category')]] = np.random.choice(['NaN', 'null', '???', 'UNKWN'], 1, p=[0.25, 0.25, 0.25, 0.25])[0]

def introduce_error_height_NaN(dataframe, length, height_errors):
	number_of_errors = math.floor(round(height_errors*length, 0))
	errors_indices = np.random.choice(length, number_of_errors, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Height')]] = np.nan

def introduce_error_salary_heterogeneous(dataframe, length, salary_errors):
	number_of_errors = math.floor(round(salary_errors*length, 0))
	errors_indices = np.random.choice(length, number_of_errors, replace=False)
	dataframe.iloc[errors_indices, [dataframe.columns.get_loc('Salary')]] = np.multiply(1000, np.random.randint(low=450, high=500, size=number_of_errors))

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
