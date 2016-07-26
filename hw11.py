
"""
Financial Engeneering and Risk Management - Part I
Homework 1
"""

__author__ = 'Antonio Giannino'
__email__ = 'antonio.giannino@gmail.com'

def geom_series(z, a, b):
    return (z**a - z**(b+1)) / (1-z)

def d(t1=0, t2=1, r=0.1, n=1, spot=None):
    if not spot:
        return (1+r/n) ** (-(t2-t1)*n)
    else:
        return (1+spot[t2-1]) ** (-t2)

def f_t1t2(t1, t2, s1, s2):
    return ((1+s2)**t2 / (1+s1)**t1) ** (1/(t2-t1)) - 1

# 1. Lottery payments
# A major lottery advertises that it pays the winner $10 million. However this 
# prize money is paid at the rate of $500,000 each year (with the first payment
# being immediate) for a total of 20 payments. What is the present value of 
# this prize at 10% interest compounded annually? Report your answer in 
# $millions, rounded to two decimal places. So, for example, if you compute the 
# answer to be 5.7124 million dollars then you should submit an answer of 5.71.
cf = 500000
t = 20
pv = cf * geom_series(z=d(t1=0, t2=1, r=0.1, n=1), a=0, b=t-1)

print('Q1: {:0.2f}'.format(round(pv/10**6, 2)))


# 2. Sunk Costs (Exercise 2.6 in Luenberger)
# A young couple has made a deposit of the first month's rent (equal to $1,000)
# on a 6-month apartment lease. The deposit is refundable at the end of six
# months if they stay until the end of the lease. The next day they find a
# different apartment that they like just as well, but its monthly rent is only
# $900. And they would again have to put a deposit of $900 refundable at the 
# end of 6 months. They plan to be in the apartment only 6 months. Should they 
# switch to the new apartment? Assume an (admittedly unrealistic!) interest
# rate of 12% per month compounded monthly.

# case 1
cf1 = -1000
cf2 = -900
r = 0.12
t = 6
pv1 = cf1 * geom_series(z=1/(1+r), a=0, b=t-1) + (-cf1)/(1+r)**t
pv2 = cf2 + cf2 * geom_series(z=1/(1+r), a=0, b=t-1) + (-cf2)/(1+r)**t
if pv1 > pv2:
	print('Q2: Stay')
else:
	print('Q2: Leave')

# 3. Relation between spot and discount rates
# Suppose the spot rates for 1 and 2 years are s1=6.3% and s2=6.9% with annual 
# compounding. Recall that in this course interest rates are always quoted on 
# an annual basis unless otherwise specified. What is the discount rate d(0,2)?
# Please submit your answer rounded to three decimal places. So, for example, 
# if your answer is 0:4567 then you should submit an answer of 0:457.
print('Q3: {:f}'.format(d(t2=2, spot=[0.063, 0.069])))


# 4. Relation between spot and forward rates
# Suppose the spot rates for 1 and 2 years are s1=6.3% and s2=6.9% with annual 
# compounding. Recall that in this course
# interest rates are always quoted on an annual basis unless otherwise 
# specified. What is the forward rate, f1,2 assuming annual compounding? Please
# submit your answer as a percentage rounded to one decimal place so, for 
# example, if your answer is 8.789% then you should submit an answer of 8.8.
print('Q4: {:0.1f}%'.format(round(f_t1t2(t1=1, t2=2, s1=0.063, s2=0.069)*100, 1)))


# 5. Forward contract on a stock
# The current price of a stock is $400 per share and it pays no dividends.
# Assuming a constant interest rate of 8% per year compounded quarterly, what 
# is the stock's theoretical forward price for delivery in 9 months? Please 
# submit your answer rounded to two decimal places so for example, if your 
# answer is 567.1234 then you should submit an answer of 567.12
r = 0.08
n = 3
S0 = 400.0
print('Q5: {:0.2f}'.format(round(S0*(1+r)**3, 2)))

# 6. Bounds using different lending and borrowing rate
# Suppose the borrowing rate rB=10% compounded annually. However, the lending
# rate (or equivalently, the interest rate on deposits) is only 8% compounded
# annually. Compute the difference between the upper and lower bounds on the
# price of an perpetuity that pays A=10,000$ per year. Please submit your 
# answer rounded to the nearest dollar so if your answer is 23,456.789 then you 
# should submit an answer of 23457.
rB = 0.10
rL = 0.08
A = 10000
print('Q6: {:0.0f}'.format(round(A/rL-A/rB, 1)))

# 7. Value of a Forward contract at an intermediate time
# Suppose we hold a forward contract on a stock with expiration 6 months from
# now. We entered into this contract 6 months ago so that when we entered into
# the contract, the expiration was T=1 year. The stock price$ 6 months ago was
# S0=100, the current stock price is 125 and the current interest rate is r=10%
# compounded semi-annually. (This is the same rate that prevailed 6 months 
# ago.) What is the current value of our forward contract? Please submit your 
# answer in dollars rounded to one decimal place so if your answer is 42.678 
# then you should submit an answer of 42.7.
S0 = 100.0
St = 125.0
r = 0.1
n = 2
F0 = S0/d(0, 1, r, n)
ft = St - F0*d(0.5, 1, r, n)
print('Q7: {:0.1f}'.format(round(ft, 1)))