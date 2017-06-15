# ***********************************************
# Title: logistic regression
# Author : johnfarrell
# Date   : 2016-01-15
# Email  : xjz199273@163.com
# ***********************************************

# reference: machine learning in action

from numpy import array,log,zeros,mat,exp,arange,diagflat
import random
import matplotlib.pyplot as plt

#### DEF
def loadData():
	dataMat = []
	labelMat = []
	fr = open("ex4x.dat")
	# fr = open(r"D:\temp\Machine Learning\logistic regression\ex4Data\ex4x.dat")
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
	fr.close()
	fr = open("ex4y.dat")
	# fr = open(r"D:\temp\Machine Learning\logistic regression\ex4Data\ex4y.dat")
	for line in fr.readlines():
		lineArr = line.strip().split()
		temp = int(float(lineArr[0]))
		labelMat.append(temp)
	fr.close()
	return dataMat, labelMat
#

def sigmoid(z):
	return 1.0/(1+exp(-z))
#

def logLikelihoodEstimation(h, y):
	l = 1.0 * (y.T*log(h) + (1-y).T*log(1-h))
	return -l
#

def gradAscent(dataMatIn, classLabels, alpha, maxCycles):
	dataMatrix = mat(dataMatIn)
	labelMatrix = mat(classLabels).T
	m, n = dataMatrix.shape[0], dataMatrix.shape[1]
	weights = zeros((n,1)) ## theta
	cost = zeros((maxCycles, 1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix * weights)
		error = labelMatrix - h
		weights = weights + alpha * dataMatrix.T * error / m
		cost[k] = logLikelihoodEstimation(h, labelMatrix) / m
		if k%1000==0:print(cost[k])
	return weights, cost
#

def sticGradAscent(dataMatIn, classLabels, alpha, maxCycles):
	dataMatrix = array(dataMatIn)
	# labelMatrix = classLabels
	m,n = dataMatrix.shape[0], dataMatrix.shape[1]
	weights = zeros(n)
	# cost = zeros((m, 1))
	for j in range(maxCycles):
		dataIndex = range(m)
		for i in range(m):
			# alpha += 4/(1+j+i) ##
			randIndex = int(random.uniform(0, len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex] * weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex] / m
			del(dataIndex[randIndex])
			print(weights)
	return weights
#
def newton(dataMatIn, classLabels, maxCycles=7):
	dataMatrix = mat(dataMatIn)
	labelMatrix = mat(classLabels).T
	m, n = dataMatrix.shape[0], dataMatrix.shape[1]
	weights = zeros((n,1)) ## theta
	cost = zeros((maxCycles, 1))
	for i in range(maxCycles):
		h = sigmoid(dataMatrix * weights)
		grad = dataMatrix.T * (h-labelMatrix) / m
		hessian = dataMatrix.T * diagflat(h) * diagflat(1-h) * dataMatrix / m 
		cost[i] = logLikelihoodEstimation(h, labelMatrix) / m 
		print(cost[i]) 
		weights = weights - hessian.I * grad
	return weights, cost
#

def plotBestFit(weights, dataMat, labelMat):
	dataArr = array(dataMat)
	n = dataArr.shape[0]
	xcord1 = [];ycord1 = []
	xcord2 = [];ycord2 = []
	for i in range(n):
		if labelMat[i]==1:
			xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
		else:
			xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1, ycord1, s=30, c = 'red', marker = 'x')
	ax.scatter(xcord2, ycord2, s=30, c = 'green', marker = 'o')
	x = arange(15, 65, 0.1)
	y = (-weights[0]-weights[1] * x)/weights[2]
	ax.plot(x, y)
	plt.xlabel('X1');plt.ylabel('X2')
	plt.show()
#

#### END

dataMat, labelMat = loadData()

# print(dataMat)
# print(labelMat)
print("-------------"+"Data ready"+"-------------")

#### Newton's method

theta = [0, 0, 0]
theta, cost = newton(dataMat, labelMat)
theta = array(theta)
# print(type(theta))
print("\ncurrent theta is:\n")
print(theta)
plotBestFit(theta, dataMat, labelMat)
print("\nfinal cost is:\n")
print(cost[len(cost)-1])
plt.scatter(range(cost.shape[0]), cost)
plt.plot(range(cost.shape[0]), cost)
plt.xlabel('iters');plt.ylabel('cost function')
plt.show()

#### Newton END

#### Batch gradient ascent
## iterates too many, and no convergence, maybe there are some mistakes...
## NOT Recommended

# alpha = 0.00135 
# maxCycles = 2000000 
# # theta, cost = gradAscent(dataMat, labelMat, alpha, maxCycles)
# # print("after 2000000 iterations, theta is [[-15.77067   ] [  0.14373649] [  0.15259652]]")
# theta = array([-15.77067, 0.14373649, 0.15259652])
# print(theta)
# plotBestFit(theta, dataMat, labelMat)

#### Batch END

#### Stocastic gradient ascent
## somehow, too slow, also no convergence, maybe somethong is wrong...
# alpha = 0.004
# maxCycles = 40000
# theta = sticGradAscent(dataMat, labelMat, alpha, maxCycles)
## cost
# cost = 0
# dataMatrix = mat(dataMat)
# labelMatrix = mat(labelMat).T
# m = dataMatrix.shape[0]
# h = sigmoid(dataMatrix * mat(theta).T)
# cost = logLikelihoodEstimation(h, labelMatrix) / m
# print(cost)
# plotBestFit(theta, dataMat, labelMat)

#### Stocastic END
