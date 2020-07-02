#I'll be exploring different features in this file

import pandas as pd 
import string
from matplotlib import pyplot
import numpy as np

%matplotlib inline


data = pd.read_csv("data.rated-only.csv")

pyplot.hist(data['stance'], bins)
pyplot title("Stance")
pyplot.show()


print(data.head())