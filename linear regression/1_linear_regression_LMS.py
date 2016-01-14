import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
2009, 2010, 2011, 2012, 2013]
price = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704,
6.853, 7.971, 8.561, 10.000, 11.280, 12.900]
n = len(year)

# price1 = []
# for i in price: 
	# i *= 1000
	# price1.append(i)

# price = price1

# print n
xx = mat(array(year))
xx = xx.T
x0 = mat(ones((n, 1)))
# print x0
xx = hstack((x0, xx))
print xx

yy = mat(array(price))
yy = yy.T
# # xx is m*2 matrix   
# # xy is m*1  

# # so that theta must be 2*1 matrix  

# Hypothesis
def h(vx, theta):
# # theta is 2*1 matrix 
	return vx * theta
# Normal Equation (ordinary least squares)
def LMS(vx, vy): 
# # vx is m*2  
# # vy is m*1   
	return (vx.T * vx).I * vx.T * vy
# Cost function
def J(theta, vx, vy):
	J = float((vx * theta - vy).T * (vx * theta - vy)) / 2
	return J

theta = LMS(xx, yy)
print(theta)

yh = h(xx, theta)
print(yh)
print("\nThe cost of LMS method is \n")
print(J(theta, xx, yy))
plt.scatter(year, price)
plt.plot(year, yh)
plt.show()

x2014 = mat([1, 2014])
y2014 = float(h(x2014, theta).T)

print("\nThe Hypothesis of price in 2014 is\n\n" + str(y2014) + " * 10^3 CHN\n\n")

# Tests
# theta0 = mat([0, 0]).T
# print(yy)
# print(type(yy))
