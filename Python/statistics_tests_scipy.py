"""
Author: Janith Weeraman
Date: 8/12/2020

Code that does statistics stuff! ¯\_(ツ)_/¯
"""

from scipy import stats as st
import matplotlib.pyplot as plt
# import seaborn as sb
import pandas as pd
import statsmodels.api as sm

# Plot descriptive statistics for temperature values
temps = pd.read_csv('Temperature.csv')
print(temps.describe())

# Plot histogram of temperature values
plot1 = plt.hist(temps)
plt.title("Histogram for temperatures")
plt.savefig('1.jpg')

# Drawing qqplot
plot2 = sm.qqplot(temps)
plt.title("Quantile-Quantile plot for temperatures")
plt.savefig('2.jpg')

print()
# Testing for normality
a = st.shapiro(temps)
print("P-value is : ", a[1], " which is > 0.05 so null hypothesis is not rejected")
print()

# Carrying out a 1-sample t-test and printing the result
t, p = st.ttest_1samp(temps, 98.7)
print('p: ', p, '\n', 't: ', t)
