from vektor import *
import pygame

class Fish:
  def __init__(self, posX, posY, velX, velY, img='./fish.svg'):
    self.__pos = Vector(posX, posY)
    self.__vel = Vector(velX, velY)
    self.__img = img
    self.__fish_img = pygame.image.load(self.__img)
    self.__fish_img = pygame.transform.scale(self.__fish_img, (50,50))
    self.__fish_img = pygame.transform.flip(self.__fish_img, True, False)
  def update(self):
    self.__pos = self.__pos + self.__vel
    self.__vel = self.__vel/self.__vel.getLength()*3.5
    self.__vel. x = self.bordercheck().x
    self.__vel. y = self.bordercheck().y
  def bordercheck(self):
    if ((self.__pos.x > 750) or (self.__pos.x < -50)):
      return Vector(self.__vel.x * (-2), self.__vel.y*2)
    elif ((self.__pos.y > 590) or (self.__pos.y < 0)):
      return Vector(self.__vel.x*2, self.__vel.y * (-2))
    else:
      return self.__vel

  def render(self, screen):
    screen.blit(self.__fish_img,(self.__pos.x, self.__pos.y))
  def attract(self):
    self.__vel = self.__vel + ((Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) - self.__pos)*0.0004
  def avoid(self):
    self.__vel = self.__vel + (self.__pos - (Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))*0.001
