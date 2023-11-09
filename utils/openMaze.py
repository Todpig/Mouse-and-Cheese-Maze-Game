def openMaze(name, w_info, h_info, block_size):
    try:
        maze_list = []
        with open(name) as file:
            text = file.readline()
            text = text.split(" ")
            for line in file:
                maze_list.append(list(line.strip()))
            if int(text[0]) * block_size > w_info or int(text[1]) * block_size > h_info:
                raise Exception("The maze is too big for the screen!")
        return maze_list, int(text[0])* 32, int(text[1]) *32
    except: 
        print("Width or heigth not allowed!")
        return