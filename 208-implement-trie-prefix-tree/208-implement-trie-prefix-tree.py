class Trie(object):
    def __init__(self):
        self.root = Trie.TrieNode()
    
    class TrieNode(object):
        def __init__(self):
            self.eow=False
            self.children={}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self.root
        for char in word:
                if char not in node.children:
                    node.children[char]=Trie.TrieNode()
                node=node.children[char]
        node.eow=True        
            
 
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
       
        node=self.root
        for char in word:
                if char not in node.children:
                    return False
                node=node.children[char]
        return node.eow
                  

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
       
        node=self.root
        for char in prefix:
                if char not in node.children:
                    return False
                node=node.children[char]
        return True
       
                                

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#time O(longest string * #queries)