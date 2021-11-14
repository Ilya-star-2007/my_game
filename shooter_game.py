#Создай собственный Шутер!

from pygame import *
from random import randint
from time import *
lost=0
fire_time = 0
num_fire =0
rel_time = False


Bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self,x_player,y_player,image_player,player_speed,player_size_1,player_size_2):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(player_size_1,player_size_2))# 65,65
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = x_player
        self.rect.y = y_player
    def recet(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x <650:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
    def fire(self):
        Sprite_x=self.rect.x
        Sprite_top = self.rect.top
        bullet =Bullet(Sprite_x,Sprite_top,"bullet.png",13,30,30)
        Bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y<450:
            self.rect.y= self.rect.y+self.speed
        else:
            self.rect.y=0
            self.rect.x=randint(0,650)
            lost=lost+1
class Bullet(GameSprite):
    def update(self):
        self.rect.y= self.rect.y-self.speed
        if self.rect.y<0:
            self.kill()
class Asteroid(GameSprite):
        def update(self):
            if self.rect.y<450:
                self.rect.y= self.rect.y+self.speed
            else:
                self.rect.y=0
                self.rect.x=randint(0,650)






window = display.set_mode((700, 500))
display.set_caption("Шутер")
background=transform.scale(image.load("galaxy.jpg"),(700,500))




#clock=time.Clock()
FPS = 60
game = True
player = Player(200,435,"rocket.png",20,65,65)
monster = Enemy(randint(0,650),0,"ufo.png",13,65,65)
asteroid_1=Asteroid(randint(0,650),0,"asteroid.png",13,65,65)
asteroid_2=Asteroid(randint(0,650),0,"asteroid.png",13,65,65)
asteroid_3=Asteroid(randint(0,650),0,"asteroid.png",13,65,65)
monsters = sprite.Group()
font.init()
font =font.SysFont("Arial",35)
for i in range(1,6):
    monster = Enemy(randint(0,650),0,"ufo.png",randint(1,5),65,65)
    monsters.add(monster)
finish=False
while game:
    
        
    
    for i in event.get():
        if i.type ==QUIT:
            game = False
        elif i.type ==KEYDOWN:
            if i.key ==K_SPACE:
                if num_fire<5 and rel_time ==False:
                    player.fire()
                    num_fire = num_fire+1
                if num_fire>=5 and rel_time ==False:
                    rel_time=True
                    last_time=time()

                    
    if not finish:
        window.blit(background,(0,0))

       


        player.update()
        player.recet()
        asteroid_1.recet()
        asteroid_1.update()
        asteroid_2.recet()
        asteroid_2.update()
        asteroid_3.recet()
        asteroid_3.update()
        monsters.draw(window)
        monsters.update()
        Bullets.update()
        Bullets.draw(window)
        lose_score = font.render("Пропущено:"+str(lost),True,(255,215,0))
        window.blit(lose_score,(5,25))
        collides = sprite.groupcollide(monsters,Bullets,True,True)
        for c in collides:
            monster = Enemy(randint(0,650),0,"ufo.png",randint(1,5),65,65)
            monsters.add(monster)
        if rel_time ==True:
            now_time =time()
            if now_time-last_time<3:
                bullet_time = font.render("Перезарядка",True,(255,215,0))
                window.blit(bullet_time,(100,300))
            else:
                rel_time=False
                num_fire=0


    #clock.tick(FPS)
    display.update()