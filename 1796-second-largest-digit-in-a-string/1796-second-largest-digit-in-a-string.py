class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) < 2):
            return -1
        max_num = -1
        second_max = -1
        for elem in s:
            if elem.isdigit():
                if elem > max_num:
                    second_max = max_num
                    max_num = elem
                elif elem!=max_num and elem > second_max:
                    second_max = elem
        return second_max