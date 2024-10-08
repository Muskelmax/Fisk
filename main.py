import pygame
import random
from fluck import *
from slider_w_labels import *


def main():
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((800, 600))
  fisk = Flock(100, screen, 50, 100)
  running = True
  seperation_slider = Slider_w_labels(screen, 11, 1, 100, "seperation")
  allignment_slider = Slider_w_labels(screen, 12, 1, 100, "allignment")
  cohesion_slider = Slider_w_labels(screen, 13, 1, 100, "cohesion")
  while running:
    screen.fill((0, 128, 255))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    seperation_slider.update()
    allignment_slider.update()
    cohesion_slider.update()
    pygame_widgets.update(pygame.event.get())
    fisk.update(seperation_slider.value, allignment_slider.value, cohesion_slider.value)
    fisk.draw()
    fisk.react(pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2])
    pygame.display.flip()
    clock.tick(60)

main()