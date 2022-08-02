class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndNode = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEndNode = True     

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
            return cur.isEndNode
        return dfs(0,self.root)
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)