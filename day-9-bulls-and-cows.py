class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        from collections import Counter
        
        cows,bulls = 0,0
        
        c = Counter(secret)
        
        # print(c)
        ptr = [False]*len(secret)
        
        for i in range(len(secret)):
            # print(c)
            if(secret[i] == guess[i]):
                ptr[i] = True
                bulls += 1
                c[secret[i]] -= 1
                
                if(c[secret[i]] == 0):
                    del c[secret[i]]
                    
        for i in range(len(secret)):
            
            if(ptr[i]==False and guess[i] in c):
                cows += 1
                c[guess[i]] -= 1
                if(c[guess[i]] == 0):
                    del c[guess[i]]
        
        
        return f'{bulls}A{cows}B'