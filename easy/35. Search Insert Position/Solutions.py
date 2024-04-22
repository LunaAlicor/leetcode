class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
		    return nums.index(target)
        else:
            if target < min(nums):
                return 0
            if target > max(nums):
                return len(nums)
            last_elem = None
            target_copy = target-1
            while True:
                if target_copy in nums:
                    last_elem = target_copy
                    break
                else:
                    target_copy -= 1
            return nums.index(last_elem)+1