

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #visualizing data
import seaborn as sns

df = pd.read_csv('calorie_info.csv', encoding = 'unicode_escape')

df.shape

df.head()

df.info()

pd.isnull(df)

pd.isnull(df).sum()

df.describe()

df.dropna(inplace=True)