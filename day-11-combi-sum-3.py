class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        
        
        def combi(start,arr,target):
            
            if(len(arr) == k):
                if(target == 0):
                    ans.append(arr)
                return
            
            
            for i in range(start+1,10):
                combi(i,arr+[i],target - i)
            
            
        
        
        combi(0,[],n)
        
        
        return ans