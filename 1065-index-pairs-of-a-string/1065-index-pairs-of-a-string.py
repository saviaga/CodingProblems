
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
        len_t = len(text)
        mytrie = Trie()
        node = mytrie.root
        
        #O(KL) time space, k is #words, L is max len of word
        for word in words:
            mytrie.insert(word)
        solutions = []
        
        def trie_search(char_to_search):
            node = mytrie.root
            idx = char_to_search
            while node and idx < len_t  and text[idx] in node:
                node = node[text[idx]]
                if node.eow:
                    solutions.append([char_to_search,idx])
                idx+=1
        #O(N*L)
        for char in range(len_t):
            trie_search(char)
        return solutions
            
            
            