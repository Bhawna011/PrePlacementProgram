                          # Assignment 3 Array 
# Question 1
# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to the target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

# Time complexity: O(2n)
# Space: O(n)


def closeTriplet(arr, n, x, count, sum, ind, ans, minm):
	if ind == n:
		if count == 3:
			if abs(x - sum) < minm[0]:
				minm[0] = abs(x - sum)
				ans[0] = sum
		return
	closeTriplet(arr, n, x, count + 1, sum + arr[ind], ind + 1, ans, minm)

	closeTriplet(arr, n, x, count, sum, ind + 1, ans, minm)


arr = [-1, 2, 1, -4]
x = 1
n = len(arr)
minm = [float('inf')]
ans = [0]

closeTriplet(arr, n, x, 0, 0, 0, ans, minm)
print(ans[0])


# Question 2
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#            ● 0 <= a, b, c, d < n
#            ● a, b, c, and d are distinct.
#            ● nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


#  **Question 3**
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater
# permutation of its integer. More formally, if all the permutations of the array are
# sorted in one container according to their lexicographical order, then the next
# permutation of that array is the permutation that follows it in the sorted container.

# If such an arrangement is not possible, the array must be rearranged as the
# lowest possible order (i.e., sorted in ascending order).

# ● For example, the next permutation of arr = [1,2,3] is [1,3,2].
# ● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# ● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
# have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.

# **Example 1:**
# Input: nums = [1,2,3]
# Output: [1,3,2]


# Question 4
# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in
# order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# time complexity O(log n)

def searchInsert(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print(result)   

# Question 5
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most significant
# to least significant in left-to-right order. The large integer does not contain any
# leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

def increment(digits):
    n = len(digits)
    
    i = n - 1
    carry = 1
    
    while i >= 0 and carry > 0:
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10
        i -= 1
    if carry > 0:
        digits.insert(0, carry)
    
    return digits
digits = [1, 2, 3]
result = increment(digits)
print(result)

# Question 6
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1



# Time complexity : O(n)
# Space complexity : O(1)

def singleNumber(nums):
        a = 0
        for i in nums:
            a ^= i
        return a
nums = [2,2,1]
result=singleNumber(nums)
print(result)

# Question 7
# You are given an inclusive range [lower, upper] and a sorted unique integer array
# nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in
# nums.

# Return the shortest sorted list of ranges that exactly covers all the missing
# numbers. That is, no element of nums is included in any of the ranges, and each
# missing number is covered by one of the ranges.

# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]


def missingRanges(nums, lower, upper):
        def f(a, b):
            return str(a) if a == b else f'{a}->{b}'

        n = len(nums)
        if n == 0:
            return [f(lower, upper)]
        ans = []
        if nums[0] > lower:
            ans.append(f(lower, nums[0] - 1))
        for a, b in pairwise(nums):
            if b - a > 1:
                ans.append(f(a + 1, b - 1))
        if nums[-1] < upper:
            ans.append(f(nums[-1] + 1, upper))
        return ans
nums = [0,1,3,50,75]
lower = 0
upper = 99
result=missingRanges(nums, lower, upper)
print(result)


# Question 8
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

def attendAllMeeting(intervals) :
    new_intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(len(new_intervals)-1):
        if new_intervals[i-1][1] > new_intervals[i][0]:
            return False
    return True

intervals = [[0,30],[5,10],[15,20]]
result=attendAllMeeting(intervals)    
print(result)
