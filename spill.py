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
            self.rekttest=pygame.Rect((self.x-self.fart,self.y),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in laberyntlist:
                if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
                    self.status=False
            if self.status:

                self.x-=self.fart
                print ("oink")
        elif tast[pygame.K_d]:
            self.rekttest=pygame.Rect((self.x+self.fart,self.y),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in laberyntlist:
                if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
                    self.status=False
            if self.status:

                self.x+=self.fart
                print ("oink")
        elif tast[pygame.K_w]:
            self.rekttest=pygame.Rect((self.x,self.y-self.fart),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in laberyntlist:
                if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
                    self.status=False
            if self.status:

                self.y-=self.fart
                print ("oink")
        elif tast[pygame.K_s]:
            self.rekttest=pygame.Rect((self.x,self.y+self.fart),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in laberyntlist:
                if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
                    self.status=False
            if self.status:

                self.y+=self.fart
                print ("oink")
    

class Labirynt(Felles):
    def __init__(self, x,y,strx,stry):
        super().__init__(x,y,"purple",strx,stry)





import pygame 
pygame.init()
skjerm= pygame.display.set_mode((500,500))
klokke=pygame.time.Clock()
running=True
test=Packman()
#vegger
lab1= Labirynt(0,0, skjerm.get_width(), skjerm.get_height()/25)
lab2= Labirynt(0,0, skjerm.get_width()/25, skjerm.get_height())
lab3= Labirynt((skjerm.get_width()/25)*24,0,skjerm.get_width(),skjerm.get_height())
lab4= Labirynt(0,(skjerm.get_height()/25)*24, skjerm.get_width(), skjerm.get_height()/25)
#indre vegger fra venstre til høyre som lesing
lab5= Labirynt(skjerm.get_width()/5,0, skjerm.get_width()/25, skjerm.get_height()/5)
lab7= Labirynt(skjerm.get_width()/5,skjerm.get_height()/5, skjerm.get_width()/5, skjerm.get_height()/25)
lab8= Labirynt((skjerm.get_width()/7)*4,0, skjerm.get_width()/25, (skjerm.get_height()/25)*6)
lab9= Labirynt((skjerm.get_width()/7)*5,0, skjerm.get_width()/25, (skjerm.get_height()/25)*6)
lab6= Labirynt(0,skjerm.get_height()/3, skjerm.get_width()/2, skjerm.get_height()/25)
lab10= Labirynt((skjerm.get_width()/5),(skjerm.get_height()/4)*3, skjerm.get_width()/2, skjerm.get_height()/25)
lab11= Labirynt((skjerm.get_width()/5),(skjerm.get_height()/4)*3, skjerm.get_width()/25, skjerm.get_height()/25*4)
lab12= Labirynt((skjerm.get_width()/3)*2,(skjerm.get_height()/4)*3, skjerm.get_width()/25, skjerm.get_height()/25*4)

laberyntlist=[lab1, lab2, lab3, lab4, lab5,lab6,lab7, lab8, lab9, lab10, lab11, lab12]
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    klokke.tick(30)
    skjerm.fill("black")
    for x in laberyntlist:
        x.tegn()
    test.oppdater()
    test.tegn()
    
    pygame.display.flip()



pygame.quit()