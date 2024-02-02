from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.y += self.speed
        
win_w = 700
win_h = 500

window = display.set_mode((win_w, win_h))

raketka_lef = Player('raketka.png', 30, 200, 10, 100, 100)
raketka_rig = Player('raketka.png', 520, 200, 10, 100, 100)
ball = GameSprite('ball.png', 200, 200, 8, 50, 50)

font.init()
text_lose1 = font.Font(None, 35).render('PLAYER 1 LOSE!', True, (237, 9, 5))
text_lose2 = font.Font(None, 35).render('PLAYER 2 LOSE!', True, (237, 9, 5))

clock = time.Clock()

speed_x = 3
speed_y = 3

game = True
finish = False

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.fill((108, 140, 230))

        raketka_lef.update_l()
        raketka_rig.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(raketka_lef, ball) or sprite.collide_rect(raketka_rig, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_h - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(text_lose1, (200, 200))
            

        if ball.rect.x > win_w:
            finish = True
            window.blit(text_lose2, (200, 200))
            
            
        raketka_lef.reset()
        raketka_rig.reset()
        ball.reset()

    display.update()
    clock.tick(60)
