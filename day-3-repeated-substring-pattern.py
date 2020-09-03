class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(len(s)-1):
            sub_str = s[:i+1]
            
            multiplier = len(s)//len(sub_str)
            
            result = sub_str * multiplier
            
            if(result == s):
                return True