import pygame
import sys
import math
import pandas as pd
import openpyxl


background_colour = (255,255,255)
(width, height) = (1080, 1100)
bg = pygame.image.load(r"C:\Users\Uzair\PycharmProjects\WarzoneDropDecider\venv\Images\map.jpg")
circle = pygame.image.load(r"C:\Users\Uzair\PycharmProjects\WarzoneDropDecider\venv\Images\pngfind.com-circle-outline-png-971129.png")
circle = pygame.transform.scale(circle, (1350, 1350))
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption('Warzone Map')

pygame.display.flip()
running = True



### import excel file
df = pd.read_excel(r'C:\Users\Uzair\Documents\GUItestdata.xlsx',engine='openpyxl')

print(df)





def RIGHTMOVE(keys_pressed, RIGHTPLAYER):  # MOVEMENT OF RIGHT PLAYER
  if keys_pressed[pygame.K_LEFT]:
    RIGHTPLAYER.x -= VEL
  if keys_pressed[pygame.K_RIGHT] and RIGHTPLAYER.x < width - PLAYERWIDTH:
    RIGHTPLAYER.x += VEL
  if keys_pressed[pygame.K_UP]:
    RIGHTPLAYER.y -= VEL
  if keys_pressed[pygame.K_DOWN]:
    RIGHTPLAYER.y += VEL



def draw(WIN):
  WIN.blit(bg, (0, 0))
  WIN.blit(circle, (RIGHTPLAYER))
 # pygame.draw.rect(WIN, (0,0,0), rectangle)
  pygame.draw.line(WIN,(255,255,255),startline,endline,10)
  #midpointsquare
  pygame.draw.rect(WIN, (255,0,0), pygame.Rect(a-5,b, 10, 10))




VEL = 10
FPS = 60  #REFRESH RATE
PLAYERWIDTH,PLAYERHEIGHT =5,2000
RIGHTX, RIGHTY = 1,1
RIGHTPLAYER = pygame.Rect(RIGHTX, RIGHTY, PLAYERWIDTH, PLAYERHEIGHT)

rot = 0
rot_speed = 4
x=10     ### x and y are size of line
y=3000
image_orig = pygame.Surface((x, y))

image_orig.set_colorkey((0,0,0))
image_orig.fill((255,255,255))
image = image_orig.copy()
image.set_colorkey((0,0,0))
rect = image.get_rect()
a=width // 2
b=height // 2
rect.center = (a ,b)
t=0



while True:
  clock = pygame.time.Clock()
  clock.tick(FPS)
  keys_pressed = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif keys_pressed[pygame.K_RETURN]:
      row = []
      #creating row to add to excel file
      for i in range(11):
        if i in list:
          row.append(1)
        else:
          row.append(0)

      df.loc[len(df.index)] = row
      df.to_excel(r"C:\Users\Uzair\Documents\GUItestdata.xlsx",sheet_name = "Line", index = False)
      print(df)
      pygame.quit()
      sys.exit()


  RIGHTMOVE(keys_pressed, RIGHTPLAYER)
 # LEFTMOVE(keys_pressed, LEFTPLAYER)

  old_center = rect.center
  # defining angle of the rotation
  #rotation of line
  if keys_pressed[pygame.K_q]:
    rot = (rot + rot_speed) % 360
    t-=math.pi/36
  if keys_pressed[pygame.K_e]:
    rot = (rot - rot_speed) % 360
    t+=math.pi/36
  #movement of line
  if keys_pressed[pygame.K_a]:
    a=a-10
    old_center=(a,b)
  if keys_pressed[pygame.K_d]:
    a = a + 10
    old_center = (a, b)
  if keys_pressed[pygame.K_w]:
    b=b-10
    old_center = (a, b)
  if keys_pressed[pygame.K_s]:
    b = b + 10
    old_center = (a, b)

  # rotating the orignal image

  # set the rotated rectangle to the old center
  rect.center = old_center

  startline = (2000*math.cos(t)+a,2000*math.sin(t)+b)
  endline = (2000*math.cos(t+(math.pi))+a,2000*math.sin(t+(math.pi))+b)







  Shore = pygame.Rect(350, 320, 200, 200)
  Construction = pygame.Rect(200, 500, 200, 220)
  Harbour = pygame.Rect(700, 500, 200, 220)
  Prison = pygame.Rect(500, 400, 250, 250)
  Decon = pygame.Rect(550, 210, 330, 120)
  Chemical= pygame.Rect(880, 210, 150, 280)
  Bioweapons = pygame.Rect(800, 80, 200, 140)
  Headquarters = pygame.Rect(400, 650, 200, 140)
  Factory = pygame.Rect(580, 720, 150, 240)
  Living = pygame.Rect(280, 780, 250, 240)
  Security = pygame.Rect(20, 780, 250, 240)

  list = []
  clist = []
  sites = [Security,Living,Factory,Headquarters,Construction,Shore,Prison,Harbour,Chemical,Decon,Bioweapons]

  for count, x in enumerate(sites):
    clipped_line = x.clipline(startline, endline)
    if clipped_line:
      list.append(count)


  print(clist)
  draw(WIN)




  pygame.display.update()
