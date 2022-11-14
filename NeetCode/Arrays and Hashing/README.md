### Task 217: Containt duplicates

### Task 242: Valid anagram

### Task 1: Two sum

### Task 49: Group anagrams

### Task 347: Top K frequnet elemets
Best complexity - O(n)
General idea:
* Count frequency of every value from input list, save in dict like value - frequnecy
* Create list with empty sublists size len(nums) + 1, for worst case when all values are the same
* Put values in sublists, where sublist index is value frequnecy
* Extract top K values from reverted list



