class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        l = len(nums)//3
        
        c = Counter()
        
        for i in nums:
            
            c[i] += 1
            
            if(len(c) == 3):
                temp = Counter()
                for j in c:
                    c[j] -= 1
                    if(c[j] >=1):
                        temp[j] = c[j]
                
                c = temp
        
        out = []
        for candi in c:
            if(nums.count(candi) > l):
                out.append(candi)
                
        return(out)