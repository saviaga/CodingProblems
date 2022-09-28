class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for elem in strs:
            key = sorted(elem)
            groups[tuple(key)].append(elem)
        res = []

        for key,value in groups.items():
            res.append(value)
        return res