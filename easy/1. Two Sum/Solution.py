class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = dict()
        
        for index, value in enumerate(nums):
            sec_num = target - value
            if nums_dict.get(sec_num) is not None:
                result.extend([nums_dict[sec_num], index])
                break
            nums_dict[value] = index

        return [result, nums.index((target - nums[result]), i+1)]
