# ***********************************************
# Title: logistic regression
# Author : johnfarrell
# Date   : 2016-01-15
# HomePage : github.com/john7farrell/
# Email  : xjz199273@163.com
# ***********************************************

# reference(with very little difference): machine learning in action 5.1

from numpy import *
import random
import matplotlib.pyplot as plt

#### DEF
def loadData():
	dataMat = []; labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat
#

def sigmoid(z):
	return 1.0/(1+exp(-z))
#
## stochastic gradient ascent
def stocGradAscent0(dataMatrix, classLabels):
	m = dataMatrix.shape[0]
	n = dataMatrix.shape[1]
	alpha = 0.01
	weights = ones(n)
	for i in range(m):
		h = sigmoid(sum(dataMatrix[i]*weights))
		error = classLabels[i] - h
		weights = weights + alpha * error * dataMatrix[i]
	return weights
#
## random stochastic gradient ascent
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
	m = dataMatrix.shape[0]
	n = dataMatrix.shape[1]
	weights = ones(n)
	for j in range(numIter): 
		dataIndex = range(m)
		for i in range(m):
			alpha = 4/(1.0+j+i)+0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex]*weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weights
#

def plotBestFit(weights):
	import matplotlib.pyplot as plt
	dataMat,labelMat=loadData()
	dataArr = array(dataMat)
	n = dataArr.shape[0]
	xcord1 = []; ycord1 = []
	xcord2 = []; ycord2 = []
	for i in range(n):
		if int(labelMat[i])== 1:
			xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
	ax.scatter(xcord2, ycord2, s=30, c='green')
	x = arange(-3.0, 3.0, 0.1)
	y = (-weights[0]-weights[1]*x)/weights[2]
	ax.plot(x, y)
	plt.xlabel('X1'); plt.ylabel('X2');
	plt.show()
#

#### END

dataArr, labelMat = loadData()
print("-------------"+"Data ready"+"-------------")
weights = stocGradAscent1(array(dataArr),labelMat,150)
plotBestFit(weights)
