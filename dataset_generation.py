from errors_generation import *
import random
import string

def generate_dataset(length=50):
	dataframe = pd.DataFrame()
	generate_name_column(dataframe, length)
	introduce_error_name_NaN(dataframe, length)
	generate_missing_column(dataframe, length)
	introduce_error_missing_NaN(dataframe, length)
	generate_category_column(dataframe, length)
	introduce_error_category_null_values(dataframe, length)
	generate_height_column(dataframe, length)
	introduce_error_height_NaN(dataframe, length)
	generate_salary_column(dataframe, length)
	introduce_error_salary_heterogeneous(dataframe, length)
	dates_array = introduce_error_date(dataframe, length)
	generate_date_column(dataframe, dates_array)
	countries, probas = introduce_error_country()
	generate_country_column(dataframe, length, countries, probas)
	suffixes, probas = introduce_error_email()
	generate_email_column(dataframe, length, suffixes, probas)
	generate_strange_column(dataframe, length)
	return dataframe

def generate_name_column(dataframe, length):
	most_common_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth',
		'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Margaret']
	dataframe["Name"] = np.random.choice(most_common_names, length)

def generate_missing_column(dataframe, length):
	dataframe["Missing"] = np.random.randint(low=0, high=100, size=length)

def generate_category_column(dataframe, length):
	dataframe["Category"] = np.random.choice(['Classic', 'Regular', 'Special'], length)

def generate_height_column(dataframe, length):
	dataframe["Height"] = np.round(np.random.uniform(low=1.45, high=2.10, size=length), 2)

def generate_salary_column(dataframe, length):
	dataframe["Salary"] = np.multiply(1000, np.random.randint(low=30, high=145, size=length))

def generate_date_column(dataframe, dates_array):
	dataframe["Date"] = dates_array

def generate_country_column(dataframe, length, countries, probas):
	dataframe["Country"] = np.random.choice(countries, length, p=probas)

def generate_email_column(dataframe, length, suffixes, probas):
	email_data_array = []
	for row in range(length):
		first_part = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
		second_part = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
		extension = ''.join(np.random.choice(suffixes, 1, p=probas))
		random_data = '{}.{}{}'.format(first_part, second_part, extension)
		email_data_array += [random_data]
	dataframe["Email"] = email_data_array

def generate_strange_column(dataframe, length):
	strange_data_array = []
	for row in range(length):
		random_data = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
		strange_data_array += [random_data]
	dataframe["Strange"] = strange_data_array
