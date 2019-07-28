##A knight(a,b) may move on an nxn grid by moving a spaces horizontally and b spaces vertically or b spaces horizontally and a spaces vertically. In other words, a knight(a,b) located at a space in the grid (x,y) may move to a space (x±a,y±b) or (x±b,y±a). To answer the following questions, you will need to determine the shortest path a knight(a,b) may take from space (0,0) in the upper-left corner to space (n−1,n−1) in the lower-right corner on an nxn grid.¶

import numpy as np
# #--------------------------Input variables----------------------------------------------
# initialize the starting point of knight
# start = (0,0)

# # initialise knight's current position
# knight = ()

# # initialise the end point on the board (n*n board)
# size = 5
#--------------------------------------------------------------------------------------------------------------------
#---define function - Required steps to reach a grid-
#--------------------------------------------------------------------------------------------------------------------
def req_steps(start ,knight, size):
    steps = [(start[0],start[1],0)]
    limit = np.inf

    dr = [knight[0],-knight[0],knight[0],-knight[0],knight[1],-knight[1],knight[1],-knight[1]]
    dc = [knight[1],knight[1],-knight[1],-knight[1],knight[0],knight[0],-knight[0],-knight[0]]


    # input character matrix fill it with -1
    mat = np.full((size, size), limit)

    # mark the start position as visited in m
    mat[start[0]][start[1]] = 0



#---------------------------Analysis--------------------------------------------
    def find_step(x,y,s):
        if mat[x][y]>s+1:
            mat[x][y]=s+1
            steps.append((x,y,s+1))

    while len(steps)>0:
        temp=steps[-1]
        x=temp[0]
        y=temp[1]
        s=temp[2]
        steps=steps[:-1]


        for i in range(0,8):
            cal_x = x + dr[i]
            cal_y = y + dc[i]


            if cal_x < 0 or cal_y <0 : continue
            if cal_x > size-1 or cal_y > size-1 : continue
            if mat[cal_x][cal_y] != limit : continue

            find_step(cal_x,cal_y,s)


    return mat

#--------------------------------------------------------------------------------------------------------------------
#---define function - total moves in the shortest path
#--------------------------------------------------------------------------------------------------------------------
def shortest_path_total_moves(size):
    limit =np.inf
    sum_moves=0
    for i in range(0,size):
        for j in range (0,size):
            knight = (i,j)
    #         print('matrix for knight(' + str(i) + ', ' + str(j) +')')
            mat = req_steps(start = (0,0),knight= (knight[0], knight[1]),size=size )
            if mat[size-1][size-1] != limit:
                sum_moves += mat[size-1][size-1]
    return sum_moves

#--------------------------------------------------------------------------------------------------------------------
#---define function - Knights that cannot reach the end point
#--------------------------------------------------------------------------------------------------------------------

def cannot_reach (size):
    limit = np.inf
    counter = 0
    for i in range(1,size):
        for j in range (1,size):
            knight = (i,j)
            mat = req_steps(start = (0,0),knight= (knight[0], knight[1]),size = size)
            if mat[size-1][size-1] == limit:
                counter +=1
    return counter
#--------------------------------------------------------------------------------------------------------------------
#---Answers
#--------------------------------------------------------------------------------------------------------------------

## For n=5, how many moves are in the shortest path for knight(1,2)?
a = req_steps(start = (0,0),knight= (1,2),size=5 )
a[4][4]


## how many knights with 0 <a<=b cannot reach (4,4)?
cannot_reach(5)

## For n=5, what is the sum of the number of moves for the shortest paths for all knights with a<=b?
shortest_path_total_moves(5)

## For n=25, how many moves are in the shortest path for knight(4,7)?
size=25
mat = req_steps(start = (0,0),knight= (4,7),size=25 )
mat[size-1][size-1]
## For n=25, what is the sum of the number of moves for the shortest paths for all knights with a<=b?
shortest_path_total_moves(25)

##For n=25, how many knights with 0<a<=b cannot reach (24,24)?
cannot_reach(25)

###For n=1000, how many moves are in the shortest path for knight(13,23)?
mat = req_steps(start = (0,0),knight= (13,23),size=1000 )
mat[size-1][size-1]


##For n=10000, how many moves are in the shortest path for knight(73,101)
mat = req_steps(start = (0,0),knight= (73,101),size=10000 )
 mat[size-1][size-1]
