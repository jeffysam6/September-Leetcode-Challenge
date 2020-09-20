class Solution:
    def sequentialDigits(self, low, high):
        
        ans = []
        
        def find_rest(tot):
            
            # if()
            
            if(low<=tot<=high):
                ans.append(tot)
                
            elif(tot>high):
                return
            
            if(tot%10 + 1 == 10):
                return 
                
            
            find_rest(tot*10 + (tot%10 +1))
        
        for i in range(1,9):
            # print(i)
            find_rest(i)
        
        
        return(sorted(ans))