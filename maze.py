import pygame
from utils.centralizeMaze import centralizeMaze
from utils.drawMaze import draw_maze
from utils.findInitialPosition import find_initial_mouse_position
from utils.message import message

pygame.init()

#constants
screen_width = 800
screen_height = 600
fps = 15
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse and Cheese Maze Game")
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
exit_image = pygame.image.load("./assets/cheese.png")

# Define the game loop
def gameLoop():
    game_exit = False
    finish_game = False

    # Set the maze
    maze_list = []
    with open("maze.txt") as file:
        for line in file:
            maze_list.append(list(line.strip()))

    # Centralize the maze on the screen
    maze_x, maze_y =centralizeMaze(maze_list, block_size, screen_width, screen_height)

    # Find the initial position of the mouse in the maze based on the "maze.txt" file
    mouse_x, mouse_y = find_initial_mouse_position(maze_list)

    # Set the game loop
    while not game_exit:

        # Set the game over loop
        while finish_game == True:
            screen.fill((0, 0, 0))
            if show_message:
                message("You found the exit, press 'C' to continue and 'Q' to quit the game", (255, 0, 0), font, screen, screen_height, screen_width)
            pygame.display.update()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        finish_game = False
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
            finish_game = True

        # Draw the maze
        draw_maze(screen, wall_texture, floor_texture, exit_image, block_size, maze_list, maze_x, maze_y)

        # Draw the mouse in the new position
        screen.blit(mouse_image, (maze_x + mouse_x * block_size, maze_y + mouse_y * block_size))

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()
