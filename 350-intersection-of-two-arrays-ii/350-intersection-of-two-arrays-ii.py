class Solution(object):
            
    def intersect(self, nums1, nums2):
            
        match = {}
        for x in nums1:
            if x in match:
                match[x] += 1
            else:
                match[x] = 1

        i = []
        for x in nums2:
            if x in match:
                i.append(x)
                match[x] -= 1
                if match[x] == 0:
                    del match[x]

        return i
