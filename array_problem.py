# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

nums=[1,1,2,2,4,5,5]
res = nums[0]

for i in range(1,len(nums)):
    res=res^nums[i]

print(res)

# the bitwise XOR will give 0 for same numbers and return the number for the others


# def singleNumber(nums:a) :
#     nums.sort()
#     for i in range(len(nums)):
#         if(nums[i]==nums[i+1]):
#             pass
#         else:
#             return nums[i]



# b= singleNumber(a)
# print(b)