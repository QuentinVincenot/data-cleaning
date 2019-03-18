from errors_generation import *

def generate_dataset():
	dataframe = pd.DataFrame()
	generate_dates_column(dataframe)
	introduce_error_dates_NaN(dataframe)
	return dataframe

def generate_dates_column(dataframe):
	dataframe["Date"] = np.random.randint(low=1950, high=2020, size=50)
