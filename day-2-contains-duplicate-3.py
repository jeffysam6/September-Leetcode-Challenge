class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        l = len(nums)
        
        if(t == 0 and l == len(set(nums))):
            return False
        
        for i in range(len(nums)):
            
            for j in range(i+1,i+1+k):
                
                if(j>=l):
                    break
                
                if(abs(nums[i]-nums[j]) <= t):
                    return True
        
        return False
                