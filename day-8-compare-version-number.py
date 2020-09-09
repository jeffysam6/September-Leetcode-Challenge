class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        
        v2 = version2.split('.')
        
        max_length = max(len(v1),len(v2))
        
        def filtered(version):
            temp = []
            for i in version:
                if(i.count('0') != len(i)):
                    temp.append(int(i.lstrip('0')))
                else:
                    temp.append(0)
            
            if(len(version) < max_length):
                temp += [0]*(max_length-len(version))
            
            return temp
                    
        
        v1,v2 = filtered(v1),filtered(v2)
        
        
        index = 0
        # print(v1,v2)
        
        while(index < min(len(v1),len(v2))):
            
            if(v1[index]<v2[index]):
                return -1
            
            elif(v1[index] > v2[index]):
                return 1
            
            index += 1

        
        return 0
            
        
            
        