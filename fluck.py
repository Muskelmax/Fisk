from fish import *
import random

#test

class Flock:
  def __init__(self, amount):
    self.__amount = amount
    self.__fishies = []
    for i in range(0, self.__amount + 1):
      self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5))
  def draw(self, screen):
    for fish in self.__fishies:
      fish.render(screen)
  def update(self):
    for fish in self.__fishies:
      fish.update()
      fish.bordercheck()
  def react(self, leftClick, rightClick):
    for fish in self.__fishies:
      if(leftClick == True):
        fish.attract()
      if(rightClick == True):
        fish.avoid()

