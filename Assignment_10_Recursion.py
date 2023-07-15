# Assignment 10 Recursion 

# **Question 1**

# Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

# An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

# Input: n = 27
# Output: true
# Explanation: 27 = 33

# time complexity  : O(log n)
# space complexity : O(log n)

def power_of_three(n):
    if n == 1:
        return True
    elif n <= 0 or n % 3 != 0:
        return False
    else:
        return is_power_of_three(n // 3)

print(power_of_three(27))  


# **Question 2**

# You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

# - Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
# - Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
# - Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

# Given the integer `n`, return *the last number that remains in* `arr`.

# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2,3, 4,5, 6,7, 8,9]
# arr = [2,4, 6,8]
# arr = [2, 6]
# arr = [6]

# time complexity  : O(log n)
# space complexity : O(log n)

def last_remaining(n):
    if n == 1:
        return 1
    else:
        return 2 * (n // 2 + 1 - last_remaining(n // 2))

print(last_remaining(9))  


#  **Question 3**

# ****Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

# **Example 1:**

# Input :  set = “abc”

# Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}

def print_subsets(s, subset=""):
    if len(s) == 0:
        print(subset)
    else:
        print_subsets(s[1:], subset)
        print_subsets(s[1:], subset + s[0])
print_subsets("abc")



# **Question 4**

# Given a string calculate length of the string using recursion.

# Input : str = "abcd"
# Output :4

# Input : str = "GEEKSFORGEEKS"
# Output :13



# time complexity : O(n)
# space complexity : O(n)

def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

print(string_length("abcd"))  


# **Question 5**

# We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

# Input  : S = "abcab"
# Output : 7
# There are 15 substrings of "abcab"
# a, ab, abc, abca, abcab, b, bc, bca
# bcab, c, ca, cab, a, ab, b
# Out of the above substrings, there
# are 7 substrings : a, abca, b, bcab,
# c, a and b.

# Input  : S = "aba"
# Output : 4
# The substrings are a, b, a and aba

# time complexity : O(n)
# space complexity : O(n)

def count_contiguous_substrings(s):
    if len(s) <= 1:
        return len(s)
    else:
        count = count_contiguous_substrings(s[1:])
        if s[0] == s[-1]:
            count += len(s) - 1
        return count
print(count_contiguous_substrings("abcab"))  
print(count_contiguous_substrings("aba"))  


# **Question 6**

# The [tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) is a famous puzzle where we have three rods and **N** disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs **N**. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.**Note:** The discs are arranged such that the **top disc is numbered 1** and the **bottom-most disc is numbered N**. Also, all the discs have **different sizes** and a bigger disc **cannot** be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.


# Input:
# N = 2
# Output:
# move disk 1 from rod 1 to rod 2
# move disk 2 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 3
# 3
# Explanation:For N=2 , steps will be
# as follows in the example and total
# 3 steps will be taken.


#  **Question 7**

# Given a string **str**, the task is to print all the permutations of **str**. A **permutation** is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.


#  Input: str = “cd”

# **Output:** cd dc

# **Input:** str = “abb”

# **Output:** abb abb bab bba bab bba

def print_permutations(s, start, end):
    if start == end:
        print("".join(s))
    else:
        for i in range(start, end + 1):
            s[start], s[i] = s[i], s[start]
            print_permutations(s, start + 1, end)
            s[start], s[i] = s[i], s[start]  

s = "cd"
print_permutations(list(s), 0, len(s) - 1)



# **Question 8**

# Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.
# Input : abc de
# Output : 3
# There are three consonants b, c and d.

# Input : geeksforgeeks portal
# Output : 12


def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    if len(s) == 0:
        return count
    else:
        if s[0] in consonants:
            count += 1
        count += count_consonants(s[1:])
        return count

print(count_consonants("abc de"))  
print(count_consonants("geeksforgeeks portal"))  













