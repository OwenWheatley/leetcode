class Solution:
    def possibleStringCount(self, word: str) -> int:
        if not word:
            return 0
        
        possible_count = 1
        
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            consecutive_count = j - i
            
            if consecutive_count > 1:
                possible_count += consecutive_count - 1
            
            i = j
            
        return possible_count