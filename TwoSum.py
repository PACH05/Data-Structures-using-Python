#Two Sum

class Solution(object):
    def twoSum(self, nums, target):
       buffer = {}
       for i in range(len(nums)):
           if target - nums[i] in buffer:
               return [buffer[target - nums[i]], i]

           else :
               buffer[nums[i]] = i


ar = [2,7,11,15]
o1 = Solution()
print(o1.twoSum(ar,9))



