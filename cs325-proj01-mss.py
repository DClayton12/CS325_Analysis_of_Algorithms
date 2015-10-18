# CS325 - Project 1 - Max Sum Subarray
#Group 9: Darnel Clayton, Rudy Gonzalez, Brad Parker

import random
import time
import sys

sys.setrecursionlimit(1500)
testarrays = []

#read in arrays from text file
def load_arrays():
    with open('mss_problems.txt') as f:
        for line in f:
            inputarray = []
            numstring = line.strip().replace("'", "").replace("[", "").replace("]", "").replace(",", " ")
            numbers = map(int, numstring.split())

            for num in numbers:
                inputarray.append(num)
            testarrays.append(inputarray)
    f.close()
load_arrays()


# Algorithm 1 - theta(n^3)
#Indices i and j define the start and end of subarray sizes from 1 to n.
#k serves to find the sum within each subarray and compares to max_sum.
def mss_algorithm_01(A):

    max_sum = A[0]
    start = None
    end = None
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
                start = i
                end = j+1
            elif A[j] > max_sum: 
                max_sum = A[j]
    if end == 0:
        end = 1
    return A[start:end], max_sum


# Algorithm 3 - theta(n lg n)
def cross_subarray(A, start, mid, end):
    left_sum = 0
    maxleft_sum = float("-inf")

    for i in range(mid, start-1, -1):
        left_sum = left_sum + A[i]
        if left_sum > maxleft_sum:
            maxleft_sum = left_sum

    right_sum = 0
    maxright_sum = float("-inf")

    for j in range(mid+1, end+1, 1):
        right_sum = right_sum + A[j]
        if right_sum > maxright_sum:
            maxright_sum = right_sum

    return maxleft_sum + maxright_sum

def mss_algorithm_03(A, start, end):

    if start == end:
        return A[start]

    else:
        mid = int((start + end)/2)

        left_sum = mss_algorithm_03(A, start, mid)
        right_sum = mss_algorithm_03(A, mid+1, end)
        cross_sum = cross_subarray(A, start, mid, end)

        return max(left_sum, right_sum, cross_sum)


# Algorithm 4 - theta(n) time
def mss_algorithm_04(A):
    curr_start = float("-inf")
    curr_end = float("-inf")
    start = float("-inf")
    end = float("-inf")
    max_sum = float("-inf")
    endsum = float("-inf")

    for j in range(0, len(A)):

        curr_end = j
        if endsum > 0:
            endsum += A[j]
        else:
            curr_start = j
            endsum = A[j]

        if endsum > max_sum:
            max_sum = endsum
            start = curr_start
            end = curr_end + 1
        
    return A[start:end], max_sum

# ALGORITHM ACCURACY TESTS
def test_accuracy():
    f = open("mss_results.txt", "w")
    print("Algorithm 1 Results:")
    f.write("Algorithm 1 Results:" + "\n")
    for A in testarrays:
        results = []
        results = mss_algorithm_01(A)
        print(results[0])
        print(results[1])
        f.write("[")
        f.write(", ".join(str(elem) for elem in results[0]))
        f.write("]" + "\n")
        f.write(str(results[1]) + "\n\n")
        print()

    print("Algorithm 2 Results:")
    f.write("Algorithm 2 Results:" + "\n")
    for A in testarrays:
        results = []
        results = mss_algorithm_02(A)
        print(results[0])
        print(results[1])
        f.write("[")
        f.write(", ".join(str(elem) for elem in results[0]))
        f.write("]" + "\n")
        f.write(str(results[1]) + "\n\n")
        f.write("\n")
        print()

    print("Algorithm 3 Results:")
    f.write("Algorithm 3 Results:" + "\n")
    for A in testarrays:
        results = mss_algorithm_03(A, 0, len(A)-1)
        print(results)
        #f.write(results[0])
        #f.write(results[1])
        f.write(str(results) + "\n\n")
        print()

    print("Algorithm 4 Results:")
    f.write("Algorithm 4 Results:" + "\n")
    for A in testarrays:
        results = []
        results = mss_algorithm_04(A)
        print(results[0])
        print(results[1])
        f.write("[")
        f.write(", ".join(str(elem) for elem in results[0]))
        f.write("]" + "\n")
        f.write(str(results[1]) + "\n\n")
        f.write("\n")
        print()

    print("Accuracy Results written to mss_results.txt" + "\n\n")
    f.close()


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
            if algorithm == mss_algorithm_03:
                start_time = time.time()
                algorithm(A, 0, len(A)-1)
                run_time = time.time() - start_time
            else:
                start_time = time.time()
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


test_accuracy()
get_timing(1, mss_algorithm_01, 100, 1100, 100)
get_timing(2, mss_algorithm_02, 1000, 11000, 1000)
get_timing(3, mss_algorithm_03, 100000, 1100000, 100000)
get_timing(4, mss_algorithm_04, 1000000, 11000000, 1000000)
