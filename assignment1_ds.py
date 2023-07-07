     #  Assignment 1  Data Science
 # 1. Write a Python program to reverse a string without using any built-in string reversal functions.
str1="python"
s=""
for i in str1:
    s= i + s 
print(s)


# 2. Implement a function to check if a given string is a palindrome.
def strPalindrome(s,start,end):
    while start<=end:
        if s[start]==s[end]:
            start=start+1
            end=end-1
        else:
            return False
    return s          
s="nitin"
#s="abcddcba"
# s="mango"
start=0
end=len(s)-1
result=strPalindrome(s,0,end)
print (result)

#3. Write a program to find the largest element in a given list.
l1=[3,2,6,5,9,8]
print(max(l1))
def largest(li):
    temp=li[0]
    for i in range (1,len(li)):
        if li[i]>temp:
            temp=li[i]
        else:
            pass
    return temp


li=[3,2,4,8,6,9,7]
result=largest(li)
print(result)

# 4. Implement a function to count the occurrence of each element in a list

#5. Write a Python program to find the second largest number in a list.
li=[32,23,43,28,94,45]
li.sort()
print("second largest number is" , li[-2])

# 6. Implement a function to remove duplicate elements from a list.
# method 1
li=[2,3,1,2,5,4,2,5,8]
new_list=set(li)
print(new_list)

# method 2 
def Remove(li):
    new_list = []
    for i in li:
        if i not in new_list:
            new_list.append(i)
    return new_list
     

li=[27,32,11,27,32,41,27,11,84]
print(Remove(li))

#7. Write a program to calculate the factorial of a given number.
def factorial(n):

    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
n = 7
result = factorial(n)
print("The factorial of", n, "is", result)

# 8. Implement a function to check if a given number is prime.
import math
 
def check_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
 
print(check_prime(11))  
print(check_prime(1))
print(check_prime(15)) 

# 9. Write a Python program to sort a list of integers in ascending order.
li=[76,32,12,45,39,87,51,93,11]
li.sort()
print(li)

# 10. Implement a function to find the sum of all numbers in a list.
def sum(li):
    total = 0
    for i in li:
        total+=i
    return total

li=[2,5,7,8,4,12,9]    
result=sum(li)
print(result)


# 11. Write a program to find the common elements between two lists.
def common_elements(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
 
    if (l1_set & l2_set):
        print(l1_set & l2_set)
    else:
        print("No common elements")
          
  
l1 = [3,2,5,1,7,6]
l2 = [4,5,8,9,10]
common_elements(l1, l2)
  

# 12. Implement a function to check if a given string is an anagram of another string.
def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False

str1="team"
str2="mate"
result=anagram(str1,str2)
print(result)
    
# 13. Write a Python program to generate all permutations of a given string.

# 14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 

n = 5
result=fibonacci(n)
print(result)

# 15. Write a program to find the median of a list of numbers.

def test(li):
    li.sort()
    n=len(li)
    if n % 2 == 0:
        median = (li[n//2 - 1] + li[n//2]) / 2
    else:
        median = li[n//2]
    return median 

  
li = [4, 5, 8, 9, 10, 17]
result=test(li)
print(result)

# 16. Implement a function to check if a given list is sorted in non-decreasing order.

def check_list(A):
    A_copy=A[:]
    A_copy.sort()
    if (A==A_copy):
        return True
    else:
        return False    

A = [11,23,42,51,67]
result=check_list(A)
print(result)


# 17. Write a Python program to find the intersection of two lists.
def intersection(l1, l2):
    return list(set(l1) & set(l2))
 

l1 = [3,2,15, 9, 10, 5, 4, 9]
l2 = [3,9, 4, 5, 36, 47, 26, 10]
result=intersection(l1, l2)
print(result)


# 18. Implement a function to find the maximum subarray sum in a given list.

# 19. Write a program to remove all vowels from a given string.

def remove_vowel(str1):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ""
    n = len(str1)

    for i in range(n):
        if str1[i] not in vowels:
           new_string = new_string + str1[i]
    return new_string       

str1="Pre PLcement Program"
result=remove_vowel(str1)
print(result)


# 20. Implement a function to reverse the order of words in a given sentence.
def reverse(str1):
    s = str1.split()[::-1]
    li=[]
    for i in s:
        li.append(i)
        
    return li  
str1="Pre Placement Program" 
result=reverse(str1) 
print(result) 

# 21. Write a Python program to check if two strings are anagrams of each other.
def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False

str1="teacher"
str2="cheater"
result=anagram(str1,str2)
print(result)

# 22. Implement a function to find the first non-repeating character in a string.


# 23. Write a program to find the prime factors of a given number.
def Prime_Factorial(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2,(2+n//2)):
            if i == (1 + n // 2):
                arr.append(n)
                n = n // n
            if n % i == 0:
                arr.append(i)
                n = n // i
                break
    return arr


n = 210
print(Prime_Factorial(n))

# 24. Implement a function to check if a given number is a power of two.
def PowerTwo(n):
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True

n=64
result=PowerTwo(n) 
print(result)   

# 25. Write a Python program to merge two sorted lists into a single sorted list.
l1 = [1,2,3,4,5]
l2= [10,20,30,40,50,60]
print(sorted(l1 + l2))

# 26. Implement a function to find the mode of a list of numbers.

# 27. Write a program to find the greatest common divisor (GCD) of two numbers.
def gcd(n1,n2):
    if (n2 == 0):
         return n1
    return gcd(n2, n1%n2)

n1=98
n2=56
result=gcd(n1,n2)
print(result)

# 28. Implement a function to calculate the square root of a given number.
def solve(x):
    start=0
    end=x/2
    
    if x<=1:
        return x

    while start<=end:
        mid=int(start+(end-start) /2)
        if mid**2>x:
           end=mid-1
        elif mid**2<x:
           start=mid+1
        else:
           return mid        
    return end



x=16
result=solve(x)
print(result)

# 29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
def strPalindrome(s,start,end):
    while start<=end:
        if s[start]==s[end]:
            start=start+1
            end=end-1
        else:
            return False
    return s          
s="nitin"
#s="abcddcba"
#s="mango"
start=0
end=len(s)-1
result=strPalindrome(s,0,end)
print (result)

# 30. Implement a function to find the minimum element in a rotated sorted list.
def findMin(li,n):
     
    x = li[0]
    for i in range(n) :
        if li[i] < x :
            x = li[i]
 
    return x
 
li = [15, 9, 11, 2, 3, 4]
n = len(li)
 
print(findMin(li,n))
# 31. Write a program to find the sum of all even numbers in a list.
li=[2,3,4,5,6,7,8,10]

sum=0
for i in li:
  if i%2==0:
    sum=sum+i
print("sum =",sum)

# 32. Implement a function to calculate the power of a number using recursion.
def myPow(x, n):
  if n == 0:
    return 1
  
  elif n < 0:
    x = 1/x
    n = -n
    return myPow(x, n)
  elif n == 1:
    return x
  else:
    
    mid = n // 2

    b = myPow(x, mid)
    result = b * b

    if n % 2 == 0:
      return result
    else:
      return result * x


x = 8
n = 2
result = myPow(x, n)
print(result)
# 33. Write a Python program to remove duplicates from a list while preserving the order.

li = [1, 1, 9, 1, 9, 6, 9, 7]
new_list = sorted(set(li), key=li.index)
print(new_list)

# 34. Implement a function to find the longest common prefix among a list of strings.

# 35. Write a program to check if a given number is a perfect square.
n = 64
 
for i in range(n+1):
    if i**2 == n:
        print("Yes")
        break
else:
    print("No")

# 36. Implement a function to calculate the product of all elements in a list.
def product(l1):
    prod = 1
    for i in l1:
         prod = prod * i
    return prod
     

l1 = [10, 20, 4, 3]
result=product(l1)
print(result)

# 37. Write a Python program to reverse the order of words in a sentence while preserving the word order.

# 38. Implement a function to find the missing number in a given list of consecutive numbers.
def MissingNumber(li):
    i, sum1 = 0, 1
    n=len(li)
    for i in range(2, n + 2):
        sum1 += i
        sum1 -= li[i - 2]
    return sum1
 
li=[ 1, 2 , 5 , 3 ]
result=MissingNumber(li)
print(result)

# 39. Write a program to find the sum of digits of a given number.
def sum_digit(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = 123
result=sum_digit(n)
print(result)

# 40. Implement a function to check if a given string is a valid palindrome considering case sensitivity.
def valid_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start = start + 1
        while start < end and not s[end].isalnum():
            end = end - 1
        if s[start].lower() != s[end].lower():
            return False
        start = start + 1
        end = end - 1
        
    return True
s="Nitin"    
result=valid_palindrome(s)
print(result)

# 41. Write a Python program to find the smallest missing positive integer in a list.
def missing(li):
    n = len(li)
    l2 = li
    x = set(l2)
    for i in range(1, n + 2):
        if i not in x:
            return i

li=[-1,9,4,0,2,3] 
result=missing(li)  
print(result) 

# 42. Implement a function to find the longest palindrome substring in a given string.

# 43. Write a program to find the number of occurrences of a given element in a list.
def find(li, x):
    count = 0
    for i in li:
        if (i == x):
            count = count + 1
    return count
 
li = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
result=find(li,x)
print(result)

# 44. Implement a function to check if a given number is a perfect number.
def perfect(n):  
    sum_n = 0  
    for i in range(1, n):  
        if n % i == 0:  
            sum_n=sum_n+i  
    return sum_n == num  
n=25
result=perfect(n) 
print(result)

# 45. Write a Python program to remove all duplicates from a string.
str1="Pre Placement Program "
str2=[]
for e in str2:
    if e not in str2:
        str2.append(e)
for i in range(0,len(str2)):
    print(str2[i],end="")

# 46. Implement a function to find the first missing positive.
def MissingNumber(li):
    i, sum1 = 0, 1
    n=len(li)
    for i in range(2, n + 2):
        sum1 += i
        sum1 -= li[i - 2]
    return sum1
 
li=[ -1, 2 , 5 , 3 ]
result=MissingNumber(li)
print(result)


