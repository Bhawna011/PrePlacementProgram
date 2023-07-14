                      # Assignment 11 Binary Search
  
#  **Question 1**

# Given a non-negative integer `x`, return *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

# You **must not use** any built-in exponent function or operator.

# - For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

def find_sqrt(x):
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return -1  

x=4
result=find_sqrt(x)
print(result)


# **Question 2**

# A peak element is an element that is strictly greater than its neighbors.

# Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

# You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in `O(log n)` time.

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Time complexity: O(log N)
# Space complexity: O(1)

def peakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

nums = [1,2,3,1]
result=peakElement(nums)
print(result)



# **Question 3**
# Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the
# range that is missing from the array.*

# **Example 1:**

# Input: nums = [3,0,1]
# Output: 2

# Time complexity: O(N)
# Space complexity: O(1)

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(nums)  

    return expected_sum - actual_sum

nums = [3,0,1]
result=missingNumber(nums)
print(result)


# **Question 4**

# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` 
# inclusive.

# There is only **one repeated number** in `nums`, return *this repeated number*.

# You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

# Input: nums = [1,3,4,2,2]
# Output: 2

# Time complexity: O(N LogN)
# Space complexity: O(1)


def findDuplicate(nums):
    low = 1
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in nums)

        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low

nums = [1,3,4,2,2]
result=findDuplicate(nums)
print(result)


# **Question 5**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order*

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))

nums1 = [1,2,2,1]
nums2 = [2,2]
result=intersection(nums1, nums2)
print(result)




#  **Question 6**

# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.

# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

# You must write an algorithm that runs in `O(log n) time.`

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


# time complexity : O(log n)  
#  space complexity : O(1)

def findMin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1

    return nums[low]


nums = [3,4,5,1,2]
result=findMin(nums)
print(result)


#  **Question 7**

# Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

# If `target` is not found in the array, return `[-1, -1]`.

# You must write an algorithm with `O(log n)` runtime complexity.

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Time complexity: O(LogN)
# Space complexity: O(1)

def searchRange(nums, target):
    left = -1
    right = -1

   
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    if nums[low] == target:
        left = low

    
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high + 1) // 2

        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid

    if nums[high] == target:
        right = high

    return [left, right]


nums = [5,7,7,8,8,10]
target = 8
result=searchRange(nums, target)
print(result)


#  **Question 8**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []

    for num in nums1:
        low = 0
        high = len(nums2) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums2[mid] == num:
                left = right = mid

                while left > 0 and nums2[left - 1] == num:
                    left -= 1
                while right < len(nums2) - 1 and nums2[right + 1] == num:
                    right += 1

                result.extend(nums2[left:right + 1])
                break
            elif nums2[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

    return result

nums1 = [1,2,2,1]
nums2 = [2,2]
result=intersect(nums1, nums2)
print(result)