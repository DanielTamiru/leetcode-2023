class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        -   Brute force approach: sequentially assign s3 chars to s1 or s2, branching at each point
            where char could be assigned to both. If an assignment branch reaches the end of s3 without
            encountering an unassignable char, s3 is an interleave
        -   This question explodes exponentially and has a ton of subproblem redundancy between the
            branches, making it a great candidate for memoization or a DP solution
        """
        l1, l2 = len(s1), len(s2)
        
        # Edge cases:
        if not s1: return s3 == s2
        if not s2: return s3 == s1
        if len(s3) != l1 + l2: return False

        dp = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # Base cases:
        dp[l1] = [s3[l1+j:] == s2[j:] for j in range(l2)]
        for i in range(l1): dp[i][l2] = s3[l2+i:] == s1[i:]

        # Fill table:
        for i in reversed(range(len(s1))):
            for j in reversed(range(len(s2))):
                dp[i][j] =  (s1[i] == s3[i + j] and dp[i+1][j]) or (s2[j] == s3[i + j] and dp[i][j+1])

        return dp[0][0]
