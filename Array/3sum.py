"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
"""
# Brute Force Approach
def threeSum_Brute(nums):
    n = len(nums)
    nums.sort()
    arr=[]
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                continue
            for k in range(0,n):
                if j==k or i==k:
                    continue
                if nums[i]+nums[j]+nums[k]==0:
                    lst = sorted([nums[i], nums[j], nums[k]])
                    if lst not in arr:
                        arr.append(lst)
    return arr


def threeSum_2pointer(nums):
    n = len(nums)
    nums.sort()
    arr=[]
    for i in range(0,n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start, end = i+1, n-1
        while start < end:
            add = nums[i]+nums[start]+nums[end]
            if add > 0:
                end -= 1
            elif add < 0:
                start += 1
            elif add == 0:
                arr.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1

                while start < end and nums[start] == nums[start-1]:
                    start += 1
                
    return arr


if __name__ == "__main__":
    n = int(input("Enter length of array: "))
    nums = []
    for i in range(n):
        ele = int(input(f"Enter {i}th element of array: "))
        nums.append(ele)
    
    res = threeSum_Brute(nums)
    print("Brute 3 sum arr sums to 0: ", res)

    res1 = threeSum_2pointer(nums)
    print("2 pointer 3 sum arr sums to 0: ", res1)
