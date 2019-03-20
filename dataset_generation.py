from errors_generation import *
import random
import string

def generate_dataset():
	dataframe = pd.DataFrame()
	generate_missing_column(dataframe)
	introduce_error_missing_NaN(dataframe)
	generate_category_column(dataframe)
	introduce_error_category_NaN(dataframe)
	generate_height_column(dataframe)
	introduce_error_height_NaN(dataframe)
	generate_date_column(dataframe)
	introduce_error_date_NaN(dataframe)
	countries, probas = introduce_error_country()
	generate_country_column(dataframe, countries, probas)
	suffixes, probas = introduce_error_email()
	generate_email_column(dataframe, suffixes, probas)
	generate_useless_column(dataframe)
	return dataframe

def generate_missing_column(dataframe):
	dataframe["Missing"] = np.random.randint(low=0, high=100, size=50)

def generate_category_column(dataframe):
	dataframe["Category"] = np.random.choice(['Classic', 'Regular', 'Special'], 50)

def generate_height_column(dataframe):
	dataframe["Height"] = np.round(np.random.uniform(low=1.45, high=2.10, size=50), 2)

def generate_date_column(dataframe):
	dataframe["Date"] = np.random.randint(low=1950, high=2020, size=50)

def generate_country_column(dataframe, countries, probas):
	dataframe["Country"] = np.random.choice(countries, 50, p=probas)

def generate_email_column(dataframe, suffixes, probas):
	email_data_array = []
	for row in range(50):
		first_part = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
		second_part = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
		extension = ''.join(np.random.choice(suffixes, 1, p=probas))
		random_data = '{}.{}{}'.format(first_part, second_part, extension)
		email_data_array += [random_data]
	dataframe["Email"] = email_data_array

def generate_useless_column(dataframe):
	useless_data_array = []
	for row in range(50):
		random_data = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
		useless_data_array += [random_data]
	dataframe["Useless"] = useless_data_array
