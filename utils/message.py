def message(msg, color, font, screen, screen_height, screen_width):
    """Emits a message on the screen"""
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 2])