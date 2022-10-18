from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mark = [False] * len(s)
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i+len(word)) <= len(s) and word == s[i:i+len(word)]:
                    if i+len(word) == len(s):
                        mark[i] = True
                    # Check if breaking point is true or not
                    elif mark[i+len(word)]:
                        mark[i] = True

        if mark[0]:
            return True
        
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("applepenapple", ["apple","pen"]))
