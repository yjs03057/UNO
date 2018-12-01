import sys
import pygame
from pygame.locals import *
import startgame

img_basic_address = './img/'

class UNOGame():
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(img_basic_address+'background.png')
        self.screen_width = 800
        self.screen_height = 600
        self.background_Color = (0,66,0)
        self.playernum = 2
        self.difficulty = 1
        self.font = 'Berlin Sans FB'
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.background_Color)
        self.screen.blit(self.background, (-30, -30))
        pygame.display.update()

    def text_format(self, message, textFont, textSize, textColor):
        newFont = pygame.font.SysFont(textFont, textSize)
        newText = newFont.render(message, K_0, textColor)
        return newText

    def set_players(self):
        pygame.init()
        self.background = pygame.image.load('./img/default.png')
        self.screen.blit(self.background, (-100, -70))
        selected = 1
        menu = True
        while menu:
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.init()
            sound = pygame.mixer.Sound('./sound/menu.wav')
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        sound.play()
                        if selected <=1:
                            selected = 1
                        else:
                            selected = selected-1
                    elif event.key == K_DOWN:
                        sound.play()
                        if selected >=4:
                            selected = 4
                        else:
                            selected = selected+1
                    if event.key == K_RETURN:
                        if selected <= 1:
                            self.playernum = 2
                            self.background = pygame.image.load('./img/background.png')
                            return
                        if selected == 2:
                            self.playernum = 3
                            self.background = pygame.image.load('./img/background.png')
                            return
                        if selected == 3:
                            self.playernum = 4
                            self.background = pygame.image.load('./img/background.png')
                            return
                        if selected >= 4:
                            self.background = pygame.image.load('./img/background.png')
                            return
           
            if selected == 1:
                text_two = self.text_format("2 PLAYERS", self.font, 50, (255,24,0))
            else:
                text_two = self.text_format("2 PLAYERS", self.font, 50, (0,0,0))
            if selected == 2:
                text_three = self.text_format("3 PLAYERS", self.font, 50, (255,24,0))
            else:
                text_three = self.text_format("3 PLAYERS", self.font, 50, (0,0,0))
            if selected == 3:
                text_four = self.text_format("4 PLAYERS", self.font, 50, (255,24,0))
            else:
                text_four = self.text_format("4 PLAYERS", self.font, 50, (0,0,0))
            if selected == 4:
                text_quit = self.text_format("BACK", self.font, 50, (255,24,0))
            else:
                text_quit = self.text_format("BACK", self.font, 50, (0,0,0))

            two_rect = text_two.get_rect()
            three_rect = text_three.get_rect()
            four_rect = text_four.get_rect()
            quit_rect=text_quit.get_rect()

            self.screen.blit(text_two, (self.screen_width/2 - (two_rect[2]/2), 180))
            self.screen.blit(text_three, (self.screen_width/2 - (three_rect[2]/2), 240))
            self.screen.blit(text_four, (self.screen_width/2 - (four_rect[2]/2), 300))
            self.screen.blit(text_quit, (self.screen_width/2 - (quit_rect[2]/2), 360))
            pygame.display.update()

    def set_difficulty(self):
        self.background = pygame.image.load('./img/default.png')
        self.screen.blit(self.background, (-100, -70))
        selected = 1
        menu = True
        while menu:
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.init()
            sound = pygame.mixer.Sound('./sound/menu.wav')
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        sound.play()
                        if selected <=1:
                            selected = 1
                        else:
                            selected = selected-1
                    elif event.key == K_DOWN:
                        sound.play()
                        if selected >=3:
                            selected = 3
                        else:
                            selected = selected+1
                    if event.key == K_RETURN:
                        if selected <= 1:
                            self.difficulty = 1
                            self.background = pygame.image.load('./img/background.png')
                            return
                        if selected == 2:
                            self.difficulty = 2
                            self.background = pygame.image.load('./img/background.png')
                            return
                        if selected >= 3:
                            self.background = pygame.image.load('./img/background.png')
                            return
           
            if selected == 1:
                text_basic = self.text_format("BASIC MODE", self.font, 50, (255,24,0))
            else:
                text_basic = self.text_format("BASIC MODE", self.font, 50, (0,0,0))
            if selected == 2:
                text_advanced = self.text_format("ADVANCED MODE", self.font, 50, (255,24,0))
            else:
                text_advanced = self.text_format("ADVANCED MODE", self.font, 50, (0,0,0))
            if selected == 3:
                text_quit = self.text_format("BACK", self.font, 50, (255,24,0))
            else:
                text_quit = self.text_format("BACK", self.font, 50, (0,0,0))

            basic_rect = text_basic.get_rect()
            advanced_rect = text_advanced.get_rect()
            quit_rect=text_quit.get_rect()

            self.screen.blit(text_basic, (self.screen_width/2 - (basic_rect[2]/2), 200))
            self.screen.blit(text_advanced, (self.screen_width/2 - (advanced_rect[2]/2), 260))
            self.screen.blit(text_quit, (self.screen_width/2 - (quit_rect[2]/2), 320))
            pygame.display.update()

    def main_menu(self):
        menu = True
        selected = 1
        while menu:
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.init()
            sound = pygame.mixer.Sound('./sound/menu.wav')
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        sound.play()
                        if selected <=1:
                            selected = 1
                        else:
                            selected = selected-1
                    elif event.key == K_DOWN:
                        sound.play()
                        if selected >=4:
                            selected = 4
                        else:
                            selected = selected+1
                    if event.key == K_RETURN:
                        if selected <= 1:
                            self.background = pygame.image.load('./img/default.png')
                            self.screen.blit(self.background, (-30, -30))
                            game = startgame.game(self.playernum, self.difficulty)
                            game.startgame()
                            self.background = pygame.image.load('./img/background.png')
                            self.screen.blit(self.background, (-30, -30))
                        if selected == 2:
                            self.set_players()
                            self.screen.blit(self.background, (-30, -30))
                        if selected == 3:
                            self.set_difficulty()
                            self.screen.blit(self.background, (-30, -30))
                        if selected >= 4:
                            pygame.quit()
                            sys.exit()
           
            if selected == 1:
                text_start = self.text_format("START", self.font, 50, (255,24,0))
            else:
                text_start = self.text_format("START", self.font, 50, (0,0,0))
            if selected == 2:
                text_player = self.text_format("PLAYERS SET", self.font, 50, (255,24,0))
            else:
                text_player = self.text_format("PLAYERS SET", self.font, 50, (0,0,0))
            if selected == 3:
                text_dfficulty = self.text_format("DIFFICULTY SET", self.font, 50, (255,24,0))
            else:
                text_dfficulty = self.text_format("DIFFICULTY SET", self.font, 50, (0,0,0))
            if selected == 4:
                text_quit = self.text_format("QUIT", self.font, 50, (255,24,0))
            else:
                text_quit = self.text_format("QUIT", self.font, 50, (0,0,0))

            start_rect = text_start.get_rect()
            player_rect = text_player.get_rect()
            difficulty_rect = text_dfficulty.get_rect()
            quit_rect=text_quit.get_rect()

            self.screen.blit(text_start, (self.screen_width/2+70 - (start_rect[2]/2), 200))
            self.screen.blit(text_player, (self.screen_width/2+70 - (player_rect[2]/2), 260))
            self.screen.blit(text_dfficulty, (self.screen_width/2+70 - (difficulty_rect[2]/2), 320))
            self.screen.blit(text_quit, (self.screen_width/2+70 - (quit_rect[2]/2), 380))
            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.display.set_caption("UNO!")

if __name__ == '__main__':
    uno = UNOGame()
    uno.main_menu()