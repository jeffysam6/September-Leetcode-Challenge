class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from collections import Counter


        c1 = Counter(arr)

        hours = 23
        minutes= 59
        
        if(arr == [0,0,0,0]):
            return "00:00"

        while(hours > 0):
            temp = Counter((map(int,str(hours).zfill(2)+str(minutes).zfill(2))))
            if(temp == c1):
                # print(temp,c1)
                return(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}")
        

            minutes -= 1

            if(minutes < 0):
                hours -= 1
                minutes = 59
        
        return ""
