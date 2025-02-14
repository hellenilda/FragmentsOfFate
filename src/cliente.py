import pygame
from FragmentsOfFate.src.network import Network
width = 1024
height = 576

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("MvP")


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= self.vel
        if key[pygame.K_RIGHT]:
            self.x += self.vel
        if key[pygame.K_UP]:
            self.y -= self.vel
        if key[pygame.K_DOWN]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def renderDraw(window, jogador_1, jogador_2):
    window.fill((224,212,123))
    jogador_1.draw(window)
    jogador_2.draw(window)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    net = Network()
    starPos = read_pos(net.getPos())
    jogador = Player(starPos[0], starPos[1], 100, 100, (0,255,0))
    jogador_2 = Player(0,0, 100, 100, (255,0,0))

    while True:
        clock.tick(60)
        p2Pos = read_pos(net.send(make_pos((jogador.x, jogador.y))))
        jogador_2.x = p2Pos[0]
        jogador_2.y = p2Pos[1]
        jogador_2.update()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        jogador.move()
        renderDraw(window, jogador, jogador_2)

main()