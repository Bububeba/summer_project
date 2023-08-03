import pygame
import pygame_gui

pygame.init()

# Создание окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Создание менеджера GUI
ui_manager = pygame_gui.UIManager((screen_width, screen_height))

# Создание кнопки "Play"
play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Play',
    manager=ui_manager)

play_button.set_background_colour(pygame.Color('blue'))
# Основной цикл игры
running = True
clock = pygame.time.Clock()

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка событий GUI
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print("Play button pressed!")

        # Обработка событий pygame
        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    # Отрисовка GUI
    ui_manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
