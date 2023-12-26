"""
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# wqs C＋＋中的函数（不只是构造函数）参数可以拥有默认值。 but can not c
def foo(a=4):
    print("a is ")

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ''

        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0:1]
        
        for i in range(n):
            
            # wqs j is left than i index
            for j in range(i - 1, -1, -1):
                # wqs the dp impact is as flag
                # wqs the position[j][i] above the diagonal
                # wqs the dp[][] true meaning that is j->i is the true palindromic
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    # wqs if n>len(s):
                    # wqs the special case is that dp[n-1][0]
                    # wqs this the new case need to update ans
                    if i - j + 1 > len(ans):
                        ans = s[j:i + 1]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("jkbsgawww"))
    print(sol.longestPalindrome(""))
    print(sol.longestPalindrome("ababbabababa"))
