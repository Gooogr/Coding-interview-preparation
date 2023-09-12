# https://leetcode.com/problems/word-break/

from typing import List

###--- Naive recursive solution - TL error ---###
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def can_break(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordDict and can_break(s, wordDict, end):
                    return True
            return False  
        return can_break(s, set(wordDict), 0)

###---------- DP implementation - OK ----------###
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # s[i : i + len(w)] == w is O(n), this could be optimized with trie
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

###--------- Trie implementation -OK ---------###

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		# instantiate an empty trie 
        trie = Trie()
        # Iterate over words in dictionary and build trie one word at a time
        for word in wordDict:  
            trie.add(word) 
        print(trie.root.children)
        #Find if s is made up of words in the trie
        return trie.find(s)  

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_done = False

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.memo = {}

    def add(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node(char)
            # on to the child - going one level down the tire branch/path
            root = root.children[char]
        root.is_done = True    

    def find(self, s):
        root = self.root
        for i, char in enumerate(s):
            # if char does not exist
            if char not in root.children:
                return False
            # if char does exit, but it's marked as the last char/leaf node
            if root.children[char].is_done: 
			                                            
                # if the remaining part hasn't been seen before, then we need to check it -> call the function recursively
                if s[i+1:] not in self.memo:                 
                    self.memo[s[i+1:]] = self.find(s[i+1:]) 
                # if remaining has been seen - return True (no need to check)
                if self.memo[s[i+1:]]:                 
                    return True
            # move on to the child node - go one level down the branch                                      
            root = root.children[char]         
        #  Only return True if the last char in s is marked as leaf in the trie
        return root.is_done  