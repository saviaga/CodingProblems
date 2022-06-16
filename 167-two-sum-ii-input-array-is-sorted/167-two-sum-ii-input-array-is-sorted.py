class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = 0
        indices = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in indices:
                return [indices[complement]+1,i+1]
            else:
                indices[numbers[i]] = i
        return []
        