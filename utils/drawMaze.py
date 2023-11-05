def draw_maze(screen, wall_texture, floor_texture, exit_image, block_size, maze_list, maze_x, maze_y):
    """Draw the maze on the screen"""
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "1":
                screen.blit(wall_texture, (maze_x + column * block_size, maze_y + row * block_size))
            elif maze_list[row][column] == "0":
                screen.blit(floor_texture, (maze_x + column * block_size, maze_y + row * block_size))
            elif maze_list[row][column] == "e":
                screen.blit(exit_image, (maze_x + column * block_size, maze_y + row * block_size))
