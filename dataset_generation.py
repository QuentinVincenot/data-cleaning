from errors_generation import *
import random
import string

def generate_dataset():
	dataframe = pd.DataFrame()
	generate_dates_column(dataframe)
	introduce_error_dates_NaN(dataframe)
	generate_useless_column(dataframe)
	return dataframe

def generate_dates_column(dataframe):
	dataframe["Date"] = np.random.randint(low=1950, high=2020, size=50)

def generate_useless_column(dataframe):
	useless_data_array = []
	for row in range(50):
		random_data = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
		useless_data_array += [random_data]
	dataframe["Useless"] = useless_data_array
