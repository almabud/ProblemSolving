class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        return self.dp_solution(s, 0, dp)
    
    def dp_solution(self, s:str, index=0, dp=[]) -> int:
        if index >= len(s):
            return 1
        if int(s[index]) == 0:
            return 0
        if dp[index]:
            return dp[index]
            
        if index+1 < len(s) and int(s[index]+s[index+1]) <= 26:
            print(s[index], [s[index+1]])
            print("h")
            dp[index] = self.dp_solution(s, index+1, dp) + self.dp_solution(s, index+2, dp)
        else:
            dp[index] = self.dp_solution(s, index+1, dp)
        
        return dp[index]
