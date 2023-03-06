import pandas as pd
import numpy as np
from pandas import DataFrame

random_data = np.random.randn(10, 5)
column_names = ["a", "b", "c", "d", "e"]

our_dataframe = DataFrame(random_data, columns=column_names)

print(our_dataframe["a"])