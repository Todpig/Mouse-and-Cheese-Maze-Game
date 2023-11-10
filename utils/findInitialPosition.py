def find_initial_mouse_position(maze_list):
    """find the initial position of the mouse in the maze"""
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "m":
                maze_list[row] = maze_list[row][:column] + ["0"] + maze_list[row][column+1:]
                return column, row

def find_initial_exit_position(maze_list):
    """find the initial position of the mouse in the maze"""
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "e":
                maze_list[row] = maze_list[row][:column] + ["0"] + maze_list[row][column+1:]
                return column, row