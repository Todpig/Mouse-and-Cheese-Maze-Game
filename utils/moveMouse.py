from time import sleep

def moveMouse(maze_list, mouse_x, mouse_y, exit):
    visiteds = []
    correct_path = []

    while maze_list[mouse_y][mouse_x] != maze_list[exit["y"]][exit["x"]]:
        position = (mouse_x, mouse_y)
        sleep(1)
        print(position)
        visiteds.append(position)
        if maze_list[mouse_y][mouse_x + 1] == "0" and position not in correct_path:
            mouse_x += 1
            correct_path.append(position)
            print("direita")
        elif maze_list[mouse_y][mouse_x - 1] == "0" and position not in correct_path:
            mouse_x -= 1
            correct_path.append(position)
            print("esquerda")
        elif maze_list[mouse_y + 1][mouse_x] == "0" and position not in correct_path:
            mouse_y += 1
            correct_path.append(position)
            print("baixo")
        elif maze_list[mouse_y - 1][mouse_x] == "0" and position not in correct_path:
            mouse_y -= 1
            correct_path.append(position)
            print("cima")

    return mouse_x, mouse_y
