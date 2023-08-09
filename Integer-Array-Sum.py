# Problem Statement
# Given an array of integers, find the sum of its elements.

# For example, if the array $ar = [1,2,3], 1+2+3 =6, so return 6.

# Function Description
# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

# simpleArraySum has the following parameter(s):

# ar: an array of integers
# Sample Input : 1 2 3 4 10 11
# Sample Output : 31
# Explanation
# In our text editor on HackerRank, we already have the simpleArraySum() function declared with the parameter $ar which can be any given array. All you need to do is write a set of instructions in the function that will calculate the sum of all array elements so whenever the function is called, it can calculate the sum of the array elements of any simple array.
# For example in our Sample Input [1, 2, 3, 4, 10, 11], we expect an output of 31 seeing 1 +2+ 3+ 4 +10 +11 = 31.

def simpleArraySum(ar):
    # Write your code here
    return sum(ar)


arr =[1 ,2 ,3 ,4 ,10 ,11]
print (simpleArraySum(arr))