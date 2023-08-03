import pygame
import sys
from button import Button
#from map_test import *
from main import *

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("fonts\\Pixeloza03.ttf", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(200, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/move_right_1.png"), pos=(140, 300),
                             text_input="PLAY", font=get_font(120), base_color="white", hovering_color="green")
        CONTINUE_BUTTON = Button(image=pygame.image.load("images/move_right_1.png"), pos=(213, 450),
                                 text_input="CONTINUE", font=get_font(120), base_color="white", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("images/move_right_1.png"), pos=(135, 600),
                             text_input="QUIT", font=get_font(120), base_color="white", hovering_color="green")

        # SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CONTINUE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game(0)
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game(1)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
