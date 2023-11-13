def draw_maze(screen, block_size, maze_list, floor_texture, wall_texture, cheese_image, exit_x, exit_y):
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "1":
                screen.blit(wall_texture, (column * block_size, row * block_size))
            elif maze_list[row][column] == "0":
                screen.blit(floor_texture, (column * block_size, row * block_size))
    #draw exit/cheese
    if exit_y < len(maze_list) and exit_x < len(maze_list[0]):
        screen.blit(cheese_image, (exit_x * block_size, exit_y * block_size))
