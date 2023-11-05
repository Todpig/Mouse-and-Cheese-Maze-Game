def centralizeMaze(maze_list, block_size, screen_width, screen_height):
    """Centralize the maze on the screen, first maze_x and maze_y"""
    maze_width = len(maze_list[0]) * block_size
    maze_height = len(maze_list) * block_size
    return  (screen_width - maze_width) // 2, (screen_height - maze_height) // 2