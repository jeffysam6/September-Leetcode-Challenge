class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        # pattern = 'aa'
        # string = 'dog dog'

        d = {}

        s = string.split()
        
        if(len(s) != len(pattern)):
            return False
        # print(s)

        for i in range(len(s)):
            if(pattern[i] in d and d[pattern[i]] != s[i]):
                return False
                
            elif(pattern[i] not in d):
                if(s[i] in d.values()):
                    return False
                    
                else:
                    d[pattern[i]] = s[i]
        
        return True