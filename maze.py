import os
from time import sleep
import pygame
from utils.drawMaze import draw_maze
from utils.findInitialPosition import find_initial_mouse_position, find_initial_exit_position
from utils.message import message
from utils.solveMaze import solveMaze
from utils.openMaze import openMaze
from utils.constants import constants
import argparse
from colorama import init, Fore
init()
def initPygame():
    pygame.init()
    # Set the maze
    screen_info = pygame.display.Info()
    w_info = screen_info.current_w
    h_info = screen_info.current_h
    # Set the clock
    clock = pygame.time.Clock()

    # Define a font
    font = pygame.font.Font(None, 28)
    
    #laod music
    pygame.mixer.music.load('./assets/audio/audioPlay.mp3')

    # Load show_message = Truefloor and wall textures
    floor_texture = pygame.image.load("./assets/img/floor.png")
    wall_texture = pygame.image.load("./assets/img/wall.png")

    # Load mouse and exit images
    mouse_image = pygame.image.load("./assets/img/mouse.png")
    cheese_image = pygame.image.load("./assets/img/cheese.png")
    check_image = pygame.image.load("./assets/img/check.png")
    
    return w_info, h_info, clock, font, floor_texture, wall_texture, mouse_image, cheese_image, check_image
    
#get args to terminal for get path maze
parser = argparse.ArgumentParser(description='Script para executar o jogo do labirinto em Pygame.')
parser.add_argument('arquivo', help='Nome do arquivo do labirinto dentro da pasta "mazes"')
args = parser.parse_args()
constants["PATH_MAZE"] = os.path.join('./mazes', args.arquivo)

#constants
block_size = 32
fps = 15
show_message = True


# Define the game loop
def gameLoop():
    try:
        constants["FINISH"] = False
        w_info, h_info, clock, font, floor_texture, wall_texture, mouse_image, cheese_image, check_image = initPygame()
        maze_list, screen_width, screen_height = openMaze(constants["PATH_MAZE"], w_info, h_info, block_size)
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Mouse and Cheese Maze Game")
        game_exit = False

        # Find the initial position of the mouse in the maze based on the "maze.txt" file
        mouse_x, mouse_y = find_initial_mouse_position(maze_list)
        exit_x, exit_y = find_initial_exit_position(maze_list)

        # Set the game loop
        while not game_exit:
            pygame.mixer.music.play()

            # Set the game over loop
            while constants["FINISH"] == True:
                screen.fill((0, 0, 0))
                if show_message:
                    message("press 'P' to play or 'Q' to quit the game", (255, 0, 0), font, screen, screen_height, screen_width)
                pygame.display.update()

                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_exit = True
                            pygame.quit()
                        if event.key == pygame.K_p:
                            gameLoop()
                pygame.display.update()

            
            # Draw maze
            draw_maze(screen, constants["BLOCK_SIZE"], maze_list, floor_texture, wall_texture, cheese_image, exit_x, exit_y)
            
            correct_path, visiteds_path = solveMaze(maze_list, mouse_x, mouse_y, {"x": exit_x, "y": exit_y})
            
            if len(correct_path) > 0 or len(visiteds_path) > 0:
                for path in correct_path:
                    mouse_x, mouse_y = path 
                    #time to render positions             
                    sleep(0.2)
                    screen.blit(mouse_image, (mouse_x * block_size, mouse_y * block_size))
                    pygame.display.update()
                #render paths not visiteds and not in correct paths
                for path in visiteds_path:
                    if path not in correct_path:
                        p_x, p_y = path
                        if p_x == exit_x and p_y == exit_y:
                            break
                        screen.blit(check_image, (p_x * block_size, p_y * block_size))                     
                    pygame.display.update()
                sleep(5)
                constants["FINISH"] = True

                
            clock.tick(constants["FPS"])
    except Exception as e:
        print(Fore.RED, e, Fore.RESET)
        
    pygame.quit()

if __name__ == "__main__":
    gameLoop()
