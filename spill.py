class Felles:
    def __init__(self, x,y,farge, strx, stry):
        self.x=x
        self.y=y
        self.farge=farge
        self.strx=strx
        self.stry=stry
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
    def tegn(self):
        pygame.draw.rect(skjerm, self.farge, self.rekt)
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))

class Packman(Felles):
    def __init__(self):
        super().__init__(skjerm.get_width()/20, skjerm.get_height()/20, "Yellow", skjerm.get_width()/20, skjerm.get_height()/20)
        self.fart=5
    
    def oppdater(self):
        tast= pygame.key.get_pressed()
        if tast[pygame.K_a]:
            self.x-=self.fart
        elif tast[pygame.K_d]:
            self.x+=self.fart
        elif tast[pygame.K_w]:
            self.y-=self.fart
        elif tast[pygame.K_s]:
            self.y+=self.fart

class Labirynt(Felles):
    def __init__(self, x,y,strx,stry):
        super().__init__(x,y,"purple",strx,stry)





import pygame 
pygame.init()
skjerm= pygame.display.set_mode((500,500))
klokke=pygame.time.Clock()
running=True
test=Packman()
lab1= Labirynt(0,0, skjerm.get_width(), skjerm.get_height()/25)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    klokke.tick(30)
    skjerm.fill("black")
    lab1.tegn()
    test.oppdater()
    test.tegn()
    
    pygame.display.flip()



pygame.quit()