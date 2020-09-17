class Trie:       
    def __init__(self):
        self.children = {}

class Solution:
    
    def __init__(self):
        self.root = Trie()
        
    
    def insert_nums(self,num):
        bit_num = bin(num)[2:].zfill(32)
        
        curr = self.root
        
        for bit in bit_num:
            
            if(bit not in curr.children):
                curr.children[bit] = Trie()
            
            curr = curr.children[bit]
    
    def find_max_xor(self,num):
        bit_num = bin(num)[2:].zfill(32)
        
        curr = self.root
        
        maxi_xor = ''
        
        for bit in bit_num:
            
            if(bit == '0'):
                oppo = '1'
            
            elif(bit == '1'):
                oppo = '0'
            
            if(oppo in curr.children):
                maxi_xor += oppo
                curr = curr.children[oppo]
            
            else:
                maxi_xor += bit
                curr = curr.children[bit]
        
        return int(maxi_xor,2) ^ num
        
        
        
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        for num in nums:
            self.insert_nums(num)
        
        maxi = 0
        
        for num in nums:
            maxi = max(maxi,self.find_max_xor(num))
        
        return maxi