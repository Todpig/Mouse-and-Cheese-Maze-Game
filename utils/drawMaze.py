def draw_maze(screen, wall_texture, floor_texture, exit_image, block_size, maze_list):
    """Draw the maze on the screen"""
    exit = {
        "x": 0,
        "y": 0
    }
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "1":
                screen.blit(wall_texture, (  column * block_size,   row * block_size))
            elif maze_list[row][column] == "0":
                screen.blit(floor_texture, (  column * block_size,   row * block_size))
            elif maze_list[row][column] == "e":
                screen.blit(exit_image, (  column * block_size,   row * block_size))
                exit["x"] = column
                exit["y"] = row
    return exit
