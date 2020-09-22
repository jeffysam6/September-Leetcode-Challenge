class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        from collections import defaultdict
        
        if(len(trips) == 1):
            return trips[0][0] <= capacity
        
        if(len(trips) == 0):
            return True
        
        pickup = defaultdict(list)
        
        dropoff = defaultdict(list)
        
        start,end = float('inf'),float('-inf')
        
    
        trips.sort(key=lambda x:x[1])
        
        for c,pick,drop in trips:
            pickup[pick].append(c)
            dropoff[drop].append(c)
            start = min(start,pick)
            end = max(end,drop)
            
        # print(start,end)
        
        curr = 0
        for i in range(start,end):
            
            curr -= sum(dropoff[i])
            
            curr += sum(pickup[i])
            
            if(curr > capacity):
                return False
        

        return True
        
        