class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case 
        if len(s) != len(t):
            return False 

        counts = [0] * 26 

        for ch_s, ch_t in zip(s, t):
            counts[ord(ch_s) - ord('a')] += 1 
            counts[ord(ch_t) - ord('a')] -= 1 
        
        return all(c == 0 for c in counts)

    
        