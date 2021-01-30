"""

Author: Janith Weeraman
Date: 28/12/2020

Code to carry out a paired t-test on the effect of testosterone levels
of red-winged blackbirds and their effect on immunocompetence

"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st

birds = pd.read_csv('BlackbirdTestosterone.csv')

# Formatting dataframe to remove all columns except log before, log after and difference in logs values
# and rename variables
birds = pd.DataFrame(birds, columns=['log before', 'log after', 'dif in logs']) \
    .rename(columns={'log before': 'before', 'log after': 'after', 'dif in logs': 'difference'})

# Outputting the descriptive statistics for log values of before, after and log difference
print(birds.describe())

# Drawing histograms and qq plots for variable(s)
# Plotting two histograms
plt.hist(birds.before, color='green')
plt.hist(birds.after, color='red')
plt.legend(['log before', 'log after'])
plt.title("Histograms of 'log before' and 'log after' rates of antibody production")
plt.savefig('log_b4_aftr.jpg')
plt.close()

# plotting qq plots
sm.qqplot(birds.before)
plt.title("qq plot for 'log before' antibody production")
plt.savefig('qq_b4.jpg')
plt.close()
sm.qqplot(birds.after)
plt.title("qq plot for 'log after' antibody production")
plt.savefig('qq_aftr.jpg')
plt.close()

# Performing normality test (Shapiro-Wilk) on the length variables
print("For log before antibody levels:")
a = st.shapiro(birds.before)
print(f"P-value is {a[1]} which is", "> 0.05 so null hypothesis is not rejected" if a[1] > 0.05
else "< 0.05 so null hypothesis is rejected")
print()
print("For log after antibody levels:")
a = st.shapiro(birds.after)
print(f"P-value is {a[1]} which is", "> 0.05 so null hypothesis is not rejected" if a[1] > 0.05
else "< 0.05 so null hypothesis is rejected")
print()


# Plotting boxplots and violinplots for the variabe distributions
f, ((box1, box2), (viol1, viol2)) = plt.subplots(2, 2,sharey=True)
box1.boxplot(birds.before)
box1.set_title("Boxplot of 'log before' antibody production")
box2.boxplot(birds.after)
box2.set_title("Boxplot of for 'log after' antibody production")
viol1.violinplot(birds.before)
viol1.set_title("violinplot of 'log before' antibody production")
viol2.violinplot(birds.after)
viol2.set_title("violinplot of 'log after' antibody production")
plt.show()

# Carrying out non-parametric tests
print("Carrying out a Kruskal-Wallis H test on log antibody level data:")
t, p = st.kruskal(birds.before,birds.after)
print(f"P-value is : {p} which is", "> 0.05 so null hypothesis is not rejected" if p > 0.05
else "< 0.05 so null hypothesis is rejected")
print()