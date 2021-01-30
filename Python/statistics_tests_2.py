"""
Author: Janith Weeraman
Date: 8/12/2020

Code that does *even more* statistics stuff! ¯\_(ツ)_/¯
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats as st

# Load csv into a dataframe and drop any rows without a length value
liz = pd.read_csv('HornedLizards.csv').dropna(axis=0)

# Change "Squamosal horn length" to length to preserve sanity when writing the rest of this
liz = liz.rename(columns={'Squamosal horn length': 'length'})

# Printing descriptive statistics for horned lizard horn lengths
print(liz.describe())

survived = liz.loc[liz['Survive'] == 'survived']['length']
dead = liz.loc[liz['Survive'] == 'dead']['length']

# Plotting two histograms
plt.hist(survived, color='green')
plt.hist(dead, color='red')
plt.legend(['survived lizards', 'dead lizards'])
plt.title('Histograms of living and dead lizard horn lengths')
plt.savefig('lizard_hists.jpg')
plt.close()

# plotting qq plots
qq_survived = sm.qqplot(survived)
plt.title("qq plot for horn length of horned of living horned lizards")
plt.savefig('qq_living.jpg')
plt.close()
qq_dead = sm.qqplot(dead)
plt.title("qq plot for horn length of horned of dead horned lizards")
plt.savefig('qq_dead.jpg')
plt.close()

# Performing normality test (Shapiro-Wilk) on the length variables
print("For Living lizards:")
a = st.shapiro(survived)
print(f"P-value is {a[1]} which is", "> 0.05 so null hypothesis is not rejected" if a[1] > 0.05
else "< 0.05 so null hypothesis is rejected")
print()
print("For Dead lizards:")
a = st.shapiro(dead)
print(f"P-value is {a[1]} which is", "> 0.05 so null hypothesis is not rejected" if a[1] > 0.05
else "< 0.05 so null hypothesis is rejected")
print()

# Plotting boxplots and violinplots for the variabe distributions
f, ((box1, box2), (viol1, viol2)) = plt.subplots(2, 2,sharey=True)
box1.boxplot(survived)
box1.set_title("Boxplot of survived lizards horn length")
box2.boxplot(dead)
box2.set_title("Boxplot of dead lizards horn length")
viol1.violinplot(survived)
viol1.set_title("violinplot of survived lizards horn length")
viol2.violinplot(survived)
viol2.set_title("violinplot of dead lizards horn length")
plt.savefig("box & violin plots")

# Carrying out non-parametric tests
print("Carrying out a Kruskal-Wallis H test on the horned lizard length data:")
t, p = st.kruskal(survived,dead)
print(f"P-value is : {p} which is", "> 0.05 so null hypothesis is not rejected" if p > 0.05
else "< 0.05 so null hypothesis is rejected")
print()