class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = float('inf')
        
        prof = 0
        
        
        for i in prices:
            mini = min(i,mini)
            
            prof = max(prof,i-mini)
            
        
        return prof