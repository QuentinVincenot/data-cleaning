import pandas as pd
import numpy as np

def generate_dataset():
	dataframe = pd.DataFrame()
	dataframe["Date"] = generate_dates_column()
	return dataframe

def generate_dates_column():
	random_dates = np.random.randint(low=1950, high=2020, size=50)
	# TODO : introduce errors...
	return random_dates
