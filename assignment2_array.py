# Question 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4

# time complexity = O(nlogn)
# space complexity  = O(1)

def pairSum(nums):

        nums.sort()
        return sum(nums[::2])
nums = [1,4,3,2]  
result=pairSum(nums)
 print(result)    

# Question 2
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3

# time complexity = O(n)
# space complexity = O(n)

def maxUniqueCandies(candyType):
    max_candies = len(candyType) // 2
    unique_candies = set(candyType)
    return min(max_candies, len(unique_candies))

candyType = [1, 1, 2, 2, 3, 3]
result = maxUniqueCandies(candyType)
print(result)


# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5

#  time complexity = O(n log n)
# space complexity = O(1)

def findLHS(nums):
        nums.sort()
        left =0
        right =1
        ans = 0 
        while right < len(nums):
            diff = nums[right] - nums[left]
            if diff == 1: 
                ans = max(ans, right - left + 1)
        
            elif diff <= 1:
                right=right+1
            
            else:
                left=left+1
        
        return ans
nums = [1,3,2,2,5,2,3,7]
result=findLHS(nums)
print("result is ",result)

# Question 4
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# time complexity = O(n)
# space complexity = O(1)

def flowersPlace(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
        i += 1
    return False


flowerbed = [1, 0, 0, 0, 1]
n = 1
result = flowersPlace(flowerbed, n)
print(result)


# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# time complexity =O(n log n)
# space complexity = O(1)

def maxProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

nums = [1, 2, 3]
result = maxProduct(nums)
print(result)

# Question 6
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

# time complexity = O(log n)
# space complexity = O(1)

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)


# Question 7
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
# monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# time complexity = O(n)
# space complexity = O(1)

def monotonic(nums):
    inc = True
    dec = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dec = False
        if nums[i] < nums[i-1]:
            inc = False

    return inc or dec

nums = [1, 2, 2, 3]
result = monotonic(nums)
print(result)





