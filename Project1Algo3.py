__author__ = 'darnelclayton'

# CS325 - Project 1 - Max Sum Subarray

import random
import time



testarrays = [[1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11],
[2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2],
[10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19],
[31,-41, 59, 26, -53, 58, 97, -93, -23, 84],
[3, 2, 1, 1, -8, 1, 1, 2, 3],
[12, 99, 99, -99, -27, 0, 0, 0, -3, 10],
[-2, 1, -3, 4, -1, 2, 1, -5, 4]]

def findFirstMax(A):
	reverseA = A[::-1]
	currmax = reverseA[0]
	currsum = 0
	begIndex = 0

	for i in reverseA:
		currsum += i
		if currsum > currmax:
			currmax = currsum
			begIndex=i

	return [currmax, begIndex]

def findSecondMax(A):
    currsum = 0
    currmax = A[0]
    endIndex = 0

    for i in A:
        currsum += i
        if currsum > currmax:
            currmax = currsum
	    endIndex = i

    return [currmax, endIndex]

def mss_algorithm_03(A):
	leftIndexSum = []
	rightIndexSum = []

	if len(A) <= 1:
		return A[0]

	else:
		firstArr = A[:int(len(A))/2]
		secondArr = A[int(len(A))/2:]

		sum1 = mss_algorithm_03(firstArr) # If maximum subarray is contained entirely in the first half
		sum2 = mss_algorithm_03(secondArr) # If maximum subarray is contained entirely in the second half

		leftSum,leftIndex = findFirstMax(firstArr)
		rightSum, rightIndex = findSecondMax(secondArr)

		sum3 = leftSum + rightSum

        max_sum =  max([sum1, sum3, sum3])

        return A[leftIndex:rightIndex], max_sum

print("Algorithm 3 Results:")
for A in testarrays:
    results = mss_algorithm_03(A)
    print(results[0])
#    print(results[1])

