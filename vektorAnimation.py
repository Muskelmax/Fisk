import pygame
import random
from fluck import *



def main():
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((800, 600))
  fisk = Flock(300, screen, 50)
  running = True
  while running:
    screen.fill((0, 128, 255))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    fisk.update()
    fisk.draw()
    fisk.react(pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2])
    pygame.display.flip()
    clock.tick(60)

main()