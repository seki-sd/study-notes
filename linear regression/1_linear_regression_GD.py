# ***********************************************
# Title: linear regression with GD
# Author : johnfarrell  
# Date   : 2016-01-01
# HomePage : github.com/john7farrell/
# Email  : xjz199273@163.com
# ***********************************************

import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

# year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
# 2009, 2010, 2011, 2012, 2013]
year = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
price = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704,
6.853, 7.971, 8.561, 10.000, 11.280, 12.900]
m = len(year)

# initialize
xx = mat(array(year))
xx = xx.T
x0 = mat(ones((m, 1)))
# print x0
xx = hstack((x0, xx))
# print xx

yy = mat(array(price))
yy = yy.T
# # xx is m*2 matrix   
# # yy is m*1  

# Hypothesis
def h(vx, theta):
	return vx * theta
	
# Cost function
def J(theta, vx, vy):
	J = float((vx * theta - vy).T * (vx * theta - vy)) / 2
	return J

# Gradient Descent
theta = mat([0, 0]).T

niters = 200
alpha = 0.033

J_history = mat(ones((niters, 1)))
for i in range(niters):
	error = xx * theta - yy
	theta = theta - alpha/m * xx.T * error
	print theta
	print("\n")
	J_history[i, :] = J(theta, xx, yy)
	print(J_history[i, :])
	print("\n")
	plt.scatter(year, price)
	plt.plot(year, xx * theta)

print("GD over\n")
print("\n\n\ncurrent theta: \n\n")
print(theta.T)
plt.show()

plt.scatter(year, price)
plt.plot(year, xx * theta)
plt.show()

x2014 = mat([1, 14])
y2014 = float(h(x2014, theta).T)

print "\n\n\nThe Hypothesis of price in 2014 is\n\n" + str(y2014) + " * 10^3 CHN\n\n"