import sys
import random
import pygame
from pygame.locals import *
import loadcard
import popup
import AI

class game():
    def __init__(self, playernum, difficulty):
        self.playernum = playernum
        self.difficulty = difficulty
        self.background = pygame.image.load('./img/default.png')
        self.screen = pygame.display.set_mode((800, 700))
        self.screen.blit(self.background, (-100, -70))
        self.color = {1:'RED', 2:'YELLOW', 3:'GREEN', 4:'BLUE', 5:'BLACK'}
        self.skill = {11:'_SKILL_0', 12:'_SKILL_1', 13:'_SKILL_2', 14:'_SKILL_3', 15:'_SKILL_4'}
        self.card_deck = []
        self.player = [[0] for i in range (0, self.playernum)]
        self.waste_group = pygame.sprite.RenderPlain()
        self.rotate = 0
        self.uno = 0
        pygame.display.update()

    def text_format(self, message, textFont, textSize, textColor):
        newFont = pygame.font.SysFont(textFont, textSize)
        newText = newFont.render(message, K_0, textColor)
        return newText

    def set_deck(self):
        for color_idx in range(1,5):
            card = self.color[color_idx]
            now_card = card + '_0'
            self.card_deck.append(now_card)
            for card_number in range(1, 10):
                now_card = card + "_" + str(card_number)
                iterate = 0
                while iterate != 2:
                    self.card_deck.append(now_card)
                    iterate += 1
            for card_number in range(11, 14):
                now_card = card + self.skill[card_number]
                iterate = 0
                while iterate != 2:
                    self.card_deck.append(now_card)
                    iterate += 1
        card = 'BLACK'
        for card_number in range(14, 16):
            now_card = card + self.skill[card_number]
            iterate = 0
            while iterate != 4:
                self.card_deck.append(now_card)
                iterate += 1
        random.shuffle(self.card_deck)

    def set_window(self):
        self.set_deck()
        for player in range(0, self.playernum):
            card = []
            for number in range(0, 7):
                temp = self.card_deck.pop(number)
                card.append(temp)
            self.player[player] = card
        deck = loadcard.Card('BACK', (350, 300))
        self.deck_group = pygame.sprite.RenderPlain(deck)

        player_deck = self.player[0]
        init_card = []
        for item in player_deck:
            cards = loadcard.Card(item, (400, 300))
            init_card.append(cards)

        for i in range(0, len(self.player)):
            player_deck = self.player[i]
            if i == 0:
                user_card = []
                for item in player_deck:
                    cards = loadcard.Card(item, (400, 300))
                    user_card.append(cards)
            elif i == 1:
                self.com1_card = []
                for item in player_deck:
                    cards = loadcard.Card('BACK', (400, 300))
                    cards.rotation(180)
                    self.com1_card.append(cards)
            elif i == 2:
                self.com2_card = []
                for item in player_deck:
                    cards = loadcard.Card('BACK', (400, 300))
                    cards.rotation(270)
                    self.com2_card.append(cards)
            else:
                self.com3_card = []
                for item in player_deck:
                    cards = loadcard.Card('BACK', (400, 300))
                    cards.rotation(90)
                    self.com3_card.append(cards)
        setting = True
        settinguser = 1; settingcom1 = 1; settingcom3 = 1; settingcom2 = 1
        if self.playernum == 3:
            settingcom3 = 0
        if self.playernum == 2:
            settingcom3 = 0
            settingcom2 = 0

        while setting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            i = 0
            temp_list = []
            
            for item in user_card:
                item.update((200+70*i, 500))
                temp_list.append(item)
                i +=1
            self.user_group = pygame.sprite.RenderPlain(*temp_list)

            self.lastcard0 = temp_list[-1].getposition()
            if self.lastcard0 == (200+70*(len(temp_list)-1), 500):
                settinguser = 0

            i = 0
            temp_list = []
            setting = True
            for item in self.com1_card:
                item.update((270+40*i, 100))
                temp_list.append(item)
                i +=1
            self.com1_group = pygame.sprite.RenderPlain(*temp_list)
            self.lastcard1 = temp_list[-1].getposition()
            if self.lastcard1 == (270+40*(len(temp_list)-1), 100):
                settingcom1 = 0


            if self.playernum >= 3:
                i = 0
                temp_list = []
                setting = True
                for item in self.com2_card:
                    item.update((80, 170+40*i))
                    temp_list.append(item)
                    i +=1
                self.com2_group = pygame.sprite.RenderPlain(*temp_list)
                self.lastcard2 = temp_list[-1].getposition()
                if self.lastcard2 == (80, 170+40*(len(temp_list)-1)):
                    settingcom2 = 0

            if self.playernum == 4:
                i = 0
                temp_list = []
                setting = True
                for item in self.com3_card:
                    item.update((710, 170+40*i))
                    temp_list.append(item)
                    i +=1
                self.com3_group = pygame.sprite.RenderPlain(*temp_list)
                self.lastcard3 = temp_list[-1].getposition()
                if self.lastcard3 == (710, 170+40*(len(temp_list)-1)):
                    settingcom3 = 0
            
            
            if settinguser == 0 and settingcom1 == 0 and settingcom2 == 0 and settingcom3 == 0:
                setting = False

            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.init()
            card = pygame.mixer.Sound('./sound/card.wav')
            for i in range(0,7):
                card.play()
            self.printwindow()
            pygame.display.update()

    def next_turn(self, now_turn):
        if now_turn == 0:
            user_text = self.text_format("ME", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(user_text, (165, 420))

        elif now_turn == 1:
            com1_text = self.text_format("COM1", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(com1_text, (235, 18))

        elif now_turn == 2:
            com2_text = self.text_format("COM2", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(com2_text, (45, 100))

        elif now_turn == 3:
            com3_text = self.text_format("COM3", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(com3_text, (675, 100))
        temp = self.get_next_player(now_turn)
        return temp
        
    def get_next_player(self, now_turn):
        if self.rotate==0 and now_turn + 1 == self.playernum: return 0
        elif self.rotate==1 and now_turn - 1 < 0: return self.playernum-1
        else: 
            if self.rotate == 0: return now_turn + 1
            elif self.rotate == 1: return now_turn - 1
        return 0

    def select_player(self, now_turn):
        if now_turn == 0:
            user_text = self.text_format("ME", 'Berlin Sans FB', 30, (255,242,0))
            self.screen.blit(user_text, (165, 420))
        elif now_turn == 1:
            com1_text = self.text_format("COM1", 'Berlin Sans FB', 30, (255,242,0))
            self.screen.blit(com1_text, (235, 18))
        elif now_turn == 2:
            com2_text = self.text_format("COM2", 'Berlin Sans FB', 30, (255,242,0))
            self.screen.blit(com2_text, (45, 100))
        else:
            com3_text = self.text_format("COM3", 'Berlin Sans FB', 30, (255,242,0))
            self.screen.blit(com3_text, (675, 100))
        pygame.display.update()
    
    def printwindow(self):
        self.screen.blit(self.background, (-100, -70))
        self.deck_group.draw(self.screen)
        self.user_group.draw(self.screen)   
        self.com1_group.draw(self.screen)
        if self.playernum >= 3:
            self.com2_group.draw(self.screen)
            com2_text = self.text_format("COM2", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(com2_text, (45, 100))
        if self.playernum == 4:
            self.com3_group.draw(self.screen)
            com3_text = self.text_format("COM3", 'Berlin Sans FB', 30, (0,0,0))
            self.screen.blit(com3_text, (675, 100))
        user_text = self.text_format("ME", 'Berlin Sans FB', 30, (0,0,0))
        self.screen.blit(user_text, (165, 420))
        com1_text = self.text_format("COM1", 'Berlin Sans FB', 30, (0,0,0))
        self.screen.blit(com1_text, (235, 18))
        self.waste_group.draw(self.screen)

    def check_card(self, sprite):
        if len(self.waste_card) == 0:
            return True
        else:
            name = sprite.get_name()
            name = name.split('_')
            w_name = self.waste_card[-1]
            w_name = w_name.split('_')
            if w_name[0] == 'BLACK' : return True
            if name[0] == 'BLACK' : return True
            if len(name)<3 or len(w_name)<3:
                if w_name[0] == name[0]: return True
                if len(name)>1 and len(w_name)>1:
                    if w_name[1] == name[1]: return True               
            else: 
                if w_name[0] == name[0]: return True
                if w_name[2] == name[2] : return True

        return False

    def card_skill(self, sprite):
        name = sprite.get_name()
        name = name.split('_')
        if name[1] == 'SKILL':
            if name[2] == '0':
                pygame.time.wait(500)
                self.now_turn = self.next_turn(self.now_turn)
            elif name[2] == '1':
                if self.playernum == 2:
                    pygame.time.wait(500)
                    self.now_turn = self.next_turn(self.now_turn)
                else:
                    if self.rotate == 0 : self.rotate = 1
                    else : self.rotate = 0
            elif name[2] == '2':
                pygame.time.wait(500)
                self.give_card(2)
                self.now_turn = self.next_turn(self.now_turn)
            elif name[2] == '3':
                pygame.mixer.pre_init(44100, -16, 1, 512)
                pygame.init()
                select = pygame.mixer.Sound('./sound/select.wav')
                select.play()
                if self.now_turn == 0:
                    self.pick_color()
                elif self.now_turn == 1:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[1])
                elif self.now_turn == 2:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[2])
                elif self.now_turn == 3:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[3])
            elif name[2] == '4':
                pygame.mixer.pre_init(44100, -16, 1, 512)
                pygame.init()
                select = pygame.mixer.Sound('./sound/select.wav')
                select.play()
                self.give_card(4)
                if self.now_turn == 0:
                    self.pick_color()
                elif self.now_turn == 1:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[1])
                elif self.now_turn == 2:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[2])
                elif self.now_turn == 3:
                    pygame.time.wait(500)
                    self.most_num_color(self.player[3])
        return True

    def most_num_color(self, card_deck):
        r = 0; y = 0; g = 0; b = 0;
        for item in card_deck:
            card = item.split('_')
            if card[0] == 'RED': r += 1
            if card[0] == 'YELLOW': y += 1
            if card[0] == 'GREEN': g += 1
            if card[0] == 'BLUE': b += 1
        a = [r, y, g, b]
        index = a.index(max(a))
        if index == 0 : temp_name = 'RED'
        if index == 1 : temp_name = 'YELLOW'
        if index == 2 : temp_name = 'GREEN'
        if index == 3 : temp_name = 'BLUE'
        temp = loadcard.Card(temp_name, (430, 300))
        self.waste_card.append(temp_name)
        self.waste_group.add(temp)
        self.printwindow()

    def pick_color(self):
        color_popup = popup.Popup('pickcolor', (400, 300))
        popup_group = pygame.sprite.RenderPlain(color_popup)
        red = popup.Popup('RED', (306, 320))
        yellow = popup.Popup('YELLOW', (368, 320))
        green = popup.Popup('GREEN', (432, 320))
        blue = popup.Popup('BLUE', (494, 320))
        colors = [red, yellow, green, blue]
        color_group = pygame.sprite.RenderPlain(*colors)

        loop = True
        while loop:
            popup_group.draw(self.screen)
            color_group.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for sprite in color_group:
                        if sprite.get_rect().collidepoint(mouse_pos):
                            temp_name = sprite.get_name()
                            temp = loadcard.Card(temp_name, (430, 300))
                            self.waste_card.append(temp_name)
                            self.waste_group.add(temp)
                            self.printwindow()
                            loop = False
        return 0

    def give_card(self, card_num):
        dest_player = self.get_next_player(self.now_turn)
        for i in range(0, card_num):
            self.get_from_deck(dest_player)

    def restart(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        win = pygame.mixer.Sound('./sound/win.wav')
        lose = pygame.mixer.Sound('./sound/lose.wav')
        pygame.draw.rect(self.screen, (255, 51, 0), pygame.Rect(200, 200, 400, 200))
        pygame.draw.rect(self.screen, (255, 180, 0), pygame.Rect(210, 210, 380, 180))

        if len(self.user_group) == 0:
            win.play()
            close_text = self.text_format("YOU WIN!", 'Berlin Sans FB', 80, (255,51,0))
            press_text = self.text_format("Press SPACE to REPLAY", 'Berlin Sans FB', 35, (255,51,0))
            self.screen.blit(close_text, (230, 220))
        else:
            lose.play()
            close_text = self.text_format("YOU LOSE!", 'Berlin Sans FB', 80, (255,51,0))
            press_text = self.text_format("Press SPACE to REPLAY", 'Berlin Sans FB', 35, (255,51,0))
            self.screen.blit(close_text, (212, 220))
        
        self.screen.blit(press_text, (228, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.startgame()
                        return
        return 0

    def startgame(self):
        self.card_deck.clear()
        self.player = [[0] for i in range (0, self.playernum)]
        self.waste_group = pygame.sprite.RenderPlain()
        self.rotate = 0
        self.set_window()
        self.playgame()

    def playgame(self):
        self.now_turn = 0
        self.waste_card = []
        while True:
            if len(self.user_group) ==0:
                self.restart()
                return
            elif self.playernum == 4:
                if len(self.player[1]) == 0 or len(self.player[2]) == 0 or len(self.player[2]) == 0:
                    self.restart()
                    return
            elif self.playernum == 3:
                if len(self.player[1]) == 0 or len(self.player[2]) == 0:
                    self.restart()
                    return
            elif self.playernum == 2:
                if len(self.player[1]) == 0:
                    self.restart()
                    return
            if len(self.card_deck) == 0:
                self.set_deck()

            self.select_player(self.now_turn)
            if self.now_turn == 1:
                self.select_player(self.now_turn)
                pygame.time.wait(700)
                ai = AI.AI(2, self.player[1], self.waste_card)
                if self.difficulty == 1:
                    temp = ai.basicplay()
                elif self.difficulty == 2:
                    next = self.get_next_player(self.now_turn)
                    if next == 0 : next_ = self.user_group
                    else : next_ = self.player[next]
                    temp = ai.advancedplay(next_)
                if temp == 0 or temp == None:
                    self.get_from_deck(1)
                    self.printwindow()
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()
                else:
                    pygame.mixer.pre_init(44100, -16, 1, 512)
                    pygame.init()
                    card = pygame.mixer.Sound('./sound/deal_card.wav')
                    for sprite in self.com1_group:
                        if sprite.getposition() == self.lastcard1:
                            self.com1_group.remove(sprite)
                    self.player[1].remove(temp)
                    self.set_lastcard(self.lastcard1, (0,0))
                    card.play()
                    self.waste_card.append(temp)
                    t_card = loadcard.Card(temp, (430, 300))
                    self.waste_group.add(t_card)
                    self.printwindow()
                    pygame.display.update()
                    self.card_skill(t_card)
                    self.printwindow()
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()
                

            elif self.now_turn == 2:
                self.select_player(self.now_turn)
                pygame.time.wait(700)
                ai = AI.AI(3, self.player[2], self.waste_card)
                if self.difficulty == 1:
                    temp = ai.basicplay()
                elif self.difficulty == 2:
                    next = self.get_next_player(self.now_turn)
                    if next == 0 : next_ = self.user_group
                    else : next_ = self.player[next]
                    temp = ai.advancedplay(next_)
                if temp == 0 or temp == None:
                    self.get_from_deck(2)
                    self.printwindow()
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()
                else:
                    pygame.mixer.pre_init(44100, -16, 1, 512)
                    pygame.init()
                    card = pygame.mixer.Sound('./sound/deal_card.wav')
                    for sprite in self.com2_group:
                        if sprite.getposition() == self.lastcard2:
                            self.com2_group.remove(sprite)
                    self.player[2].remove(temp)
                    self.set_lastcard(self.lastcard2, (0,0))
                    card.play()
                    self.waste_card.append(temp)
                    t_card = loadcard.Card(temp, (430, 300))
                    self.waste_group.add(t_card)
                    self.printwindow()
                    pygame.display.update()
                    self.card_skill(t_card)
                    self.printwindow()
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()
            elif self.now_turn == 3:
                self.select_player(self.now_turn)
                pygame.time.wait(700)
                ai = AI.AI(4, self.player[3], self.waste_card)
                if self.difficulty == 1:
                    temp = ai.basicplay()
                elif self.difficulty == 2:
                    next = self.get_next_player(self.now_turn)
                    if next == 0 : next_ = self.user_group
                    else : next_ = self.player[next]
                    temp = ai.advancedplay(next_)
                if temp == 0 or temp == None:
                    self.get_from_deck(3)
                    self.printwindow()
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()
                else:
                    pygame.mixer.pre_init(44100, -16, 1, 512)
                    pygame.init()
                    card = pygame.mixer.Sound('./sound/deal_card.wav')
                    for sprite in self.com3_group:
                        if sprite.getposition() == self.lastcard3:
                            self.com3_group.remove(sprite)
                    self.player[3].remove(temp)
                    self.set_lastcard(self.lastcard3, (0,0))
                    card.play()
                    self.waste_card.append(temp)
                    t_card = loadcard.Card(temp, (430, 300))
                    self.waste_group.add(t_card)
                    self.printwindow()
                    pygame.display.update()
                    self.card_skill(t_card)
                    self.printwindow()
                    print("computer lastcard", self.lastcard3)
                    self.now_turn = self.next_turn(self.now_turn)
                    pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

                if event.type == MOUSEBUTTONUP:
                    if self.now_turn == 0:
                        self.select_player(self.now_turn)
                        mouse_pos = pygame.mouse.get_pos()
                        for sprite in self.user_group:
                            if sprite.get_rect().collidepoint(mouse_pos):
                                if self.check_card(sprite):
                                    pygame.mixer.pre_init(44100, -16, 1, 512)
                                    pygame.init()
                                    card = pygame.mixer.Sound('./sound/deal_card.wav')
                                    self.user_group.remove(sprite)
                                    for temp in self.user_group:
                                        temp.move(sprite.getposition())
                                    sprite.setposition(430, 300)
                                    card.play()
                                    self.put_waste_group(sprite)
                                    self.card_skill(sprite)
                                    self.now_turn = self.next_turn(self.now_turn)
                                    break
                        for sprite in self.deck_group:
                            if sprite.get_rect().collidepoint(mouse_pos):
                                self.get_from_deck(self.now_turn)
                                self.now_turn = self.next_turn(self.now_turn)
                                break
            pygame.display.update()
    
    def get_from_deck(self, now_turn):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        deck = pygame.mixer.Sound('./sound/from_deck.wav')
        item = self.card_deck.pop(0)
        deck.play()
        if now_turn == 0:
            temp = loadcard.Card(item, (400, 300))
            current_pos = self.lastcard0
            if current_pos[0]>=620:
                y = current_pos[1]+80
                x = 200
            else:
                y = current_pos[1]
                x = current_pos[0]+70      
            temp.setposition(x, y)
            self.lastcard0 = (x, y)
            self.user_group.add(temp)
        elif now_turn == 1:
            temp = loadcard.Card('BACK', (350, 300))
            temp.rotation(180)
            current_pos = self.lastcard1
            if current_pos[0]>=510:
                y = current_pos[1]+40
                x = 270
            else:
                y = current_pos[1]
                x = current_pos[0]+40
            temp.setposition(x, y)
            self.lastcard1 = (x, y)
            self.com1_group.add(temp)
            self.player[1].append(item)
        elif now_turn == 2:
            temp = loadcard.Card('BACK', (350, 300))
            current_pos = self.lastcard2
            temp.rotation(90)
            if current_pos[1]>=410:
                y = 170
                x = current_pos[0]+40
            else:
                y = current_pos[1]+40
                x = current_pos[0]
            temp.setposition(x, y)
            self.lastcard2 = (x, y)
            self.com2_group.add(temp)
            self.player[2].append(item)
        elif now_turn == 3:
            temp = loadcard.Card('BACK', (350, 300))
            current_pos = self.lastcard3
            temp.rotation(270)
            if current_pos[1]>=410:
                y = 170
                x = current_pos[0]+40
            else:
                y = current_pos[1]+40
                x = current_pos[0]
            temp.setposition(x, y)
            self.lastcard3 = (x, y)
            self.com3_group.add(temp)
            self.player[3].append(item)
        self.printwindow()

    def set_lastcard(self, lastcard, compare_pos):
        x = lastcard[0]
        y = lastcard[1]

        i_x = compare_pos[0]
        i_y = compare_pos[1]

        if self.now_turn == 0:
            if x >= i_x+60 and y == i_y:
                x -= 70

            elif y > i_y:
                if x <= 200:
                    x = 620
                    y = y - 80
                else:
                    x -=70
            self.lastcard0 = (x, y)
        elif self.now_turn == 1:
            if y > 100 and x == 270:
                y -= 40
                x = 510
            else:
                x -= 40
            self.lastcard1 = (x, y)
        elif self.now_turn == 2:
            if x > 80 and y == 170:
                x -= 40
                y = 410
            else:
                y -= 40
            self.lastcard2 = (x, y)
        elif self.now_turn == 3:
            if x > 710 and y == 170:
                x -= 40
                y = 410
            else:
                y -= 40
            self.lastcard3 = (x, y)

    def put_waste_group(self, sprite):
        self.waste_group.add(sprite)
        self.waste_card.append(sprite.get_name())
        self.set_lastcard(self.lastcard0, sprite.getposition())
        self.printwindow()