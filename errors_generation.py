import pandas as pd
import numpy as np

def introduce_error_dates_NaN(dataframe):
	errors_indices = np.random.choice(50, 5, replace=False)
	dataframe.iloc[errors_indices, [0]] = np.nan
