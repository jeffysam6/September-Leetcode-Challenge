class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 0):
            return 0
        
        if(len(nums) <= 2):
            return max(nums)
        
        max_till_now = nums[0]
        
        ptr = 0
        
        for i in range(2,len(nums)):
            nums[i] += max_till_now
            ptr += 1
            max_till_now = max(max_till_now,nums[ptr])
        
        
        return max(max_till_now,nums[-1])