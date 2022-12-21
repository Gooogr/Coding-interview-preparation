# https://leetcode.com/problems/maximum-number-of-balloons/

# My solution with dict counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloon_dict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for letter in text:
            if letter in baloon_dict.keys(): # Works with O(1) becase view ~ set
                baloon_dict[letter] = baloon_dict.get(letter, 0) + 1
        baloon_dict['l'] = baloon_dict['l'] // 2
        baloon_dict['o'] = baloon_dict['o'] // 2
        return min(baloon_dict.values())

# Another solution without letters hardcode, but additional memory
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloon_dict = {}
        text_dict = {}
        for s in 'balloon':
            baloon_dict[s] = baloon_dict.get(s, 0) + 1
        for s in text:
            text_dict[s] = text_dict.get(s, 0) + 1
        max_words = float('inf')
        for key in baloon_dict.keys():
            max_words = min(text_dict.get(key, 0)//baloon_dict[key], max_words)
        return max_words