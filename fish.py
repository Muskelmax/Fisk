from vektor import *
import pygame

class Fish:
  def __init__(self, posX, posY, velX, velY, screen, scale, img='./fish.svg'):
    self.__pos = Vector(posX, posY)
    self.__vel = Vector(velX, velY)
    self.__acc = Vector(0, 0)
    self.__img = img
    self.__scale = scale
    self.__screen = screen
    #Setup image
    self.__fish_img = pygame.image.load(self.__img)
    self.__fish_img = pygame.transform.scale(self.__fish_img, (self.__scale, self.__scale))
    self.__fish_img = pygame.transform.flip(self.__fish_img, True, False)
    #attributes for screen confinement
    #maximal distance to border at which effect takes place
    self.__maxVision = 100
    #distance to border at which effect takes place
    self.__vision = 100
    #strength of border avoidance
    self.__p = 1
    #max speed
    self.__s = 3
    #if the vision should be changed depending on surounding fish
  @property
  def pos(self):
    return self.__pos
  @property
  def vel(self):
    return self.__vel
  @property
  def maxVision(self):
    return self.__maxVision
  @property
  def vision(self):
    return self.__visio
  @vision.setter
  def vision(self, vision):
    self.__vision = vision
  def update(self, other_fishes):
    #Adding adjustments from boids algorithm
    self.__acc += self.seperation(other_fishes, 100) #22
    self.__acc += self.allignment(other_fishes, 0.01) 
    self.__acc += self.cohesion(other_fishes, 0.10)
    self.screenConfinementHandler(2)
    self.__vel += self.__acc
    #limiting speed
    self.__vel = self.__vel/self.__vel.getLength()*self.__s
    self.__pos += self.__vel
    self.__acc = Vector(0, 0)

  def screenConfinementHandler(self, x):
    if(x == 1):
      self.__acc.x += self.screenConfinementX1().x
      self.__acc.y += self.screenConfinementY1().y
    elif(x == 2):
      self.__acc.x += self.screenConfinementX2().x
      self.__acc.y += self.screenConfinementY2().y
    elif(x == 3):
      self.screenConfinementX3()
      self.screenConfinementY3()
    

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
    if ((self.__pos.x + self.__scale < self.__vision)):
      return Vector(self.__vel.x + (1 - (self.__pos.x/self.__vision))*self.__p, self.__vel.y)
    elif (self.__pos.x + self.__scale - 50 > self.__screen.get_width()-self.__vision):
      return Vector(self.__vel.x - (1 - ((self.__pos.x-self.__screen.get_width()+50)/self.__vision))*self.__p, self.__vel.y)
    else:
      return self.__vel
  def screenConfinementY2(self):
    if ((self.__pos.y < self.__vision)):
      return Vector(self.__vel.x, self.__vel.y + (1 - (self.__pos.y/self.__vision))*self.__p)
    elif (self.__pos.y - 20 > self.__screen.get_height()-self.__vision):
      return Vector(self.__vel.x, self.__vel.y - (1 - ((self.__pos.y-self.__screen.get_height()+20)/self.__vision))*self.__p)
    else:
      return self.__vel
    
  def screenConfinementX3(self):
    if ((self.__pos.x + self.__scale > self.__screen.get_width())):
      self.__pos = Vector(0-20, self.__pos.y)
    elif((self.__pos.x + self.__scale < 0)):
      self.__pos = Vector(self.__screen.get_width()+20, self.__pos.y)

  def screenConfinementY3(self):
    if (self.__pos.y > self.__screen.get_height()):
      self.__pos = Vector(self.__pos.x, 0+20)
    elif(self.__pos.y < 0):
      self.__pos = Vector(self.__pos.x, self.__screen.get_height())
  def render(self):
    self.__screen.blit(self.__fish_img,(self.__pos.x, self.__pos.y))
  
  def seperation(self, other_fishes, seperation_factor):
    seperation_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(other_fishes) != 0):
      for other in other_fishes:
        if(self.__pos.distance(other.pos) != 0):
          total_vector += (self.__pos-other.pos).normalize()/((self.__pos.distance(other.pos))**1.5)
      # return seperation_vector
      seperation_vector = total_vector*seperation_factor
    return seperation_vector
  
  def allignment(self, other_fishes, allignment_factor):
    allignment_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(other_fishes) != 0):
      for other in other_fishes:
        total_vector += other.vel
      allignment_vector = (total_vector / len(other_fishes))*allignment_factor
    return allignment_vector
  
  def cohesion(self, other_fishes, cohesion_factor):
    cohesion_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(other_fishes) != 0):
      for other in other_fishes:
        total_vector += other.pos - self.__pos
      cohesion_vector = (total_vector / len(other_fishes))*cohesion_factor
    return cohesion_vector

  def attract(self):
    self.__vel = self.__vel + ((Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) - self.__pos)*0.0004
  def avoid(self):
    self.__vel = self.__vel + (self.__pos - (Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))*0.001
