import pygame
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black =(0, 0, 0)
X = 600
Y = 400
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Speech recognition Demo')
font = pygame.font.Font('arial.ttf', 28)

 
while True:
  text = font.render('مرحبا', True, black, white)
  textRect = text.get_rect()
  textRect.center = (X // 2, Y // 2)
  display_surface.fill(white)
  display_surface.blit(text, textRect)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    pygame.display.update()