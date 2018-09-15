class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}
        i = 0
        for n in nums:
          lookup = target - n
          
          if numbers.get(lookup) is not None:
            return [numbers.get(lookup), i]
          numbers[n] = i
          i = i+1
        return []
