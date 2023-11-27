from collections import deque

def solveMaze(maze_list, mouse_x, mouse_y, exit):
    visiteds_path = deque()
    correct_path = deque()

    def is_valid(x, y):
        return 0 <= x < len(maze_list[0]) and 0 <= y < len(maze_list)

    while (mouse_x, mouse_y) != (exit["x"], exit["y"]):
        position = (mouse_x, mouse_y)
        if maze_list[mouse_y][mouse_x + 1] in ["0", "e"] and (mouse_x + 1, mouse_y) not in visiteds_path and is_valid(mouse_x + 1, mouse_y):
            mouse_x += 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif (mouse_x - 1, mouse_y) not in visiteds_path  and maze_list[mouse_y][mouse_x - 1] in ["0", "e"] and is_valid(mouse_x - 1, mouse_y):
            mouse_x -= 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif maze_list[mouse_y + 1][mouse_x] in ["0", "e"] and (mouse_x, mouse_y + 1) not in visiteds_path and is_valid(mouse_x, mouse_y + 1):
            mouse_y += 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)

        elif maze_list[mouse_y - 1][mouse_x] in ["0", "e"] and (mouse_x, mouse_y - 1) not in visiteds_path and is_valid(mouse_x, mouse_y - 1):
            mouse_y -= 1
            visiteds_path.append((mouse_x, mouse_y))
            correct_path.append(position)
        else:
            if not correct_path:  
                return False
            last_position = correct_path.pop()
            mouse_x, mouse_y = last_position

    return list(correct_path), list(visiteds_path)