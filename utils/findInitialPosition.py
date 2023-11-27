def find_initial_mouse_position(maze_list):
    """find the initial position of the mouse in the maze"""
    existsMouse = False
    mouse_c = 0
    mouse_r = 0
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "m":
                maze_list[row] = maze_list[row][:column] + ["0"] + maze_list[row][column+1:]
                existsMouse = True 
                mouse_c = column
                mouse_r = row
    if(existsMouse==True):
        return mouse_c, mouse_r
    else:
        raise Exception("Mouse not found!")    

def find_initial_exit_position(maze_list):
    """find the initial position of the exit in the maze"""
    existsExit = False
    exit_c = 0
    exit_r = 0
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "e":
                maze_list[row] = maze_list[row][:column] + ["0"] + maze_list[row][column+1:]
                existsExit = True
                exit_c = column
                exit_r = row

    if(existsExit ==True):
        return exit_c, exit_r
    else:
        raise Exception("Exit not found!") 