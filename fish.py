from vektor import *
import pygame


class Fish:
  def __init__(self, posX, posY, velX, velY, screen, scale, img='./fish.svg'):
    self._pos = Vector(posX, posY)
    self.__vel = Vector(velX, velY)
    self._acc = Vector(0, 0)
    self.__img = img
    self.__scale = scale
    self.__screen = screen
    #Setup image
    self.__fish_img = pygame.image.load(self.__img)
    self.__fish_img = pygame.transform.scale(self.__fish_img, (self.__scale, self.__scale))
    self.__fish_img = pygame.transform.flip(self.__fish_img, True, False)
    #attributes for screen confinement
    #maximal distance to border at which effect takes place
    #distance to border at which effect takes place
    self.__vision = 100
    #strength of border avoidance
    self.__p = 1
    #max speed
    self.__s = 3
    #if the vision should be changed depending on surounding fish
  @property
  def pos(self):
    return self._pos
  @property
  def vel(self):
    return self.__vel
  def update(self, other_fishes, sepV, allV, cohV):
    #Adding adjustments from boids algorithm
    self._acc += self.seperation(other_fishes, sepV) #22
    self._acc += self.allignment(other_fishes, allV * 0.0001) 
    self._acc += self.cohesion(other_fishes, cohV * 0.001)
    self.screenConfinementHandler(2)
    self.__vel += self._acc
    #limiting speed
    self.__vel = self.__vel/self.__vel.getLength()*self.__s
    self._pos += self.__vel
    self._acc = Vector(0, 0)

  def screenConfinementHandler(self, x):
    if(x == 1):
      self._acc.x += self.screenConfinementX1().x
      self._acc.y += self.screenConfinementY1().y
    elif(x == 2):
      self._acc.x += self.screenConfinementX2().x
      self._acc.y += self.screenConfinementY2().y
    elif(x == 3):
      self.screenConfinementX3()
      self.screenConfinementY3()
    

  def screenConfinementX1(self):
    if ((self._pos.x + self.__scale > self.__screen.get_width()) or (self._pos.x + self.__scale < 0)):
      return Vector(self.__vel.x * (-1), self.__vel.y)
    else:
      return self.__vel
  def screenConfinementY1(self):
    if ((self._pos.y > self.__screen.get_height()) or (self._pos.y < 0)):
      return Vector(self.__vel.x*1, self.__vel.y * (-1))
    else:
      return self.__vel
    
  def screenConfinementX2(self):
    if ((self._pos.x + self.__scale < self.__vision)):
      return Vector(self.__vel.x + (1 - (self._pos.x/self.__vision))*self.__p, self.__vel.y)
    elif (self._pos.x + self.__scale - 50 > self.__screen.get_width()-self.__vision):
      return Vector(self.__vel.x - (1 - ((self._pos.x-self.__screen.get_width()+50)/self.__vision))*self.__p, self.__vel.y)
    else:
      return self.__vel
  def screenConfinementY2(self):
    if ((self._pos.y < self.__vision)):
      return Vector(self.__vel.x, self.__vel.y + (1 - (self._pos.y/self.__vision))*self.__p)
    elif (self._pos.y - 20 > self.__screen.get_height()-self.__vision):
      return Vector(self.__vel.x, self.__vel.y - (1 - ((self._pos.y-self.__screen.get_height()+20)/self.__vision))*self.__p)
    else:
      return self.__vel
    
  def screenConfinementX3(self):
    if ((self._pos.x + self.__scale > self.__screen.get_width())):
      self._pos = Vector(0-20, self._pos.y)
    elif((self._pos.x + self.__scale < 0)):
      self._pos = Vector(self.__screen.get_width()+20, self._pos.y)

  def screenConfinementY3(self):
    if (self._pos.y > self.__screen.get_height()):
      self._pos = Vector(self._pos.x, 0+20)
    elif(self._pos.y < 0):
      self._pos = Vector(self._pos.x, self.__screen.get_height())

  def render(self):
    self.__screen.blit(self.__fish_img,(self._pos.x, self._pos.y))
  
  def seperation(self, other_fishes, seperation_factor):
    seperation_vector = Vector(0, 0)
    total_vector = Vector(0, 0)
    if(len(other_fishes) != 0):
      for other in other_fishes:
        if(self._pos.distance(other.pos) != 0):
          total_vector += (self._pos-other.pos).normalize()/((self._pos.distance(other.pos))**1.5)
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
        total_vector += other.pos - self._pos
      cohesion_vector = (total_vector / len(other_fishes))*cohesion_factor
    return cohesion_vector

  def attract(self):
    self.__vel = self.__vel + ((Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) - self._pos)*0.004
  def avoid(self):
    self.__vel = self.__vel + (self._pos - (Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))*0.01


class Whale(Fish):
  def __init__(self, posX, posY, velX, velY, screen, scale, img='./whale.svg'):
    super().__init__(posX, posY, velX, velY, screen, scale, img)

class OfferFish(Fish):
  def __init__(self, posX, posY, velX, velY, screen, scale, img='./fish.svg'):
    super().__init__(posX, posY, velX, velY, screen, scale, img)
  
  def update(self, other_fishes, sepV, allV, cohV, predators):
    self._acc += self.avoidPredator(predators)
    super().update(other_fishes, sepV, allV, cohV)
  
  def avoidPredator(self, predators):
    total_vector = Vector(0,0)
    for predator in predators.fishies:
      if self._pos.distance(predator.pos) < 70:
        total_vector += (self._pos-predator.pos).normalize()/((self._pos.distance(predator.pos))**1.5)
    return total_vector*1000
