class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['eow'] = True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node:
                return False
            node = node[i]
        return 'eow' in node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
        return True
               
                                

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#time O(longest string * #queries)