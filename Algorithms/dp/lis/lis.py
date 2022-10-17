from typing import List

class LIS:
    def find_LIS(self, seq: List[int]) -> int:
        return self.LIS_n_log_n(seq)
    
    def find_recursive_LIS_v1(self, seq: List[int]) -> int:
        """
            Find the LIS for every position.
        """

        ans = 0
        dp = [-1] * len(seq)
        for i, val in enumerate(seq):
            ans = max(ans, self.recursive_dp_LIS_v1(seq, i, dp))
        
        return ans
    
    def recursive_dp_LIS_v1(self, seq: List[int], index: int, dp: List[int]) -> int:
        if dp[index] != -1:
            return dp[index]
        # Declare the res with inital value.
        ans = 0
        for j in range(index+1, len(seq)):
            if seq[j] > seq[index]:
                ans =  max(ans, self.recursive_dp_LIS_v1(seq, j, dp))

        # Add the 1st value  for the starting point.
        dp[index] = ans + 1

        return dp[index]
    
    def LIS_n_square(self, seq: List[int]):
        max_int = 999999
        min_int = -999999

        # Initialize the d
        d = [max_int] * (len(seq) + 1)
        d[0] = min_int

        for seq_val in seq:
            # Finding the suitable position for seq_val
            for j in range(1, len(d)):
                if d[j-1] < seq_val < d[j]:
                    d[j] = seq_val
        
        lis = 0
        for index, val in enumerate(d):
            if val < max_int:
                lis = index
        
        return lis
    
    def LIS_n_log_n(self, seq: List[int]):
        max_int = 999999
        min_int = -999999

        # Initialize the d
        d = [max_int] * (len(seq) + 1)
        d[0] = min_int

        def find_the_suitable_position(key: int) -> int:
            left = 0
            right = len(d) - 1
            
            while(right-left>1):
                mid = left + (right-left) // 2

                if key <= d[mid] <= max_int:
                    right = mid
                else:
                    left = mid
            
            return right

        for seq_val in seq:
            # Finding the suitable position for seq_val
            d[find_the_suitable_position(seq_val)] = seq_val
        
        lis = 0
        for index, val in enumerate(d):
            if val < max_int:
                lis = index
        return lis
        

if  __name__ == "__main__":
    s = LIS()
    print(s.find_LIS([4,10,4,3,8,9]))
