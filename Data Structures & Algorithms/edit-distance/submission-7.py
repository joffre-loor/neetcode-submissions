class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1)+1) for _ in range((len(word2)+1))]

        lenCol = len(word1)
        lenRow = len(word2)
        dp[0][0] = 0
        for col in range(1,len(word1)+1):
            dp[0][col] = col
        
        for row in range(1, len(word2)+1):
            dp[row][0] = row
        
        for row in range(1, len(word2)+1):
            for col in range(1, len(word1)+1):
                if word2[row-1] == word1[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
        print(dp)
        return dp[lenRow][lenCol]