
def openMaze(name, w_info, h_info, block_size):
    try:
        maze_list = []
        width = 0
        heigth = 0
        with open(name) as file:
            text = file.readline()
            text = text.split(" ")
            width = int(text[0])
            heigth = int(text[1])
            for line in file:
                maze_list.append(list(line.strip()))
            if int(text[0]) * block_size > w_info:
                width = 60
            if  int(text[1]) * block_size > h_info:
                heigth = 60
        return maze_list, width* 32, heigth *32
    except: 
        print("Width or heigth not allowed!")
        return