class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sk=[-1]
        max_len=0

        for i,char in enumerate(s):
            if char=='(':
                sk.append(i)
            else:
                sk.pop()
                if not sk:
                    sk.append(i)
                else:
                    max_len=max(max_len, i-sk[-1])
        return max_len
        