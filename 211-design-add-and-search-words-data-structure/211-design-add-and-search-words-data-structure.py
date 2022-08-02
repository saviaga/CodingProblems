class TrieNode(object):
        def __init__(self):
            self.children = {}
            self.eow = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
        

    def search(self, word):
        def dfs(j,child):
            cur = child
            for i in range(j,len(word)):
                w = word[i]
                if w==".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                else:
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
            return cur.eow
        return dfs(0,self.root)
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)