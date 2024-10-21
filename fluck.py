from fish import *
import random
from math import sqrt

#test 2

class Flock:
  def __init__(self, amount, screen, scale, boidR):
    self._amount = amount
    self._fishies = []
    self.__boidR = boidR
    self._useVision  = False
    self.addFish(screen, scale)
  def draw(self):
    for fish in self._fishies:
      fish.render()
  def update(self, sepV, allV, cohV):
    if(self._useVision):
      self.updateVision()
    for fish in self._fishies:
      fish.update(self.findNeighbours(fish), sepV, allV, cohV)
  def react(self, leftClick, rightClick):
    for fish in self._fishies:
      if(leftClick == True):
        fish.attract()
      if(rightClick == True):
        fish.avoid()
  def findNeighbours(self, fish):
    #finds neighbours of fish and returns them
    neighbours = []
    for neighbour in self._fishies:
      if(fish != neighbour and sqrt((neighbour.pos.x-fish.pos.x)**2+(neighbour.pos.y-fish.pos.y)**2) <= self.__boidR):
        neighbours.append(neighbour)
    return neighbours
  def updateVision(self):
    #updates the fishes vision, inversly proportional to the amount of fishes around it
    for fish in self._fishies:
      neighbours = self.findNeighbours(fish)
      if(len(neighbours) > 0):
        fish.vision = fish.maxVision*(1 -sqrt((len(neighbours)/len(self._fishies))))
      else:
        fish.vision = fish.maxVision
  def addFish(self, screen, scale):
    for i in range(0, self._amount + 1):
      self._fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5, screen, scale))
  @property
  def fishies(self):
    return self._fishies

class WhaleFlock(Flock):
  def __init__(self, amount, screen, scale, boidR):
    super().__init__(amount, screen, scale, boidR)
  def addFish(self, screen, scale):
    for i in range(0, self._amount):
      self._fishies.append(Whale(random.random()*600, random.random()*500, random.random()*5,random.random()*5, screen, scale))
  
    

class FishFlock(Flock):
  def __init__(self, amount, screen, scale, boidR):
    super().__init__(amount, screen, scale, boidR)
  def addFish(self, screen, scale):
    for i in range(0, self._amount):
      self._fishies.append(OfferFish(random.random()*600, random.random()*500, random.random()*5,random.random()*5, screen, scale))
  def fishRemove(self, fish):
    if fish in self._fishies:
      self._fishies.remove(fish)
    else:
      print("fish not found")
  def update(self, sepV, allV, cohV, predator):
    if(self._useVision):
      self.updateVision()
    for fish in self._fishies:
      fish.update(self.findNeighbours(fish), sepV, allV, cohV, predator)