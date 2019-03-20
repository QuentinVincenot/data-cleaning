from errors_generation import *
import random
import string

def generate_dataset():
	dataframe = pd.DataFrame()
	generate_category_column(dataframe)
	introduce_error_category_NaN(dataframe)
	generate_height_column(dataframe)
	introduce_error_height_NaN(dataframe)
	generate_date_column(dataframe)
	introduce_error_date_NaN(dataframe)
	countries, probas = introduce_error_country(dataframe)
	generate_country_column(dataframe, countries, probas)
	generate_useless_column(dataframe)
	return dataframe

def generate_category_column(dataframe):
	dataframe["Category"] = np.random.choice(['Classic', 'Regular', 'Special'], 50)

def generate_height_column(dataframe):
	dataframe["Height"] = np.round(np.random.uniform(low=1.45, high=2.10, size=50), 2)

def generate_date_column(dataframe):
	dataframe["Date"] = np.random.randint(low=1950, high=2020, size=50)

def generate_country_column(dataframe, countries, probas):
	dataframe["Country"] = np.random.choice(countries, 50, p=probas)

def generate_useless_column(dataframe):
	useless_data_array = []
	for row in range(50):
		random_data = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
		useless_data_array += [random_data]
	dataframe["Useless"] = useless_data_array
