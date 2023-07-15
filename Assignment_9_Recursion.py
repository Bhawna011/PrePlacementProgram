#  Assignment 9 Recursion 

#  **Question 1**

# Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

# An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

# **Example 1:**
# Input: n = 1 

# Output: true

# **Example 2:**
# Input: n = 16 

# Output: true

# **Example 3:**
# Input: n = 3 

# Output: false

def power_of_two(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 != 0:
        return False
    else:
        return power_of_two(n // 2)

print(power_of_two(1))  
print(power_of_two(16))  
print(power_of_two(3))  
    

#  **Question 2**

# Given a number n, find the sum of the first natural numbers.

# **Example 1:**
# Input: n = 3 
# Output: 6

# **Example 2:**
# Input  : 5 
# Output : 15


# time complexity : O(n) 
# space complexity :O(n)

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

print(sum_of_natural_numbers(3))  
print(sum_of_natural_numbers(5))  


#  **Question 3**

# ****Given a positive integer, N. Find the factorial of N. 
# **Example 1:**
# Input: N = 5 
# Output: 120

# **Example 2:**
# Input: N = 4
# Output: 24


# time complexity :O(N)
# space complexity : O(N)

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)

print(factorial(5))  
print(factorial(4))  


# **Question 4**

# Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

# **Example 1 :** 

# Input: N = 5, P = 2

# Output: 25

# **Example 2 :**
# Input: N = 2, P = 5

# Output: 32

def exponent(N, P):
    if P == 0:
        return 1
    else:
        return N * exponent(N, P - 1)

print(exponent(5, 2))  
print(exponent(2, 5))  


#  **Question 5**

# Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

# **Example 1:**

# Input: arr = {1, 4, 3, -5, -4, 8, 6};
# Output: 8

# **Example 2:**

# Input: arr = {1, 4, 45, 6, 10, -8};
# Output: 45


# time complexity : O(n)
# space complexity : O(n)

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))

arr1 = [1, 4, 3, -5, -4, 8, 6]
arr2 = [1, 4, 45, 6, 10, -8]

print(find_max(arr1))  
print(find_max(arr2))  


#  **Question 6**

# Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.

# **Example 1:**

# Input : a = 2 d = 1 N = 5
# Output : 6
# The 5th term of the series is : 6

# **Example 2:**

# Input : a = 5 d = 2 N = 10
# Output : 23
# The 10th term of the series is : 23


def nth_term_of_ap(a, d, N):
    if N == 1:
        return a
    else:
        return nth_term_of_ap(a + d, d, N - 1)

print(nth_term_of_ap(2, 1, 5))  
print(nth_term_of_ap(5, 2, 10)) 


#  **Question 7**

# Given a string S, the task is to write a program to print all permutations of a given string.

# **Example 1:**

# ***Input:***

# *S = “ABC”*

# ***Output:***

# *“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

# **Example 2:**

# ***Input:***

# *S = “XY”*

# ***Output:***

# *“XY”, “YX”*

def permutations(S):
   
    S = list(S)
    n = len(S)
    result = []

    def permute(start):
        if start == n - 1:
            
            result.append("".join(S))
        else:
            for i in range(start, n):
                
                S[start], S[i] = S[i], S[start]
                
                permute(start + 1)
                
                S[start], S[i] = S[i], S[start]

    
    permute(0)

    return result



# **Question 8**

# Given an array, find a product of all array elements.

# **Example 1:**

# Input  : arr[] = {1, 2, 3, 4, 5}
# Output : 120
# **Example 2:**

# Input  : arr[] = {1, 6, 3}
# Output : 18


# time complexity : O(n)
# space complexity : O(n)

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product_of_array(arr[1:])

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 6, 3]

print(product_of_array(arr1))  
print(product_of_array(arr2))  

