# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # Parameters initialization
        # freq dicts for sring t an rolling window
        freq_t, freq_w = {}, {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        # level of correct freqs in our dicts
        # thus we sill compare only necessary symbols with O(1)
        have, need = 0, len(freq_t)
        # result trackers
        res, res_len = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            char = s[r]
            freq_w[char] = freq_w.get(char, 0) + 1
            if char in freq_t and freq_w[char] == freq_t[char]:
                have += 1
            # cut down substring if we have all necessary freqs inside window
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                freq_w[s[l]] -= 1
                if s[l] in freq_t and freq_w[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""