from utils.moveMouse import moveMouse


def draw_maze(screen, wall_texture, floor_texture, exit_image, mouse_image, check_image, block_size, maze_list, mouse_x, mouse_y):
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

    correct_path, visiteds_path = moveMouse(maze_list, mouse_x, mouse_y, exit)

    for path in visiteds_path:
        x, y = path
        if(x == exit["x"] and y == exit["y"]):
            break
        screen.blit(check_image, ( x * block_size,   y * block_size))

    for path in correct_path:
        mouse_x, mouse_y = path
        screen.blit(mouse_image, ( mouse_x * block_size,   mouse_y * block_size))

    
