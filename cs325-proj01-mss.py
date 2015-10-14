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

# Algorithm 1 - theta(n^3)
#Indices i and j define the start and end of subarray sizes from 1 to n.
#k serves to find the sum within each subarray and compares to max_sum.
def mss_algorithm_01(A):

    max_sum = A[0]
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            sum = 0
            for k in range(i, j+1):
                sum += A[k]
                if sum > max_sum:
                    max_sum = sum
                    start = i
                    end = j+1

    return A[start:end], max_sum

print("Algorithm 1 Results:")
for A in testarrays:
    results = []
    results = mss_algorithm_01(A)
    print(results[0])
    print(results[1])
    print()

# Algorithm 2 - theta(n^2)
#Indices i and j define the start and end of subarray sizes from 1 to n.
#Keeps cumulative sum values during iteration rather than recalculating each time.
def mss_algorithm_02(A):
    start = 0
    end = 0
    max_sum = A[0]
    for i in range(0, len(A)):
        sum = A[i]
        for j in range(i+1, len(A)):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
            elif A[j] > max_sum: 
                max_sum = A[j]
                start = i
                end = j+1

    return A[start:end], max_sum

print("Algorithm 2 Results:")
for A in testarrays:
    results = []
    results = mss_algorithm_01(A)
    print(results[0])
    print(results[1])
    print()

# Algorithm 3 - theta(n lg n)
def findFirstMax(A):
    reverseA = A[::-1]
    currmax = reverseA[0]
    currsum = 0

    for i in reverseA:
        currsum += i
        if currsum > currmax:
            currmax = currsum

    return currmax

def findSecondMax(A):
    currsum = 0
    currmax = A[0]

    for i in A:
        currsum += i
        if currsum > currmax:
            currmax = currsum

    return currmax

def mss_algorithm_03(A):

    if len(A) <= 1:
        return A[0]

    else:
        firstArr = A[:int(len(A)/2)]
        secondArr = A[int(len(A)/2):]

        sum1 = mss_algorithm_03(firstArr) # If maximum subarray is contained entirely in the first half
        sum2 = mss_algorithm_03(secondArr) # If maximum subarray is contained entirely in the second half

        sum3 = findFirstMax(firstArr) + findSecondMax(secondArr)

        max_sum = max([sum1, sum2, sum3])

        return max_sum

print("Algorithm 3 Results:")
for A in testarrays:
    results = mss_algorithm_03(A)
    print(results)
    print()

# Algorithm 4 - theta(n) time
def mss_algorithm_04(A):
    sum = A[0]
    max_sum = A[0]
    for j in A:
        curr_start = 0
        curr_end = j
        if sum > 0:
            sum += A[j]
        else:
            curr_start = j
            sum = A[j]
        
        if sum > max_sum:
            max_sum = sum
            start = curr_start
            end = curr_end
        
    return A[start:end], max_sum

print("Algorithm 4 Results:")
for A in testarrays:
    results = []
    results = mss_algorithm_01(A)
    print(results[0])
    print(results[1])
    print()



# ALGORITHM TIMING TESTS
# 10 runs of each n-sized array

def get_timing(algnum, algorithm, start_range, end_range, range_step):

    print ("Algorithm " + str(algnum) + " Timing Results -- " + str(start_range) + " to " + str(end_range - range_step) + " n Array Sizes:")
    for size in range(start_range,end_range,range_step):

        total_results = []
        for run in range(10):
            #Generates random number from -50 to 50 and inserts it into array
            A = []
            for i in range(size):
                A.append(random.randint(-50, 50))

            #Runs algorithm and gets timing
            start_time = time.time()
            #mss_algorithm_01(A)
            algorithm(A)
            run_time = time.time() - start_time

            total_results.append(run_time)

        #get average running time from total results
        sum = 0
        avg = 0
        for res in total_results:
            sum += res
        avg = sum/10

        print(str(avg))
    print()

get_timing(1, mss_algorithm_01, 100, 1100, 100)
get_timing(2, mss_algorithm_02, 1000, 11000, 1000)
get_timing(3, mss_algorithm_03, 100000, 1100000, 100000)
get_timing(4, mss_algorithm_04, 1000000, 11000000, 1000000)
