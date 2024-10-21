from vektor import *

class Aquarium: 
  def __init__(self, screen): 
    self.screen = screen 
  def add_flock(self, preyFlock, predatorFlock): 
    self.prey = preyFlock
    self.predator = predatorFlock
  def checkCollision(self, fish1, fish2): 
    if fish1.pos.distance(Vector(fish2.pos.x+130, fish2.pos.y+30)) < 50: 
      return True 
    return False 
  def checkFlockCollision(self): 
    for fish in self.prey.fishies: 
      for pirate in self.predator.fishies: 
        if self.checkCollision(fish, pirate): 
          self.prey.fishRemove(fish) 
          
      