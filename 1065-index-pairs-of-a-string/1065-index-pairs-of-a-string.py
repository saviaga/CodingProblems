
class Trie(object):
    def __init__(self):
        self.root = Trie.TrieNode()
    
    
    class TrieNode(object):
        def __init__(self):
            self.children= collections.defaultdict(Trie.TrieNode)
            self.eow = False
            
        def __contains__(self,key):
            return key in self.children
        def __getitem__(self,key):
            return self.children[key]

    def insert(self,word):
        node = self.root
        for char in word:
            node = node[char]
        node.eow = True
            
            
                

class Solution(object):

    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(text)
        mytrie = Trie()
        node = mytrie.root
        
        #O(KL) time space, k is #words, L is max len of word
        for word in words:
            mytrie.insert(word)
        solutions = []
        
        def trie_search(j):
            node = mytrie.root
            j = i
            while node and j < n  and text[j] in node:
                node = node[text[j]]
                if node.eow:
                    solutions.append([i,j])
                j+=1
        #O(N*L)
        for i in range(n):
            trie_search(i)
        return solutions
            
            
            