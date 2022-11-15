### Task 217: Containt duplicates
Best complexity - O(n)<br>
Iterate over string and add each value in hash.
If value is already in hash - it's duplicate.

### Task 242: Valid anagram
Best complexity - O(n)<br>
General idea: compare count dictionaries of two input strings.<br>
If they same - strings are anagrams.

### Task 1: Two sum
Best complexity - O(n)<br>
General idea: save list elements in hash and compare them with current diff between target and value. If they matched - return idx of current value and idx from hash. <br>
Hash structure: dict[value] = idx

### Task 49: Group anagrams
Best complexity - O(n)<br>
General idea: create hash key for anagrams and store them in dictionary like <br>
dict[anagram_key] = [anagram1, anagram2, ...]<br>
`anagram_key` could be array with length=26 and counted values of each word.

### Task 347: Top K frequnet elemets
Best complexity - O(n)<br>
General idea:
* Count frequency of every value from input list, save in dict like value - frequnecy
* Create list with empty sublists size len(nums) + 1, for worst case when all values are the same
* Put values in sublists, where sublist index is value frequnecy
* Extract top K values from reverted list



