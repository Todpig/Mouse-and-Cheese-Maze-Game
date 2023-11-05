import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window
pygame.display.set_caption("Mouse and Cheese Maze Game")

# Set the block size
block_size = 20

# Set the clock
clock = pygame.time.Clock()

# Define a font
font = pygame.font.Font(None, 28)
show_message = True

# Load floor and wall textures
floor_texture = pygame.image.load("./assets/floor.png")
wall_texture = pygame.image.load("./assets/wall.png")

# Load mouse and exit images
mouse_image = pygame.image.load("./assets/mouse.png")
exit_image = pygame.image.load("./assets/pipe.png")

# Define the game loop
def gameLoop():
    game_exit = False
    game_over = False

    # Set the maze
    maze_list = []
    with open("maze.txt") as file:
        for line in file:
            maze_list.append(list(line.strip()))  # Remove any newline characters and convert to a list

    # Centralize the maze on the screen
    maze_width = len(maze_list[0]) * block_size
    maze_height = len(maze_list) * block_size
    maze_x = (screen_width - maze_width) // 2
    maze_y = (screen_height - maze_height) // 2

    # Find the initial position of the mouse in the maze based on the "maze.txt" file
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            if maze_list[row][column] == "m":
                maze_list[row] = maze_list[row][:column] + ["0"] + maze_list[row][column+1:]
                mouse_x = column
                mouse_y = row

    # Set the game loop
    while not game_exit:

        # Set the game over loop
        while game_over == True:
            screen.fill((0, 0, 0))
            if show_message:
                message("You found the exit, press 'C' to continue and 'Q' to quit the game", (255, 0, 0), font)
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Controlling the mouse movement with the keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            next_x = mouse_x - 1
            if maze_list[mouse_y][next_x] in ["0", "e"]:
                maze_list[mouse_y][mouse_x] = "0"
                mouse_x = next_x
        if keys[pygame.K_RIGHT]:
            next_x = mouse_x + 1
            if maze_list[mouse_y][next_x] in ["0", "e"]:
                maze_list[mouse_y][mouse_x] = "0"
                mouse_x = next_x
        if keys[pygame.K_UP]:
            next_y = mouse_y - 1
            if maze_list[next_y][mouse_x] in ["0", "e"]:
                maze_list[mouse_y][mouse_x] = "0"
                mouse_y = next_y
        if keys[pygame.K_DOWN]:
            next_y = mouse_y + 1
            if maze_list[next_y][mouse_x] in ["0", "e"]:
                maze_list[mouse_y][mouse_x] = "0"
                mouse_y = next_y

        # Check if the mouse reached the exit
        if maze_list[mouse_y][mouse_x] == "e":
            game_over = True

        # Draw the maze
        for row in range(len(maze_list)):
            for column in range(len(maze_list[row])):
                if maze_list[row][column] == "1":
                    screen.blit(wall_texture, (maze_x + column * block_size, maze_y + row * block_size))
                elif maze_list[row][column] == "0":
                    screen.blit(floor_texture, (maze_x + column * block_size, maze_y + row * block_size))
                elif maze_list[row][column] == "e":
                    screen.blit(exit_image, (maze_x + column * block_size, maze_y + row * block_size))

        # Draw the mouse in the new position
        screen.blit(mouse_image, (maze_x + mouse_x * block_size, maze_y + mouse_y * block_size))

        # Update the screen
        pygame.display.update()

        # Set the frames per second
        clock.tick(15)

    # Quit Pygame
    pygame.quit()

# Define the message function
def message(msg, color, font):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 2])

# Call the game loop
gameLoop()
