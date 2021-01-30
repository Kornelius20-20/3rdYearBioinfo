"""

Author: Janith Weeraman
Date: 28/12/2020

Code to carry out a chi-square contingency test on the effect of parasite load of
killifish on the likelihood of getting eaten by birds

"""

import pandas as pd
import statsmodels.graphics.mosaicplot as mosaicplot
import matplotlib.pyplot as plt
import scipy.stats as stat

# Creating a Dataframe from the data and printing it
fish = pd.DataFrame([[1,10,37],[49,35,9]],index=['eaten','not_eaten'],columns=['uninfected','light_infection',
                                                                               'heavy_infection'])
print(fish)
print()

# Output a mosaicplot for the dataframe
mosaicplot.mosaic(fish.stack())
plt.savefig("fish_mosaic.png")

# Carry out a chi-square contingency test on the data
chi2,p,dof,expected = stat.chi2_contingency(fish)
print(f"chi-square statistic: {chi2}\np-value: {p}\nDegree of freedom: {dof}\n")

expected = pd.DataFrame(expected)
print(expected)