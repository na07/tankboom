import pygame, sys
from pygame.locals import QUIT

pygame.init()

win_width = 700
win_height = 500
DISPLAYSURF = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('tankboom')

background = pygame.transform.scale(pygame.image.load("back.png"),
                                    (win_width, win_height))



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x,player_y, player_speed):
      super().__init__()
      self.image = pygame.transform.scale(pygame.image.load(player_image), (65,65))
      self.player_speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
      #self.direction = direction

    def reset(self):
      DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.rect.x > 5:
      self.rect.x -= self.player_speed
    if keys[pygame.K_RIGHT] and self.rect.x < win_width-80:
      self.rect.x += self.player_speed
    if keys[pygame.K_UP] and self.rect.y > 5:
      self.rect.y -= self.player_speed
    if keys[pygame.K_DOWN] and self.rect.y < win_height-80:
      self.rect.y += self.player_speed



class Player2(GameSprite):
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and self.rect.x > 5:
      self.rect.x -= self.player_speed
    if keys[pygame.K_d] and self.rect.x < win_width-80:
      self.rect.x += self.player_speed
    if keys[pygame.K_w] and self.rect.y > 5:
      self.rect.y -= self.player_speed
    if keys[pygame.K_s] and self.rect.y < win_height-80:
      self.rect.y += self.player_speed

#class Enemy(GameSprite):
  #def update(self):
    #if self.rect.x <= 470:
      #self.side = "right"
    #if self.rect.x >= win_width-85:
      #self.side = "left"

    #if self.side == "left":
      #self.rect.x -= self.player_speed
    #else:
      #self.rect.x += self.player_speed


      
class Wall(pygame.sprite.Sprite):
  def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
    super().__init__()
    self.color=color
    self.width = wall_width
    self.height = wall_height
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.x = wall_x
    self.rect.y = wall_y
  def draw_wall(self):
    DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))

    

      

player1 = Player1("tank1.png", 10, win_height-80, 5)
player2 = Player2("tank2.png", 10, win_height-80, 5)
#monster = Enemy("cyborg.png", win_width-80, 280, 2)
#final = GameSprite("treasure.png", win_width-120, win_height-80, 0)

#w1 = Wall((154,205,50),100,20,450,10)
#w2 = Wall((154,205,50),100,20,10,320)
#w3 = Wall((154,205,50),100,450,450,10)
#w4 = Wall((154,205,50),200,140,10,320)
#w5 = Wall((154,205,50),300,30,10,320)
#w6 = Wall((154,205,50),450,140,10,320)
#w7 = Wall((154,205,50),550,20,10,230)


pygame.font.init()
text = pygame.font.Font(None, 70)
win = text.render("YOU WIN", True, (255,215,0))
lose = text.render("YOU LOSE", True, (180,0,0))


clock = pygame.time.Clock()
FPS = 60
finish = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    if finish != True:
      DISPLAYSURF.blit(background, (0, 0))
      player1.reset()
      player1.update()
      player2.reset()
      player2.update()
      
  
      #w1.draw_wall()
      #w2.draw_wall()
      #w3.draw_wall()
      #w4.draw_wall()
      #w5.draw_wall()
      #w6.draw_wall()
      #w7.draw_wall()

      #if (pygame.sprite.collide_rect(player, monster) or 
          #pygame.sprite.collide_rect(player, w1) or
          #pygame.sprite.collide_rect(player, w2) or
          #pygame.sprite.collide_rect(player, w3) or
          #pygame.sprite.collide_rect(player, w4) or
          #pygame.sprite.collide_rect(player, w5) or
          #pygame.sprite.collide_rect(player, w6) or
              #pygame.sprite.collide_rect(player, w7)):
          #finish = True
          #DISPLAYSURF.blit(lose, (200,200))
          #kick.play()

      #if pygame.sprite.collide_rect(player, final):
        #finish = True
        #DISPLAYSURF.blit(win, (200,200))
        #money.play()


    #else:
      #pygame.time.delay(5000)
      #player.rect.x = 10
      #player.rect.y = win_height-80
      #finish = False

  
    clock.tick(FPS)
    pygame.display.update()