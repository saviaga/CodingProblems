class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie['word'] = word
        
    def search(self, word):
        return self.helper(self.trie, word)
    
    def helper(self, trie, word):
        if not word:
            return True if trie.get('word') else False

        if word[0] == '.':
            for c in trie:
                if c != 'word' and self.helper(trie[c], word[1:]):
                    return True
        elif word[0] in trie:
            return self.helper(trie[word[0]], word[1:])
        return False
    
    #Easy part is space complexity, it is O(M), where M is sum of lengths of all words in our Trie. This is upper bound: in practice it will be less than M and it depends, how much words are intersected. The worst time complexity is also O(M), potentially we can visit all our Trie, if we have pattern like ...... For words without ., time complexity will be O(h), where h is height of Trie. For words with several letters and several ., we have something in the middle.


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)