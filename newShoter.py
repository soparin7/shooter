from pygame import *

window = display.set_mode((1200, 600))
display.set_caption("Шутер")
background = transform.scale(image.load("background.png"), (1200, 520))

clock = time.Clock()

font.init()
font1 = font.SysFont("Arial", 100)

mixer.init()
firesound = mixer.Sound('fire.ogg')
damagesound = mixer.Sound('damage.ogg')
victorysound = mixer.Sound('victory.ogg')

redhp = 3
bluehp = 3

blacksurf = Surface((1200, 1200))
blacksurf.fill((0,0,0))
vinsurf = Surface((2200, 2200))
vinsurf.fill((0,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, scale, player_image, player_x, player_y, player_speed, player_speedx):
        super().__init__()
        self.scale = scale
        self.image = transform.scale(image.load(player_image), (self.scale))
        self.speed = player_speed
        self.type = player_speedx
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.imgg = player_image

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
            self.imgg = "red_player.png"
            self.scale = (67, 36)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed
            self.imgg = "red_player_down.png"
            self.scale = (67, 36)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_RIGHT] and self.rect.x < 1150:
            self.rect.x += self.speed
            self.imgg = "red_player_right.png"
            self.scale = (36, 67)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
            self.imgg = "red_player_left.png"
            self.scale = (36, 67)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
            self.imgg = "blue_player_up.png"
            self.scale = (67, 36)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
            self.imgg = "blue_player_down.png"
            self.scale = (67, 36)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_d] and self.rect.x < 1150:
            self.rect.x += self.speed
            self.imgg = "blue_player_right.png"
            self.scale = (36, 67)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
            self.imgg = "blue_player_left.png"
            self.scale = (36, 67)
            self.image = transform.scale(image.load(self.imgg), (self.scale))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def message1(self):
        return self.imgg
    def message2(self):
        return self.rect.x
    def message3(self):
        return self.rect.y

class Gun(GameSprite):
    def update(self, boss, bx, by):
        if boss == "blue_player_up.png" or boss == "red_player.png":
            self.rect.x = bx + 60
            self.rect.y = by - 60
            self.scale = (25, 75)
            self.image = transform.scale(image.load("gun_up.png"), (self.scale))
        elif boss == "blue_player_right.png" or boss == "red_player_right.png":
            self.rect.x = bx + 20
            self.rect.y = by - 20
            self.scale = (75, 25)
            self.image = transform.scale(image.load("gun_right.png"), (self.scale))
        elif boss == "blue_player_down.png" or boss == "red_player_down.png":
            self.rect.x = bx - 20
            self.rect.y = by + 20
            self.scale = (25, 75)
            self.image = transform.scale(image.load("gun_down.png"), (self.scale))
        elif boss == "blue_player_left.png" or boss == "red_player_left.png":
            self.rect.x = bx - 60
            self.rect.y = by - 20
            self.scale = (75, 25)
            self.image = transform.scale(image.load("gun_left.png"), (self.scale))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Gunfire(GameSprite):
    def update(self, boss, bx, by):
        if boss == "blue_player_up.png" or boss == "red_player.png":
            self.rect.x = bx +40
            self.rect.y = by - 160
            self.image = transform.scale(image.load("fire_up.png"), (self.scale))
        elif boss == "blue_player_right.png" or boss == "red_player_right.png":
            self.rect.x = bx + 100
            self.rect.y = by - 60
            self.image = transform.scale(image.load("fire_right.png"), (self.scale))
        elif boss == "blue_player_down.png" or boss == "red_player_down.png":
            self.rect.x = bx - 60
            self.rect.y = by + 100
            self.image = transform.scale(image.load("fire_down.png"), (self.scale))
        elif boss == "blue_player_left.png" or boss == "red_player_left.png":
            self.rect.x = bx - 160
            self.rect.y = by - 60
            self.image = transform.scale(image.load("fire_left.png"), (self.scale))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Healthmetr(GameSprite):
    def update(self, boss):
        if boss == "blue":
            global bluehp
            if bluehp == 3:
                self.image = transform.scale(image.load("3heart_blue.png"), (self.scale))
            elif bluehp == 2:
                self.image = transform.scale(image.load("2heart_blue.png"), (self.scale))
            elif bluehp == 1:
                self.image = transform.scale(image.load("1heart_blue.png"), (self.scale))
            elif bluehp == 0:
                self.image = transform.scale(image.load("0heart_blue.png"), (self.scale))
        if boss == "red":
            global redhp
            if redhp == 3:
                self.image = transform.scale(image.load("3heart_red.png"), (self.scale))
            elif redhp == 2:
                self.image = transform.scale(image.load("2heart_red.png"), (self.scale))
            elif redhp == 1:
                self.image = transform.scale(image.load("1heart_red.png"), (self.scale))
            elif redhp == 0:
                self.image = transform.scale(image.load("0heart_red.png"), (self.scale))
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bluep = Player((67, 36), 'blue_player_up.png', 200, 200, 20, "blue")
bluegun = Gun((150, 50), 'gun_up.png', 1100, 420, 20, "blue")
bluefire = Gunfire((100, 100), 'fire_up.png', -1000, -1000, 20, "blue")
bluehps = Healthmetr((200, 200), '3heart_blue.png', 0, 470, 20, "blue")

redp = Player((67, 36), 'red_player.png', 870, 200, 20, "red")
redgun = Gun((150, 50), 'gun_up.png', 1100, 420, 20, "red")
redfire = Gunfire((100, 100), 'fire_up.png', -1000, -1000, 20, "red")
redhps = Healthmetr((200, 200), '3heart_red.png', 1000, 470, 20, "red")

FPS = 80
firetime1 = time.get_ticks()
firetime2 = time.get_ticks()
game = True

r = 0
d = 0
while game:
    c = 0
    
    firetime11 = time.get_ticks()
    firetime21 = time.get_ticks()
    a = firetime11 - firetime1
    b = firetime21 - firetime2
    aa = 1200 - a
    bb = 1200 - b

    window.blit(background, (0, 0))
    
    




    bluep.update_l()
    bluep.reset()
    infr = bluep.message1()
    infx = bluep.message2()
    infy = bluep.message3()
    bluegun.update(infr, infx, infy)
    bluegun.reset()
    

    redp.update_r()
    redp.reset()
    infr1 = redp.message1()
    infx1 = redp.message2()
    infy1 = redp.message3()
    redgun.update(infr1, infx1, infy1)
    redgun.reset()
    
    window.blit(blacksurf, (0, 520))
    redhps.update("red")
    redhps.reset()
    bluehps.update("blue")
    bluehps.reset()


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and aa <= 0:
                firetime1 = time.get_ticks()
                bluefire.update(infr, infx, infy)
                bluefire.reset()
                c = 1
                r = 30
                firesound.play()
            if e.key == K_RCTRL and bb <= 0:
                firetime2 = time.get_ticks()
                redfire.update(infr1, infx1, infy1)
                redfire.reset()
                c = 1
                d = 30
                firesound.play()


    if sprite.collide_rect(bluefire, redp) and c == 1:
        damagesound.play(1)
        firetime1 = time.get_ticks()
        firetime2 = time.get_ticks()
        redhp -= 1
    elif sprite.collide_rect(redfire, bluep) and c == 1:
        damagesound.play(1)
        firetime1 = time.get_ticks()
        firetime2 = time.get_ticks()
        bluehp -= 1

    if  r:
        r -= 1
        bluefire.update(infr, infx, infy)
        bluefire.reset()
        print(12)
    if d:
        d -= 1
        redfire.update(infr1, infx1, infy1)
        redfire.reset()






    if bluehp == 0 or redhp == 0:
        victorysound.play()
        break
        pass

    display.update()
    clock.tick(FPS)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if redhp == 0:
        winer = " Синий"
        wincolor = (0, 0, 200)
    else:
        winer = " Красный"
        wincolor = (200, 0, 0)
    score_text = font1.render(f"Победитель -"+ winer, True, wincolor)
    window.blit(score_text, (10, 10))





    display.update()
    clock.tick(FPS)

