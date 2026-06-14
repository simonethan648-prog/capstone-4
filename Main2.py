import random
import pygame

class Button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
        class RpsGame():
            def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((960, 640))
                pygame.display.set_caption("RPS Smasher")
                self.bg = pygame.image.load("background.png")
                self.rock_btn = pygame.image.load("rock.png")
                self.paper_btn = pygame.image.load("paper.png")
                self.scissor_btn = pygame.image.load("scissor.png")
                 
                self.choose_rock = pygame.image.load("rock.png").convert_alpha()
                self.choose_paper = pygame.image.load("paper.png").convert_alpha()
                self.choose_scissor = pygame.image.load("scissor.png").convert_alpha()

                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.rock_btn, (20, 500))
                self.screen.blit(self.paper_btn, (330, 500))
                self.screen.blit(self.scissor_btn, (640, 500))

                self.rock_btn = Button(30, 520, (30, 520), 300, 140)
                self.paper_btn = Button(340, 520, (340, 520), 300, 140)
                self.scissor_btn = Button(640, 520, (640, 520), 300, 140)

                self.font = pygame.font.Font(('Splatch.ttf'), 90)
                self.text = self.font.render(f" ", True, (255, 255,255))

                self.pl_score = 0
                self.pc_score = 0

            def player(self):
                if self.rock_btn.clicked(30):
                    self.p_option = "rock"
                    self.screen.blit(self.choose_rock, (120, 200))
                elif self.paper_btn.clicked(340):
                    self.p_option = "paper"
                    self.screen.blit(self.choose_paper, (120, 200))
                else:
                    self.scissor_btn.clicked(640)
                    self.p_option = "scissor"
                    self.screen.blit(self.choose_scissor, (120, 200))

                    return self.p_option
                
            def computer(self):
                self.pc_random_choice = " "
                option = ["rock", "paper", "scissors"]