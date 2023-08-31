class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.bit_solv(s, t)
    
    def mark_array_sol(self, s: str, t: str) -> bool:
        # Len is not same then it is not a valid anagram.
        if len(s) != len(t):
            return False
        
        # Initialize mark array
        mark_arr1 = [0] * 256
        mark_arr2 = [0] * 256
        
        for key, val in enumerate(s):
            mark_arr1[ord(val)] += 1
            mark_arr2[ord(t[key])] += 1
        
        for key, val in enumerate(mark_arr1):
            if val != mark_arr2[key]:
                return False
        
        return True


    def sort_solv(self, s: str, t: str) -> bool:
        # Len is not same then it is not a valid anagram.
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)


    

if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram('abcda', 'adcab'))
        