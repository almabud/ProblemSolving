from typing import List

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python has  infinite  bit limit. So We need to manually limit this to 32bit
        # First we set a mask which binary value will be 2**32 mean 32 number of 1's
        mask = 0xffffffff # this will output '0b11111111111111111111111111111111'
        while b != 0:
            # Calculate the sum
            sum = (a ^ b) & mask
            # Carry
            b = ((a & b) << 1) & mask
            a = sum

            # Check sign bit are set or not. 31th position mean 32 no bit.
            if (a & (1<<31)):
                # Convert the negatic binary to it's actual value in python.a
                a = ~(a ^ mask)

        return a




if __name__ == "__main__":
    s = Solution()
    print(s.getSum(1, -1))