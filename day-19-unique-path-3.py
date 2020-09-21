class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        self.c = 0
        
        zeros = 0
        
        n,m = len(grid),len(grid[0])
        
        def find_paths(i,j,empty):
            
            if(i >= n or i<0 or j >= m or j <0 or grid[i][j] < 0):
                return
            
            if(grid[i][j] == 2 and empty == 0):
                self.c += 1
                return
            

            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            
            for dx,dy in dirs:
                temp = grid[i][j]
                grid[i][j] = -2
                find_paths(i+dx,j+dy,empty - 1)
                grid[i][j] = temp
                
                
#             if(i+1 < len(grid[0]) and grid[i+1][j] == 0):
#                 grid[i+1][j] = 1
#                 find_paths(i+1,j,grid)
            
#             if(i-1 >= 0 and grid[i-1][j] == 0):
#                 grid[i-1][j] = 1
#                 find_paths(i-1,j,grid)
                
                
#             if(j+1 < len(grid) and grid[i][j+1] == 0):
#                 grid[i][j+1] = 1
#                 find_paths(i,j+1,grid)
                
#             if(j-1 >= 0 and grid[i][j-1] == 0):
#                 grid[i][j-1] = 1
#                 find_paths(i,j-1,grid)
            
        
                 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j] == 1):
                    sx,sy = i,j
                
                zeros += (grid[i][j] != -1)
                
        find_paths(sx,sy,zeros-1)
        
        return self.c