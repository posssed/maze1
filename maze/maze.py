from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def draw(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

win_width = 700
win_height = 500

win = display.set_mode((win_width,win_height))
display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"),(win_width, win_height))

player = GameSprite("hero.png", 10, 10, 410)
monstr = GameSprite("cyborg.png", 10, 550, 260)
gold = GameSprite("treasure.png", 10, 550, 410)

game = True
FPS = 60
clock = time.clock()

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play
while game:
    win.blit(background,(0,0))
    player.draw()
    monstr.draw()
    gold.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)