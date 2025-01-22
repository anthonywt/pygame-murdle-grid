#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""pygame-murdle-grid-simple.py

Simple pygrame grid to use with simple Murdle puzzles.

"""

import pygame
from pygame.locals import *


def reset_rect():
  pygame.draw.rect(screen, ('black'), rect1_1)
  pygame.draw.rect(screen, ('black'), rect2_1)
  pygame.draw.rect(screen, ('black'), rect3_1)
  pygame.draw.rect(screen, ('black'), rect4_1)
  pygame.draw.rect(screen, ('black'), rect5_1)
  pygame.draw.rect(screen, ('black'), rect6_1)
  pygame.draw.rect(screen, ('black'), rect1_2)
  pygame.draw.rect(screen, ('black'), rect2_2)
  pygame.draw.rect(screen, ('black'), rect3_2)
  pygame.draw.rect(screen, ('black'), rect4_2)
  pygame.draw.rect(screen, ('black'), rect5_2)
  pygame.draw.rect(screen, ('black'), rect6_2)
  pygame.draw.rect(screen, ('black'), rect1_3)
  pygame.draw.rect(screen, ('black'), rect2_3)
  pygame.draw.rect(screen, ('black'), rect3_3)
  pygame.draw.rect(screen, ('black'), rect4_3)
  pygame.draw.rect(screen, ('black'), rect5_3)
  pygame.draw.rect(screen, ('black'), rect6_3)
  pygame.draw.rect(screen, ('black'), rect1_4)
  pygame.draw.rect(screen, ('black'), rect2_4)
  pygame.draw.rect(screen, ('black'), rect3_4)
  pygame.draw.rect(screen, ('black'), rect1_5)
  pygame.draw.rect(screen, ('black'), rect2_5)
  pygame.draw.rect(screen, ('black'), rect3_5)
  pygame.draw.rect(screen, ('black'), rect1_6)
  pygame.draw.rect(screen, ('black'), rect2_6)
  pygame.draw.rect(screen, ('black'), rect3_6)


pygame.init()
font = pygame.font.SysFont("Arial", 14)
screen = pygame.display.set_mode((700,700))
screen.fill((127,127,127))
running = True
rect1_1 = pygame.Rect(40,40,100,100)
rect2_1 = pygame.Rect(40,150,100,100)
rect3_1 = pygame.Rect(40,260,100,100)
rect4_1 = pygame.Rect(40,370,100,100)
rect5_1 = pygame.Rect(40,480,100,100)
rect6_1 = pygame.Rect(40,590,100,100)
rect1_2 = pygame.Rect(150,40,100,100)
rect2_2 = pygame.Rect(150,150,100,100)
rect3_2 = pygame.Rect(150,260,100,100)
rect4_2 = pygame.Rect(150,370,100,100)
rect5_2 = pygame.Rect(150,480,100,100)
rect6_2 = pygame.Rect(150,590,100,100)
rect1_3 = pygame.Rect(260,40,100,100)
rect2_3 = pygame.Rect(260,150,100,100)
rect3_3 = pygame.Rect(260,260,100,100)
rect4_3 = pygame.Rect(260,370,100,100)
rect5_3 = pygame.Rect(260,480,100,100)
rect6_3 = pygame.Rect(260,590,100,100)
rect1_4 = pygame.Rect(370,40,100,100)
rect2_4 = pygame.Rect(370,150,100,100)
rect3_4 = pygame.Rect(370,260,100,100)
rect1_5 = pygame.Rect(480,40,100,100)
rect2_5 = pygame.Rect(480,150,100,100)
rect3_5 = pygame.Rect(480,260,100,100)
rect1_6 = pygame.Rect(590,40,100,100)
rect2_6 = pygame.Rect(590,150,100,100)
rect3_6 = pygame.Rect(590,260,100,100)

reset = pygame.Rect(560,560,100,100)
resettxt = font.render(" RESET ", True, ('white'))
screen.blit(resettxt, reset)
s1 = pygame.Rect(40,0,100,40)
s1txt = font.render(" S1 ", True, ('white'))
screen.blit(s1txt, s1)
s2 = pygame.Rect(150,0,100,40)
s2txt = font.render(" S2 ", True, ('white'))
screen.blit(s2txt, s2)
s3 = pygame.Rect(260,0,100,40)
s3txt = font.render(" S3 ", True, ('white'))
screen.blit(s3txt, s3)
l1 = pygame.Rect(370,0,100,40)
l11 = pygame.Rect(0,370,100,40)
l1txt = font.render(" L1 ", True, ('white'))
screen.blit(l1txt, l1)
screen.blit(l1txt, l11)
l2 = pygame.Rect(480,0,100,40)
l22 = pygame.Rect(0,480,100,40)
l2txt = font.render(" L2 ", True, ('white'))
screen.blit(l2txt, l2)
screen.blit(l2txt, l22)
l3 = pygame.Rect(590,0,100,40)
l33 = pygame.Rect(0,590,100,40)
l3txt = font.render(" L3 ", True, ('white'))
screen.blit(l3txt, l3)
screen.blit(l3txt, l33)
w1 = pygame.Rect(0,40,100,40)
w1txt = font.render(" W1 ", True, ('white'))
screen.blit(w1txt, w1)
w2 = pygame.Rect(0,150,100,40)
w2txt = font.render(" W2 ", True, ('white'))
screen.blit(w2txt, w2)
w3 = pygame.Rect(0,260,100,40)
w3txt = font.render(" W3 ", True, ('white'))
screen.blit(w3txt, w3)

pygame.draw.line(screen, 'red', (0, 365), (700, 365), 2)
pygame.draw.line(screen, 'red', (365, 0), (365, 700), 2)
pygame.display.flip()

reset_rect()

while running:
   for event in pygame.event.get():
      if event.type == QUIT:
        running = False
      if event.type == pygame.KEYDOWN:
        key=pygame.key.name(event.key)
        pos=pygame.mouse.get_pos()
        if rect1_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_1)
          else:
            pygame.draw.rect(screen, ('black'), rect1_1)
        if rect2_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_1)
          else:
            pygame.draw.rect(screen, ('black'), rect2_1)
        if rect3_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_1)
          else:
            pygame.draw.rect(screen, ('black'), rect3_1)
        if rect4_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect4_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect4_1)
          else:
            pygame.draw.rect(screen, ('black'), rect4_1)
        if rect5_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect5_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect5_1)
          else:
            pygame.draw.rect(screen, ('black'), rect5_1)
        if rect6_1.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect6_1)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect6_1)
          else:
            pygame.draw.rect(screen, ('black'), rect6_1)
        if rect1_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_2)
          else:
            pygame.draw.rect(screen, ('black'), rect1_2)
        if rect2_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_2)
          else:
            pygame.draw.rect(screen, ('black'), rect2_2)
        if rect3_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_2)
          else:
            pygame.draw.rect(screen, ('black'), rect3_2)
        if rect4_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect4_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect4_2)
          else:
            pygame.draw.rect(screen, ('black'), rect4_2)
        if rect5_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect5_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect5_2)
          else:
            pygame.draw.rect(screen, ('black'), rect5_2)
        if rect6_2.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect6_2)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect6_2)
          else:
            pygame.draw.rect(screen, ('black'), rect6_2)
        if rect1_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_3)
          else:
            pygame.draw.rect(screen, ('black'), rect1_3)
        if rect2_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_3)
          else:
            pygame.draw.rect(screen, ('black'), rect2_3)
        if rect3_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_3)
          else:
            pygame.draw.rect(screen, ('black'), rect3_3)
        if rect4_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect4_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect4_3)
          else:
            pygame.draw.rect(screen, ('black'), rect4_3)
        if rect5_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect5_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect5_3)
          else:
            pygame.draw.rect(screen, ('black'), rect5_3)
        if rect6_3.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect6_3)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect6_3)
          else:
            pygame.draw.rect(screen, ('black'), rect6_3)
        if rect1_4.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_4)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_4)
          else:
            pygame.draw.rect(screen, ('black'), rect1_4)
        if rect2_4.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_4)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_4)
          else:
            pygame.draw.rect(screen, ('black'), rect2_4)
        if rect3_4.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_4)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_4)
          else:
            pygame.draw.rect(screen, ('black'), rect3_4)
        if rect1_5.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_5)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_5)
          else:
            pygame.draw.rect(screen, ('black'), rect1_5)
        if rect2_5.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_5)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_5)
          else:
            pygame.draw.rect(screen, ('black'), rect2_5)
        if rect3_5.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_5)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_5)
          else:
            pygame.draw.rect(screen, ('black'), rect3_5)
        if rect1_6.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect1_6)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect1_6)
          else:
            pygame.draw.rect(screen, ('black'), rect1_6)
        if rect2_6.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect2_6)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect2_6)
          else:
            pygame.draw.rect(screen, ('black'), rect2_6)
        if rect3_6.collidepoint(pos):
          if key=='n':
            pygame.draw.rect(screen, ('red'), rect3_6)
          elif key=='y':
            pygame.draw.rect(screen, ('green'), rect3_6)
          else:
            pygame.draw.rect(screen, ('black'), rect3_6)

      if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         if reset.collidepoint(pos):
          reset_rect()
   pygame.display.update()
pygame.quit()
