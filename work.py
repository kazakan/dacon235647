
'''
Download data and set directory.
'''

# %%
!wget 'https://drive.google.com/uc?export=download&id=192fXQDhp84rtmb3HXvhd7TTpVeDOHv4P' -O data.zip
!unzip data.zip -d data

!ls

# %%
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn

PATH_TRAIN = "./data/train.csv"
PATH_TEST_X = "./data/test_x.csv"

'''
Lets See train data
'''

# %%
#load data
df_train = pd.read_csv(PATH_TRAIN)

# %%
df_train.top(10)

# %%
df_train.describe()



