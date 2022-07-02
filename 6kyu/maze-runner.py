def maze_runner(maze, directions):
    starti = 0
    startj = 0
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                starti = i
                startj = j
                
    for dir in directions:
        if dir == "N":
            starti -= 1
        elif dir == "S":
            starti += 1
        elif dir == "W":
            startj -= 1
        elif dir == "E":
            startj += 1
            
        if starti < 0 or startj < 0 or starti > len(maze)-1 or startj > len(maze)-1 or maze[starti][startj] == 1:
            return 'Dead'
        if maze[starti][startj] == 3:
            return 'Finish'
    
    return 'Lost'
