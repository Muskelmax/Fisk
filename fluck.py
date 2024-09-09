from fish import *
import random

#test 2

class Flock:
  def __init__(self, amount, screen, scale):
    self.__amount = amount
    self.__fishies = []
    for i in range(0, self.__amount + 1):
      self.__fishies.append(Fish(random.random()*600, random.random()*500, random.random()*5,random.random()*5, screen, scale))
  def draw(self):
    for fish in self.__fishies:
      fish.render()
  def update(self):
    for fish in self.__fishies:
      fish.update()
  def react(self, leftClick, rightClick):
    for fish in self.__fishies:
      if(leftClick == True):
        fish.attract()
      if(rightClick == True):
        fish.avoid()

