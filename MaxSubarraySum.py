#Sum of maximum subarray

def maxSubArraysum(nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
               nums[i] += nums[i-1]
        return max(nums)


arr =[-2,-1,0,5,8,6,-10]
r=maxSubArraysum(arr)
print(r)

