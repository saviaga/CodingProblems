class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        q = deque()
        visited = set()
        longest = 0
        for elem in wordDict:
            longest = max(longest,len(elem))
        print(longest)
        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if len(s[start:end]) > longest:
                    break
                if s[start:end] in word_set:
                    print(s[start:end])
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False
        