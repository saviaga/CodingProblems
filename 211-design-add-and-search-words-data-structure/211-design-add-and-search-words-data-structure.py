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
        def search_node(idx,node):
            
            for i in range(idx,len(word)):
                w = word[i]
                if w==".":
                    for child in node.children.values():
                        if search_node(i+1,child):
                            return True
                    return False

                else:
                    if w not in node.children:
                        return False
                    node = node.children[w]
            return node.eow
        return search_node(0,self.root)
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)