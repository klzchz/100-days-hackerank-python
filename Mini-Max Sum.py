# First, take an input of any number by the user after that add all numbers and sort the array after sorting an array remove the first index element and last index element from the array if you get then okay if not see the below full explanation of the problem min-max sum. Read the program statement to find the Mini-Max Sum Hackerrank Solution in C++.

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

# Example

# arr = [1,3,5,7,9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and our maximum sum is 3 + 5 + 7 + 9 = 24. The function prints

# 16 24

# Function Description

# Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
# miniMaxSum has the following parameter(s):
# arr: an array of 5 integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of elements.

# Input Format

# A single line of five space-separated integers.

# Constraints

# 1<=arr[i]<=10^9

# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32-bit integer.)

# Sample Input

# 1 2 3 4 5

# Sample Output

# 10 14

# Mini-Max Sum Explanation

# Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the following sums using four of the five integers:

# If we sum everything except 1, our sum is 2+3+4+5=14.
# If we sum everything except 2, our sum is 1+3+4+5=13.
# If we sum everything except 3, our sum is 1+2+4+5=12.
# If we sum everything except 4, our sum is 1+2+3+5=11.
# If we sum everything except 5, our sum is 1+2+3+4=10.

arr = [1,2,3,4,5]

arr.sort()

mini = sum(arr[0:4]) 
maxi = sum(arr[1:5])

print(f"{mini} {maxi}")


