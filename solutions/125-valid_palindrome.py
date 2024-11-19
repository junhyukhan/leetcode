class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(i.lower() for i in s if i.isalnum())
        print(ss, ss[::-1])
        return ss == ss[::-1]     