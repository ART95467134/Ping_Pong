
from pygame import *
win_width = 700
win_height = 500

window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
back = (200, 255, 255)

font.init()
font1 = font.SysFont('Ariel', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Ariel', 36)

background_image = 'background.jpg'
player_image = 'player.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - self.rect.height - 5:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DONW] and self.rect.y < win_width - self.rect.height - 5:
            self.rect.y += self.speed

ball = GameSprite('ball.png', 50, 50, 1)
player1 = Player('player.png', 40, 100, 5)
player2 = Player('player.png', -40, -100, 5)


finish = False
game = True
score1 = 0
score2 = 0
speed_x = 3
speed_y = 3
clock = time.Clock()



finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    

    
    

        player1.update()
        player1.reset()
        ball.reset()

display.update()
clock.tick(60)

