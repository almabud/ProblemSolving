class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverse_naive_solution(n)

    def reverse_naive_solution(self, n: int) -> int:
        max_32_bit = 0xffffffff
        res = 0

        for i in range(32):
            res = ((res<<1) | ((n>>i)&1)) & max_32_bit
            print(bin(res))
        
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(225))
