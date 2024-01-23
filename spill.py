import pygame 
pygame.init()
skjerm= pygame.display.set_mode((500,500))
klokke=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    klokke.tick(30)
    skjerm.fill("white")
    
    pygame.display.flip()



pygame.quit()