"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
"""

def twoSum(nums, target):
    n=len(nums)

    #Brute Force approach
    for i in range(0, n):
        for j in range(0, n):
            if (j == i):
                continue
            add = nums[i] + nums[j]
            if(add == target):
                return [i , j]

if __name__ == "__main__":
    n = int(input("Enter length of array: "))
    nums = []
    for i in range(n):
        ele = int(input(f"Enter {i}th element of array: "))
        nums.append(ele)

    target = int(input("Enter target value: "))
    
    res = twoSum(nums, target)
    print("Result index for 2 sum target: ", res)
