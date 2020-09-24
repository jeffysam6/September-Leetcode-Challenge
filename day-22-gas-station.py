class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        curr = 0
        diff = 0
        for i in range(len(gas)):
            curr += gas[i]
            
            if(curr >= cost[i]):
                curr -= cost[i]
            
            else:
                diff += cost[i] - curr
                start = i + 1
                curr = 0
        
        if(start == len(gas) or curr < diff):
            return -1
        
        return start
                
        # ans = []
                
        # if(start is []):
        #     return -1
            
#         def loop_through(index):  
#             c = (len(gas)-index) + index
#             curr = 0
#             out = index
#             while(c > 0):
#                 curr += diff[index]

#                 if(curr < 0 ):
#                     return -1

#                 index += 1

#                 index = index%len(gas)

#                 c -= 1
            
#             return index
            
        # print(diff)
#         for i in start:
#             # print(i,sum(diff[i+1:]),sum(diff[:i]))
#             ans.append(sum(diff[i+1:]) + sum(diff[:i])+diff[i])
            
#         # print(start,ans,diff)
#         for i in range(len(ans)):
#             if(ans[i] >= 0):
#                 return start[i]
        
        # return -1
            
            
        # print(ans)
        
        # return ans
            
            