import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

class Slider_w_labels:
  def __init__(self,screen,i,minV,maxV,text):
    self.slider = Slider(screen,110,40+i*40,200,10, min=minV,max = maxV,step = 1)
    self.outputValue = TextBox(screen,80,30+i*40,35,25,fontSize = 15)
    self.outputText = TextBox(screen, 10,30+i*40, 70,25, fontSize=15)
    self.outputValue.disable()
    self.outputText.disable()
    self.outputText.setText(text)

  def update(self): 
    self.outputValue.setText(self.slider.getValue())
  
  @property
  def value(self):
    return self.slider.getValue()