import pygame
from utils.drawMaze import draw_maze
from utils.findInitialPosition import find_initial_mouse_position
from utils.message import message
from utils.moveMouse import moveMouse
from utils.openMaze import openMaze
from colorama import init, Fore
init()
pygame.init()

# Set the maze
screen_info = pygame.display.Info()
w_info = screen_info.current_w
h_info = screen_info.current_h

#constants
block_size = 32
fps = 15
maze_list, screen_width, screen_height = openMaze("./mazes/maze4x4.txt", w_info, h_info, block_size)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse and Cheese Maze Game")

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
    try:
        game_exit = False
        finish_game = False

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

            #Draw maze
            exit = draw_maze(screen, wall_texture, floor_texture, exit_image, block_size, maze_list)
            
            # Controlling the mouse movement with the keyboard
            mouse_x, mouse_y = moveMouse(maze_list, mouse_x, mouse_y, exit)

            # Check if the mouse reached the exit
            if maze_list[mouse_y][mouse_x] == "e":
                finish_game = True
            

            # Draw the mouse in the new position
            screen.blit(mouse_image, ( mouse_x * block_size,   mouse_y * block_size))

            pygame.display.update()

            clock.tick(fps)
    except Exception as e:
        print( Fore.RED, e, Fore.RESET)
        
    pygame.quit()

if __name__ == "__main__":
    gameLoop()
