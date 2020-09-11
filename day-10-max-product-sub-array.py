class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        
        B = arr[::-1]
        A = arr
        
        
        def find_max(A):
            maxi = max(A[0],float('-inf'))
            for i in range(1,len(A)):

                if(A[i-1] != 0):
                    A[i] = A[i] * A[i-1]

                if(A[i]> maxi):
                    maxi = A[i]
            
            return maxi
        
        
        return max(find_max(A),find_max(B))
        
        