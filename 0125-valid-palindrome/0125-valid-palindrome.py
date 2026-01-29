class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''.join(i for i in s.lower() if i.isalnum())
        return clean==clean[::-1]        