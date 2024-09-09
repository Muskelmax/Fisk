from vektor import *
import pygame

class Fish:
  def __init__(self, posX, posY, velX, velY, screen, scale, img='./fish.svg'):
    self.__pos = Vector(posX, posY)
    self.__vel = Vector(velX, velY)
    self.__img = img
    self.__scale = scale
    self.__screen = screen
    self.__fish_img = pygame.image.load(self.__img)
    self.__fish_img = pygame.transform.scale(self.__fish_img, (self.__scale, self.__scale))
    self.__fish_img = pygame.transform.flip(self.__fish_img, True, False)
    self.__d = 800
  def update(self):
    self.__pos = self.__pos + self.__vel
    self.__vel = self.__vel/self.__vel.getLength()*6
    self.__vel.x = self.screenConfinementX2().x
    self.__vel.y = self.screenConfinementY2().y
  def screenConfinementX1(self):
    if ((self.__pos.x + self.__scale > self.__screen.get_width()) or (self.__pos.x + self.__scale < 0)):
      return Vector(self.__vel.x * (-1), self.__vel.y)
    else:
      return self.__vel
  def screenConfinementY1(self):
    if ((self.__pos.y > self.__screen.get_height()) or (self.__pos.y < 0)):
      return Vector(self.__vel.x*1, self.__vel.y * (-1))
    else:
      return self.__vel
    
  def screenConfinementX2(self):
    if ((self.__pos.x + self.__scale + self.__d*9/10 < self.__d)):
      return Vector(self.__vel.x + (1 - (self.__pos.x/self.__d)), self.__vel.y)
    elif (self.__pos.x + self.__scale - self.__d*9/10> self.__screen.get_width()-self.__d):
      return Vector(self.__vel.x - (1 - ((self.__pos.x-self.__screen.get_width())/self.__d)), self.__vel.y)
    else:
      return self.__vel
  def screenConfinementY2(self):
    if ((self.__pos.y + self.__d*9/10 < self.__d)):
      return Vector(self.__vel.x, self.__vel.y + (1 - (self.__pos.y/self.__d)))
    elif (self.__pos.y - self.__d*9/10 > self.__screen.get_height()-self.__d):
      return Vector(self.__vel.x, self.__vel.y - (1 - ((self.__pos.y-self.__screen.get_height())/self.__d)))
    else:
      return self.__vel
  def render(self):
    self.__screen.blit(self.__fish_img,(self.__pos.x, self.__pos.y))
  def attract(self):
    self.__vel = self.__vel + ((Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) - self.__pos)*0.0004
  def avoid(self):
    self.__vel = self.__vel + (self.__pos - (Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))*0.001
