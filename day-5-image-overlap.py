class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        from collections import defaultdict

        arr1,arr2 = [],[]

        d = defaultdict(int)

        for i in range(len(A)):
            for j in range(len(B)):
                if(A[i][j]):
                    arr1.append((i,j))

                if(B[i][j]):
                    arr2.append((i,j))

        for ra,ca in arr1:
            for rb,cb in arr2:
                d[(rb-ra,cb-ca)] += 1

        return(max(d.values() or [0]))


        # print(arr1,arr2)