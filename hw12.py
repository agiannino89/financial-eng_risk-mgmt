
"""
Financial Engeneering and Risk Management - Part I
Homework 2
"""

__author__ = 'Antonio Giannino'
__email__ = 'antonio.giannino@gmail.com'

import numpy as np

def d(t1=0, t2=1, r=0.1, n=1, spot=None):
    if not spot:
        return (1+r/n) ** (-(t2-t1)*n)
    else:
        return (1+spot[t2-1]) ** (-t2)

# Term structure of interest rates and swap valuation
# Suppose the current term structure of interest rates, assuming annual 
# compounding, is as follows:   
#  	  s1	 s2	 	 s3	 	 s4		 s5	 	 s6
#    7.0%	7.3%	7.7%	8.1%	8.4%	8.8%
# What is the discount rate d(0,4)? (Recall that interest rates are always quoted 
# on an annual basis unless stated otherwise.)
# Please submit your answer rounded to three decimal places. So for example, if
# your answer is 0.4567 then you should submit an answer of 0.457.

r=[7.,7.3,7.7,8.1,8.4,8.8]
r = [i/100. for i in r]
t = 4
print('Q1: %5.3f' %d(t1=0, t2=t, r=r[t-1]))

# Swap Rates
# Suppose a 6-year swap with a notional principal of $10 million is being
# configured. What is the fixed rate of interest that will make the value
# of the swap equal to zero. (You should use the term structure of interest 
# rates from Question 1.)
# Please submit your answer as a percentage rounded to two decimal places. So 
# for example, if your answer is 4.567% or equivalently 0.04567, then you 
# should submit an answer of 4.57.

T = 6
d = [d(t1=0, t2=i+1, r=ir) for i,ir in enumerate(r)]
X = (1-d[-1])/sum(d)

print('Q2: %5.2f' %(X*100))


# Hedging using futures
# Suppose a farmer is expecting that her crop of oranges will be ready for
# harvest and sale as 150,000 pounds of orange juice in 3 months time. Suppose
# each orange juice futures contract is for 15,000 pounds of orange juice, and
# the current futures price is F0=118.65 cents-per-pound.
# Assuming that the farmer has enough cash liquidity to fund
# any margin calls, what is the risk-free price that she can guarantee herself.
# Please submit your answer in cents-per-pound rounded to two decimal places. 
# So for example, if your answer is 123.456, then you should submit an answer 
# of 123.47.

print('Q3: 118.65')

# Minimum variance hedge
# Suppose a farmer is expecting that her crop of grapefruit will be ready for
# harvest and sale as 150,000 pounds of grapefruit juice in 3 months time. She
# would like to use futures to hedge her risk but unfortunately there are no 
# futures contracts on grapefruit juice. Instead she will use orange juice 
# futures. Suppose each orange juice futures contract is for 15,000 pounds of
# orange juice and the current futures price is F0=118.65 cents-per-pound.
# The volatility, i.e. the standard deviation, of the prices of
# orange juice and grape fruit juice is 20% and 25%, respectively,
# and the correlation coefficient is 0.7. What is the approximate number
# of contracts she should purchase to minimize the variance of her payoff?
# Please submit your answer rounded to the nearest integer. So for example, if
# your calculations result in 10.78 contracts you should submit an answer of 11.

F = 0.20
S = 0.25
P = 0.7
QA = 150000
QF = 150000
C = 15000

h = P*S/F
y = h*QA/QF


print('Q4: %5.3f' %(round(y*10,0)))

# Call Options
# Consider a 1-period binomial model with R=1.02, S0=100, u=1/d=1.05. Compute
# the value of a European call option on the stock with strike K=102. The stock
# does not pay dividends.
# Please submit your answer rounded to two decimal places. So for example, if
# your answer is 3.4567 then you should submit an answer of 3.46.

R = 1.02
S0 = 100
u = 1.05
d = 1/u 
K = 102

if u*S0-K > 0:
	Cu = u*S0 - K
else:
	Cu = 0

if d*S0-K > 0:
	Cd = d*S0 - K
else:
	Cd = 0

q = (R-d)/(u-d)
C0 = 1/R*(q*Cu+(1-q)*Cd)

print('Q5: %5.2f' %C0)

# Call Options II
# When you construct the replicating portfolio for the option in the previous
# question how many dollars do you need to invest in the cash account?
# Please submit your answer rounded to three decimal places. So for example, if
# your answer is -43.4567 then you should submit an answer of -43.457.

A = np.matrix('%s, %s; %s, %s' %(u*S0, R, d*S0, R))
b = np.matrix('%s; %s' %(Cu,Cd))
x = np.linalg.inv(A)*b
print('Q6: %s' %(x[1]))

