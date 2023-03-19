from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Brute force approach: could probably be done two ways, by exhaustively checking every
        possibility on s side or the worddict side. Regardless, it is likely exponential in time
        
        We can do a lot better by taking advantage of check redundancy of substrings of s. Specifically,
        let's try a dp solution, where we iteratively compute dp(l) = wordBreak(s[0:l], wordDict)

        dp(l) = any(dp[i] and s[i:l] in wordDict, for j = 0..l-1)
        """
        dp = [True]

        for l in range(1, len(s) + 1):
            dp.append(any(
                (dp[i] and s[i:l] in wordDict) for i in range(l)
            ))
        
        return dp[-1]