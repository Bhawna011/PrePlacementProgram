     # Assignment 18 Searching and Sorting 


#  1. **Merge Intervals**

# Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

# Example 1: 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

#  time complexity :O(n log n)


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])

    merged = [intervals[0]] 

    for interval in intervals[1:]:
        start, end = interval
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append(interval)

    return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
result=merge_intervals(intervals)
print(result)




#  2. **Sort Colors**

# Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# example 1 
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


def sort_colors(nums):
    left = 0  
    right = len(nums) - 1  
    current = 0  

    while current <= right:
        if nums[current] == 0:
            
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
        else:
           
            current += 1
  
nums = [2,0,2,1,1,0]
n = len(nums)
  
result=sortcolor(nums, n)
print(result)
  


#  3. **First Bad Version Solution**

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# time complexity :O(log n)  
# space complexity : O(1)


def first_bad_version(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2  # Calculate the mid point

        if isBadVersion(mid):
            # If mid is a bad version, search in the left half
            right = mid
        else:
            # If mid is not a bad version, search in the right half
            left = mid + 1

    return left

n = 5
bad = 4
result(first_bad_version(n))
print(result)



#  4. **Maximum Gap**

# Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

# You must write an algorithm that runs in linear time and uses linear extra space.

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

# time complexity : O(n)
# space complexity : O(n)


def maximum_gap(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)
    min_num = min(nums)

    bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
    num_buckets = (max_num - min_num) // bucket_size + 1

    buckets = [[float('inf'), float('-inf')] for _ in range(num_buckets)]

   
    for num in nums:
        index = (num - min_num) // bucket_size
        buckets[index][0] = min(buckets[index][0], num)
        buckets[index][1] = max(buckets[index][1], num)

    
    max_gap = 0
    prev_max = min_num
    for bucket in buckets:
        if bucket[0] == float('inf') or bucket[1] == float('-inf'):
            
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]

    return max_gap

nums = [3, 6, 9, 1]
result = maximum_gap(nums)
print(result)



#  5. **Contains Duplicate**

# Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true


#  time complexity : O(n)
#  space complexity : O(n)

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

nums = [1, 2, 3, 1]
result = contains_duplicate(nums)
print(result)



#  6. **Minimum Number of Arrows to Burst Balloons**

# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

def min_arrows(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])

    arrows = 1  
    end = points[0][1] 

    for i in range(1, len(points)):
        start = points[i][0]

        if start > end:
            arrows += 1
            end = points[i][1]  

    return arrows

points = [[10, 16], [2, 8], [1, 6], [7, 12]]
result = min_arrows(points)
print(result)



#  7. **Longest Increasing Subsequence**

# Given an integer array `nums`, return *the length of the longest **strictly increasing***

# ***subsequence***

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize the dynamic programming array

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [10,9,2,5,3,7,101,18]
result=length_of_lis(nums)
print(result)


# 8. **132 Pattern**

# Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`.

# Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence. 

# time complexity : O(n)
# space complexity : O(n)


def find132pattern(nums):
    temp = []
    s3 = float('-inf')

    for num in reversed(nums):
        if num < s3:
            return True

        while temp and temp[-1] < num:
            s3 = temp.pop()

        temp.append(num)

    return False

nums = [1,2,3,4]
result=find132pattern(nums)
print(result)





