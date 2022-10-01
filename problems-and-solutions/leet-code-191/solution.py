from typing import List

class Solution:
    def __init__(self):
        self.mark_array = self.create_lookup_table()
    
    def hammingWeight(self, n: int) -> int:
        return self.look_up_table(n)

    def naive_solution(self, n: int) -> int:
        n = int(n, 2)
        count_set_bit = 0
        while n:
            if n & 1:
                count_set_bit += 1
            n >>= 1

        return count_set_bit
    
    def karnighan_algorithm(self, n: int) -> int:
        """
        Idea is to unset the set bit from the right side. 
        We can do this by `x & (x-1)` and count each time.
        """

        bit_set_count = 0
        while n:
            n = n & (n-1)
            bit_set_count += 1
        
        return bit_set_count
    
    def look_up_table(self, n: int) -> int:
        # The mark aray is devide by 8 bit.
        # 8 bit max number
        max_8_bit = 0xff
        res = (
            self.mark_array[n&max_8_bit] # 8 bit
            + self.mark_array[(n>>8)&max_8_bit] # next 8 bit
            + self.mark_array[(n>>16)&max_8_bit] # next 8 bit
            + self.mark_array[(n>>24)&max_8_bit] # last 8 bit
        )
        return res

    def create_lookup_table(self) -> List:
        # Unsigned 8 bit number can sotore upto 2**(8-1) = 256.
        mark_array = [0] * 256
        # binary 0 have no set bit.
        mark_array[0] = 0
        # Don't need to calculate 0's count as we get that already.
        for i in range(1,256):
            # Right shift the i and we can see that this value is already counted. So no need to count this again.
            # Right shift i means i>>1 = i/2
            # We just need the last bit count.
            mark_array[i] = mark_array[i//2] + (i&1)
        
        return mark_array




if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(int('000000000000000001110110100010001', 2)))