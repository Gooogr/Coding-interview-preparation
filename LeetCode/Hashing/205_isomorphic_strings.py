# https://leetcode.com/problems/isomorphic-strings/description

# map symbols with each other
# paper, title -> {p: t, ..., e:l, r:e} {t:p, ..., l:e, e:r}
# check mapping at every step
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {} # keep separate to prevent key mix. For example 'er' and 'le'
        for idx in range(len(s)):
            if (s[idx] not in hash_s) and (t[idx] not in hash_t):
                hash_s[s[idx]] = t[idx]
                hash_t[t[idx]] = s[idx]
                continue

            val_s = hash_s.get(s[idx], None)
            val_t = hash_t.get(t[idx], None)
            if s[idx] != val_t or t[idx] != val_s:
                return False
        return True