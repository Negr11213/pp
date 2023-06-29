from pygame import *

BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
screen = display.set_mode((700, 500))
display.set_caption('pinignpong')
clock = time.Clock()

game = True

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

while game:
    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False


    # screen.fill(BACKGROUND)
    display.update()
