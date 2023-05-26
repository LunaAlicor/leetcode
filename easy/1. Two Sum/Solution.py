class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            print(nums[i])
            if target - nums[i] in nums[i+1:]:
                result = i

                return [result, nums.index((target - nums[result]), i+1)]