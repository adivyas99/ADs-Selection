# --Random Selection--

# 1. Importing the libraries--

import numpy as np
#For Numerical calculations

import matplotlib.pyplot as plt
# For Data Vizualization

import pandas as pd
# For Data Management

import random
# For Randoms in Selection

# 2. Importing the dataset--

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# 3. Implementing Random Selection--

N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward

# 4. Visualising the results--

plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()