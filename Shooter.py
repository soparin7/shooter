from pygame import *
window = display.set_mode((1200, 500))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("ffonn.jpg"), (1200, 800))
clock = time.Clock()
font.init()
font1 = font.SysFont("Arial", 100)

firesound = mixer.Sound('fire.ogg')
damagesound = mixer.Sound('damage.ogg')
victorysound = mixer.Sound('victory.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, scale,  player_image, player_x, player_y, player_speed, player_speedx):
        super().__init__()
        self.scale = scale
        self.image = transform.scale(image.load(player_image), (self.scale))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


class Player(GameSprite):
    def update_l(self, number):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0 + number:
            self.rect.y -= self.speed
            self.image = transform.scale(image.load("blue_player_up.png"), (self.scale))
        if keys[K_DOWN] and self.rect.y < 480 - number:
            self.rect.y += self.speed
            self.image = transform.scale(image.load("blue_player_down.png"), (self.scale))
        if keys[K_RIGHT] and self.rect.x > 0 + number:
            self.rect.x += self.speed
            self.image = transform.scale(image.load("blue_player_right.png"), (self.scale))
        if keys[K_LEFT] and self.rect.x < 1180 - number:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load("blue_player_left.png"), (self.scale))  
    def update_r(self, number):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0 + number:
            self.rect.y -= self.speed
            self.image = transform.scale(image.load("red_player.png"), (self.scale))
        if keys[K_s] and self.rect.y < 480 - number:
            self.rect.y += self.speed
            self.image = transform.scale(image.load("red_player_down.png"), (self.scale))
        if keys[K_d] and self.rect.x > 0 + number:
            self.rect.x += self.speed
            self.image = transform.scale(image.load("red_player_right.png"), (self.scale))
        if keys[K_a] and self.rect.x < 1180 - number:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load("red_player_left.png"), (self.scale))
        
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Gun(GameSprite):
    def update(self, boss):
        #if self.rect.y >= 450 or self.rect.y <= 0:
         #   self.speed *= -1.01
            

        #self.rect.y += self.speed
        #self.rect.x += self.speedx
        
        
        self.rect.
        
        
            
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))