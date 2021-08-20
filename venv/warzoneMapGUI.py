import pygame
import sys

pygame.init()
pygame.font.init()




background_colour = (255,255,255)
(width, height) = (1080, 1100)
bg = pygame.image.load(r"C:\Users\Uzair\PycharmProjects\WarzoneDropDecider\venv\Images\map.jpg")
circle = pygame.image.load(r"C:\Users\Uzair\PycharmProjects\WarzoneDropDecider\venv\Images\pngfind.com-circle-outline-png-971129.png")
circle = pygame.transform.scale(circle, (1350, 1350))
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption('Warzone Map')

pygame.display.flip()
running = True


def RIGHTMOVE(keys_pressed, RIGHTPLAYER):  # MOVEMENT OF RIGHT PLAYER
  if keys_pressed[pygame.K_LEFT]:
    RIGHTPLAYER.x -= VEL
  if keys_pressed[pygame.K_RIGHT] and RIGHTPLAYER.x < width - PLAYERWIDTH:
    RIGHTPLAYER.x += VEL
  if keys_pressed[pygame.K_UP]:
    RIGHTPLAYER.y -= VEL
  if keys_pressed[pygame.K_DOWN]:
    RIGHTPLAYER.y += VEL


"""def LEFTMOVE(keys_pressed, LEFTPLAYER):  # MOVEMENT OF LEFT PLAYER
  #if keys_pressed[pygame.K_a] and LEFTPLAYER.x > 0:
  #  LEFTPLAYER.x -= VEL
  if keys_pressed[pygame.K_d] and LEFTPLAYER.x < width - PLAYERWIDTH:
    LEFTPLAYER.x += VEL
  if keys_pressed[pygame.K_w] and LEFTPLAYER.y > 0:
    LEFTPLAYER.y -= VEL
  if keys_pressed[pygame.K_s] and LEFTPLAYER.y < height - PLAYERHEIGHT:
    LEFTPLAYER.y += VEL"""


def draw(WIN):
  WIN.blit(bg, (0, 0))
  WIN.blit(circle, (RIGHTPLAYER))
  WIN.blit(new_image, rect)
  #midpointsquare
  pygame.draw.rect(WIN, (255,0,0), pygame.Rect(a-5,b, 10, 10))


VEL = 10
FPS = 60  #REFRESH RATE
PLAYERWIDTH,PLAYERHEIGHT =5,2000
RIGHTX, RIGHTY = 1,1
RIGHTPLAYER = pygame.Rect(RIGHTX, RIGHTY, PLAYERWIDTH, PLAYERHEIGHT)

rot = 0
rot_speed = 4

x=10
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






while True:
  clock = pygame.time.Clock()
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys_pressed = pygame.key.get_pressed()
  RIGHTMOVE(keys_pressed, RIGHTPLAYER)
 # LEFTMOVE(keys_pressed, LEFTPLAYER)

  old_center = rect.center
  # defining angle of the rotation
  #rotation of line
  if keys_pressed[pygame.K_q]:
    rot = (rot + rot_speed) % 360
  if keys_pressed[pygame.K_e]:
    rot = (rot - rot_speed) % 360

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
  new_image = pygame.transform.rotate(image_orig, rot)
  rect = new_image.get_rect()
  # set the rotated rectangle to the old center
  rect.center = old_center



  draw(WIN)
  pygame.display.update()
