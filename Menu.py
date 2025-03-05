import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")
        self.react = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load("./asset/Menu.mp3")
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.react)

            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(20, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + i * 25))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
