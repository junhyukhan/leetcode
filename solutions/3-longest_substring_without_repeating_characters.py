from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = set()
        l = 0
        longest = 0
        for r, val in enumerate(s):
            if val not in alpha:
                alpha.add(val)
                longest = max(longest, r-l+1)
            else:
                while val in alpha:
                    alpha.remove(s[l])
                    l += 1
                alpha.add(s[r])
        return longest
