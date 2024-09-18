import pygame
import threading  # Import threading to run music separately
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)    #7 and 30 Algorithm
            game.ai_move(new_board)
        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

# Start the music in a separate thread
music_thread = threading.Thread(target=play_music)
music_thread.start()

main()

# Stop music when the game ends
pygame.mixer.music.stop()
