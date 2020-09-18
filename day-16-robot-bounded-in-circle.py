class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # instructions = "GL"


        dirs = [0,1]
        x,y = 0,0


        for ins in instructions*4:

            if(ins == 'L'):
                dirs = [-1*dirs[1],dirs[0]]

            elif(ins == 'R'):
                dirs = [dirs[1],-1*dirs[0]]


            elif(ins == 'G'):

                x += dirs[0]
                y += dirs[1]


        if([x,y] == [0,0]):
            return True
        else:
            return False