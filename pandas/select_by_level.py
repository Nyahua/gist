import numpy as np
import pandas as pd
iterables = [['bar', 'baz', 'foo'], ['one', 'two']]
cols = pd.MultiIndex.from_product(iterables, names=['first', 'second'])

df = pd.DataFrame(data=np.random.randn(10, 6), columns=cols)
print("dataframe:\n*****************************************")
print(df)
print("\nselect level 1:\n*****************************************")
print(df.xs(key='one', level=1, axis=1))