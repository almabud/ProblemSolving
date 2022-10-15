from typing import List

class LCS:
    def find_lcs(self, seq_1:str, seq_2: str) -> int:
        return self.lcs_recursive_dp(seq_1, seq_2)

    def lcs_recursive(self, seq_1: List[int], seq_2: List[int], index_i=0, index_j=0) -> int:
        # If any index is goes to the corespoinding sequence end then return 0.
        if index_i >= len(seq_1) or index_j >= len(seq_2):
            return 0
        
        # Storing the ans
        ans = 0
        # Situation for both are same
        if seq_1[index_i] == seq_2[index_j]:
            ans = 1 + self.lcs_recursive(seq_1, seq_2, index_i+1, index_j+1)
        
        else:
            ans = max(
                self.lcs_recursive(seq_1, seq_2, index_i, index_j+1),
                self.lcs_recursive(seq_1, seq_2, index_i+1, index_j)
            )
        
        return ans
    
    def lcs_recursive_dp(self, seq_1: str, seq_2: str, index_i=0, index_j=0, dp=[]) -> int:
        # Initialize the dp
        if not len(dp):
            dp = [[-1 for x in range(len(seq_2))] for y in range(len(seq_1))]
        # If any index is goes to the corespoinding sequence end then return 0.
        if index_i >= len(seq_1) or index_j >= len(seq_2):
            return 0
        if dp[index_i][index_j] != -1:
            return dp[index_i][index_j]
        # Storing the ans
        ans = 0
        # Find LCS when both char is same.
        if seq_1[index_i] == seq_2[index_j]:
            ans = 1 + self.lcs_recursive_dp(seq_1, seq_2, index_i+1, index_j+1, dp)
        # Find LCS when both char is not same.
        else:
            ans = max(
                self.lcs_recursive_dp(seq_1, seq_2, index_i, index_j+1, dp),
                self.lcs_recursive_dp(seq_1, seq_2, index_i+1, index_j, dp)
            )
        dp[index_i][index_j] = ans

        return dp[index_i][index_j]
    
    def lcs_iterative_dp(self, seq_1: str, seq_2: str) -> int:
        # Initialize the dp
        dp = [[0]*10000]*10000

        # Another way is to start from end to start. Then this language chages will not occure.
        for i, val_i in enumerate(seq_1):
            for j, val_j in enumerate(seq_2):
                if val_i == val_j:
                    # For other language this need to change. AS dp[-1][-1] mean the last value of the dp.
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # For other language this need to change. As explain above.
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[len(seq_1)-1][len(seq_2)-1]


if __name__ == "__main__":
    s = LCS()
    print(s.find_lcs("oxcpqrsvwf", "shmtulqrypy"))
        


