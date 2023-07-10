         # Assignment 3 Stastics  Data Science 
# 1. Scenario: A company wants to analyze the sales performance of its products in different regions. They have collected the following data:
#    Region A: [10, 15, 12, 8, 14]
#    Region B: [18, 20, 16, 22, 25]
#    Calculate the mean sales for each region.

import statistics
 
Region_A=[10, 15, 12, 8, 14]
Region_B=[18, 20, 16, 22, 25]
 

print ("The average of Region A is  : ",end="")
print (statistics.mean(Region_A))
print ("The average of Region B is  : ",end="")
print (statistics.mean(Region_B))


# The average of Region A is  : 11.8
# The average of Region B is  : 20.2


# 2. Scenario: A survey is conducted to measure customer satisfaction on a scale of 1 to 5. The data collected is as follows:
# data=[4, 5, 2, 3, 5, 4, 3, 2, 4, 5]
#    Calculate the mode of the survey responses.

from statistics import mode
data=[4, 5, 2, 3, 5, 4, 3, 2, 4, 5]
print("Mode of data  is % s" % (mode(data)))

# Mode of data  is 4


# 3. Scenario: A company wants to compare the salaries of two departments. The salary data for Department A and Department B are as follows:
#    Department A: [5000, 6000, 5500, 7000]
#    Department B: [4500, 5500, 5800, 6000, 5200]
#    Calculate the median salary for each department.

import statistics  
   
Department_A=[5000, 6000, 5500, 7000]
  
Department_B=[4500, 5500, 5800, 6000, 5200] 
    
print("Median salary of Department A is % s" % statistics.median(Department_A))  
print("Median salary of Department B is % s" % statistics.median(Department_B)) 


# Median salary of Department A is 5750.0
# Median salary of Department B is 5500


# 4. Scenario: A data analyst wants to determine the variability in the daily stock prices of a company. 
# The data collected is as follows:
#  li= [25.5, 24.8, 26.1, 25.3, 24.9]
#  Calculate the range of the stock prices.


def range_stock_price(li):
    n_min = min(li)
    n_max = max(li)
    n_range = n_max - n_min
    return n_min, n_max, n_range
li=[25.5, 24.8, 26.1, 25.3, 24.9]    
result=range_stock_price(li)
print("Range of stock price is ",result)

# Range of stock price is  (24.8, 26.1, 1.3000000000000007)


# 5. Scenario: A study is conducted to compare the performance of two different teaching methods. 
# The test scores of the students in each group are as follows:
#    Group A: [85, 90, 92, 88, 91]
#    Group B: [82, 88, 90, 86, 87]
#    Perform a t-test to determine if there is a significant difference in the
#  mean scores between the two groups.

from scipy import stats

Group_A = [85, 90, 92, 88, 91]
Group_B = [82, 88, 90, 86, 87]

t_statistic, p_value = stats.ttest_ind(Group_A, Group_B)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

# T-statistic: 1.4312528946642733
# P-value: 0.19023970239078333


#6 Scenario: A company wants to analyze the relationship between advertising expenditure and sales.
#  The data collected is as follows:
#  Advertising Expenditure (in thousands): [10, 15, 12, 8, 14]
#  Sales (in thousands): [25, 30, 28, 20, 26]
#  Calculate the correlation coefficient between advertising expenditure and sales.
import numpy as np

advertising_expenditure = np.array([10, 15, 12, 8, 14])

sales = np.array([25, 30, 28, 20, 26])

correlation_coefficient = np.corrcoef(advertising_expenditure, sales)[0, 1]

print("Correlation Coefficient:", correlation_coefficient)

#Correlation Coefficient: 0.8757511375750132


# 7. Scenario: A survey is conducted to measure the heights of a group of people.
#  The data collected is as follows:
#  heights=  [160, 170, 165, 155, 175, 180, 170]
#    Calculate the standard deviation of the heights.

import statistics

heights = [160, 170, 165, 155, 175, 180, 170]

sd = statistics.stdev(heights)


print("Standard Deviation:", sd)

 # Standard Deviation: 8.591246929842246



#8. Scenario: A company wants to analyze the relationship between employee tenure and job satisfaction. 
# The data collected is as follows:
#    Employee Tenure (in years): [2, 3, 5, 4, 6, 2, 4]
#    Job Satisfaction (on a scale of 1 to 10): [7, 8, 6, 9, 5, 7, 6]
#    Perform a linear regression analysis to predict job satisfaction based on employee tenure.

import statsmodels.api as sm
import numpy as np

tenure = np.array([2, 3, 5, 4, 6, 2, 4])

satisfaction = np.array([7, 8, 6, 9, 5, 7, 6])

X = sm.add_constant(tenure)

model = sm.OLS(satisfaction, X)
results = model.fit()

print("Intercept:", results.params[0])
print("Slope (Tenure):", results.params[1])

# Intercept: 8.595744680851062
# Slope (Tenure): -0.46808510638297934


# 9. Scenario: A study is conducted to compare the effectiveness of two different medications. 
# The recovery times of the patients in each group are as follows:
#    Medication A: [10, 12, 14, 11, 13]
#    Medication B: [15, 17, 16, 14, 18]
#    Perform an analysis of variance (ANOVA) to determine if there is a significant
#     difference in the mean recovery times between the two medications.


from scipy import stats

medication_a = [10, 12, 14, 11, 13]
medication_b = [15, 17, 16, 14, 18]

f_stats, p_value = stats.f_oneway(medication_a, medication_b)

print("F-statistic:", f_stats)
print("P-value:", p_value)

# F-statistic: 16.0
# P-value: 0.003949772803445326

# 10. Scenario: A company wants to analyze customer feedback ratings on a scale of 1 to 10.
#  The data collected is as follows:
#  ratings= [8, 9, 7, 6, 8, 10, 9, 8, 7, 8]
#  Calculate the 75th percentile of the feedback ratings.

import numpy as np

ratings = np.array([8, 9, 7, 6, 8, 10, 9, 8, 7, 8])

percentile_75 = np.percentile(ratings, 75)

print("75th Percentile:", percentile_75)

# 75th Percentile: 8.75


# 11. Scenario: A quality control department wants to test the weight consistency of a product.
#  The weights of a sample of products are as follows:
#     [10.2, 9.8, 10.0, 10.5, 10.3, 10.1]
#     Perform a hypothesis test to determine if the mean weight differs significantly from 10 grams.

from scipy import stats

weights = [10.2, 9.8, 10.0, 10.5, 10.3, 10.1]

t_stats, p_value = stats.ttest_1samp(weights, 10)

print("T-test:", t_stats)
print("P-value:", p_value)


# T-statistic: 1.5126584522688367
 # P-value: 0.19077595151110102


#  12. Scenario: A company wants to analyze the click-through rates of two different website designs.
#   The number of clicks for each design is as follows:
#     Design A: [100, 120, 110, 90, 95]
#     Design B: [80, 85, 90, 95, 100]
#     Perform a chi-square test to determine if there is a significant difference in the
#      click-through rates between the two designs.

from scipy import stats
design_a = [100, 120, 110, 90, 95]
design_b = [80, 85, 90, 95, 100]

chi2_statistic, p_value = stats.chisquare([design_a, design_b])

print("Chi-square Statistic:", chi2_statistic)
print("P-value:", p_value)

# Chi-square Statistic: [2.22222222 5.97560976 2.         0.13513514 0.12820513]
# P-value: [0.13603713 0.01450507 0.15729921 0.71316606 0.72030033]

# 13. Scenario: A survey is conducted to measure customer satisfaction with a product on a scale of 1 to 10.
#  The data collected is as follows:
# scores=[7, 9, 6, 8, 10, 7, 8, 9, 7, 8]
#     Calculate the 95% confidence interval for the population mean satisfaction score.

from scipy import stats
import numpy as np
scores = np.array([7, 9, 6, 8, 10, 7, 8, 9, 7, 8])

confidence_interval = stats.t.interval(0.95, len(scores)-1, loc=np.mean(scores), scale=stats.sem(scores))

print("95% Confidence Interval:", confidence_interval)

# 95% Confidence Interval: (7.043561120599888, 8.756438879400113)


# 14. Scenario: A company wants to analyze the effect of temperature on product performance.
#  The data collected is as follows:
#     Temperature (in degrees Celsius): [20, 22, 23, 19, 21]
#     Performance (on a scale of 1 to 10): [8, 7, 9, 6, 8]
#     Perform a simple linear regression to predict performance based on temperature.

import statsmodels.api as sm
import numpy as np

temperature = np.array([20, 22, 23, 19, 21])

performance = np.array([8, 7, 9, 6, 8])

X = sm.add_constant(temperature)

model = sm.OLS(performance, X)
results = model.fit()

print("Intercept:", results.params[0])
print("Slope (Temperature):", results.params[1])

# Intercept: -2.899999999999972
# Slope (Temperature): 0.49999999999999867

# 15. Scenario: A study is conducted to compare the preferences of two groups of participants.
#  The preferences are measured on a Likert scale from 1 to 5. The data collected is as follows:
#  Group A: [4, 3, 5, 2, 4]
#  Group B: [3, 2, 4, 3, 3]
#  Perform a Mann-Whitney U test to determine if there is a significant difference in the median
#  preferences between the two groups.

from scipy import stats

group_a = [4, 3, 5, 2, 4]
group_b = [3, 2, 4, 3, 3]

statistic, p_value = stats.mannwhitneyu(group_a, group_b)

print("Test Statistic (U):", statistic)
print("P-value:", p_value)

# Test Statistic (U): 17.0
# P-value: 0.380836480306712

# 16. Scenario: A company wants to analyze the distribution of customer ages.
# The data collected is as follows:
# ages= [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
# Calculate the interquartile range (IQR) of the ages
import numpy as np

ages = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

iqr = np.percentile(ages, 75) - np.percentile(ages, 25)

print("Interquartile Range (IQR):", iqr)

# Interquartile Range (IQR): 22.5

# 17. Scenario: A study is conducted to compare the performance of three different machine learning algorithms.
#  The accuracy scores for each algorithm are as follows:
#  Algorithm A: [0.85, 0.80, 0.82, 0.87, 0.83]
#  Algorithm B: [0.78, 0.82, 0.84, 0.80, 0.79]
#  Algorithm C: [0.90, 0.88, 0.89, 0.86, 0.87]
#  Perform a Kruskal-Wallis test to determine if there is a significant difference in the median
#  accuracy scores between the algorithms.


from scipy import stats


algorithm_a = [0.85, 0.80, 0.82, 0.87, 0.83]
algorithm_b = [0.78, 0.82, 0.84, 0.80, 0.79]
algorithm_c = [0.90, 0.88, 0.89, 0.86, 0.87]


statistic, p_value = stats.kruskal(algorithm_a, algorithm_b, algorithm_c)

print("Test Statistic:", statistic)
print("P-value:", p_value)


# 18. Scenario: A company wants to analyze the effect of price on sales. 
# The data collected is as follows:
# Price (in dollars): [10, 15, 12, 8, 14]
# Sales: [100, 80, 90, 110, 95]
# Perform a simple linear regression to predict sales based on price.

import statsmodels.api as sm
import numpy as np

price = np.array([10, 15, 12, 8, 14])

sales = np.array([100, 80, 90, 110, 95])

X = sm.add_constant(price)

model = sm.OLS(sales, X)
results = model.fit()

print("Intercept:", results.params[0])
print("Slope (Price):", results.params[1])

# Intercept: 136.3719512195122
# Slope (Price): -3.5060975609756113

# 19. Scenario: A survey is conducted to measure the satisfaction levels of customers with a new product.
#  The data collected is as follows:
#  scores=[7, 8, 9, 6, 8, 7, 9, 7, 8, 7]
#  Calculate the standard error of the mean satisfaction score.

import scipy.stats as stats
import numpy as np

scores = np.array([7, 8, 9, 6, 8, 7, 9, 7, 8, 7])

standard_error = stats.sem(scores)

print("Standard Error of the Mean:", standard_error)

# Standard Error of the Mean: 0.30550504633038933

# 20. Scenario: A company wants to analyze the relationship between advertising expenditure and sales.
# The data collected is as follows:
# Advertising Expenditure (in thousands): [10, 15, 12, 8, 14]
# Sales (in thousands): [25, 30, 28, 20, 26]
# Perform a multiple regression analysis to predict sales based on advertising expenditure.


