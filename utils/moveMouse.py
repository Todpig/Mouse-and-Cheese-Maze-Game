def moveMouse(maze_list, mouse_x, mouse_y, exit):
    visiteds_path = []
    correct_path = []
    while maze_list[mouse_y][mouse_x] != maze_list[exit["y"]][exit["x"]]:
        position = (mouse_x, mouse_y)
        
        if maze_list[mouse_y][mouse_x+1] in ["0", "e"] and (mouse_x + 1, mouse_y) not in visiteds_path:
            mouse_x += 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif maze_list[mouse_y][mouse_x-1] in ["0", "e"] and (mouse_x - 1, mouse_y) not in visiteds_path:
            mouse_x -= 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif maze_list[mouse_y+1][mouse_x] in ["0", "e"] and (mouse_x, mouse_y + 1) not in visiteds_path:
            mouse_y += 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif maze_list[mouse_y-1][mouse_x] in ["0", "e"] and (mouse_x, mouse_y - 1) not in visiteds_path:
            mouse_y -= 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)
        else:
            last_position = correct_path.pop()
            mouse_x, mouse_y = last_position

    return correct_path, visiteds_path

   
