from fish import *
import random
from math import sqrt

#test 2

class Flock:
  def __init__(self, amount, screen, scale, boidR):
    self.__amount = amount
    self.__fishies = []
    for i in range(0, self.__amount + 1):
      self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5, screen, scale))
    self.__boidR = boidR
    self.__useVision  = False
  def draw(self):
    for fish in self.__fishies:
      fish.render()
  def update(self, sepV, allV, cohV):
    if(self.__useVision):
      self.updateVision()
    for fish in self.__fishies:
      fish.update(self.findNeighbours(fish), sepV, allV, cohV)
  def react(self, leftClick, rightClick):
    for fish in self.__fishies:
      if(leftClick == True):
        fish.attract()
      if(rightClick == True):
        fish.avoid()
  def findNeighbours(self, fish):
    #finds neighbours of fish and returns them
    neighbours = []
    for neighbour in self.__fishies:
      if(fish != neighbour and sqrt((neighbour.pos.x-fish.pos.x)**2+(neighbour.pos.y-fish.pos.y)**2) <= self.__boidR):
        neighbours.append(neighbour)
    return neighbours
  def updateVision(self):
    #updates the fishes vision, inversly proportional to the amount of fishes around it
    for fish in self.__fishies:
      neighbours = self.findNeighbours(fish)
      if(len(neighbours) > 0):
        fish.vision = fish.maxVision*(1 -sqrt((len(neighbours)/len(self.__fishies))))
      else:
        fish.vision = fish.maxVision