import pygame
from pygame.locals import *

temp = []

class AI():
    def __init__(self, playernum, playerdeck, wastecard):
        print(playerdeck)
        self.playernum = playernum
        self.playerdeck = playerdeck
        self.nowcard = wastecard[-1]
        self.wastes = wastecard

    def basicplay(self):
        now = self.nowcard.split('_')
        for item in self.playerdeck:
            card = item.split('_')
            if now[0] == 'BLACK' : return item
            if len(now) == 1:
                if card[0] == now[0]: return item
            elif len(card)<3 or len(now)<3:
                if card[0] == now[0]: return item
                elif card[1] == now[1]: return item
            else:
                if card[0] == now[0]: return item
                elif card[2] == now[2]: return item
        for item in self.playerdeck:
            card = item.split('_')
            if card[0] == 'BLACK' : return item
        return 0

    def advancedplay(self, next_user):
        now = self.nowcard.split('_')
        solution = []
        for item in self.playerdeck:
            card = item.split('_')
            if len(next_user) < 3:
                if len(card) == 3:
                    if card[2] == 4 : return item
                    elif card[2] == 2 : return item
        if len(self.playerdeck) == 1:
            return self.playerdeck[0]
        result = self.find_solution(now)
        if result == None:
            for item in self.playerdeck:
                card = item.split('_')
                if card[0] == 'BLACK':
                    result = item
            return result
        else: return result

    def find_solution(self, now):
        temp = []
        for item in self.playerdeck:
            item_ = item.split('_')
            if len(item_) == 2:
                if len(now) == 1:
                    if item_[0] == now[0]: temp.append(item)
                if len(now) == 2:
                    if item_[0] == now[0]: temp.append(item)
                    elif item_[1] == now[1]: temp.append(item)
                if len(now) == 3:
                    if item_[0] == now[0]: temp.append(item)
            if len(item_) == 3:
                if item_[0] != 'BLACK':
                    if item_[0] == now[0]:
                        if self.playernum == 2:
                            if self.check_same_color(item_[0]): temp.append(item)
                        else : temp.append(item)
                    if len(now) == 3:
                        if item_[2] == now[2]:
                            if self.playernum == 2:
                                if self.check_same_color(item_[0]): temp.append(item)
                            else: temp.append(item)
                elif item_[0] == 'BLACK':
                    temp.append(item)
        if len(temp) == 1:
            return temp[0]
        if len(temp) > 1:
            before = temp[0]
            check = 0
            for i in range(1, len(temp)):
                before_ = before.split('_')
                card = temp[i]
                card_ = card.split('_')
                if before_[0] == card_[0]:
                    before = card
                else: check = 1
        
            if check == 1:
                result = self.calculate_p(temp)
            else:
                result = temp[0]
                for card in temp:
                    card_ = card.split('_')
                    if len(card_) == 3:
                        result = card
            return result

    def check_same_color(self, color):
        sum = 0
        for item in self.playerdeck:
            item_ = item.split('_')
            if item_[0] == color:
                sum = sum + 1
        if sum > 1: return True
        else: return False

    def calculate_p(self, result):
        red = 0; yellow = 0; green = 0; blue = 0
        for card in self.wastes:
            card_ = card.split('_')
            if len(card_) != 1:
                if card_[0] == 'RED' : red += 1.0
                elif card_[0] == 'YELLOW' : yellow += 1.0
                elif card_[0] == 'GREEN' : green += 1.0
                elif card_[0] == 'BLUE' : blue += 1.0

        temp = [red, yellow, green, blue]
        if 0 in temp:
            temp.remove(0)
        temp.sort(reverse=True)
        c_temp = []
        for p in temp:
            if p == red: c_temp.append('RED')
            elif p == yellow: c_temp.append('YELLOW')
            elif p == green: c_temp.append('GREEN')
            elif p == blue: c_temp.append('BLUE')

        for c in c_temp:
            for i in result:
                card = i.split('_')
                if card[0] == c : return i
        
        return result[0]