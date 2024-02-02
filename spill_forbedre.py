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
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            #for x in laberyntlist:
            #    if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
            #        self.status=False
            if self.status:

                self.x-=self.fart
                
        elif tast[pygame.K_d]:
            self.rekttest=pygame.Rect((self.x+self.fart,self.y),(self.strx,self.stry))
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            #for x in laberyntlist:
            #    if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
            #        self.status=False
            if self.status:

                self.x+=self.fart
                
        elif tast[pygame.K_w]:
            self.rekttest=pygame.Rect((self.x,self.y-self.fart),(self.strx,self.stry))
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            #for x in laberyntlist:
            #    if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
            #        self.status=False
            if self.status:

                self.y-=self.fart
                
        elif tast[pygame.K_s]:
            self.rekttest=pygame.Rect((self.x,self.y+self.fart),(self.strx,self.stry))
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            #for x in laberyntlist:
            #    if (pygame.Rect.colliderect(x.rekt, self.rekttest)):
            #        self.status=False
            if self.status:

                self.y+=self.fart
    def tegn2(self):
        skjerm.blit(pakman, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))

                
    def livEllerDød(self):
        status=True
        for x in fiender:
            if pygame.Rect.colliderect(x.rekt,self.rekt):
                status=False
        return status

    

class Labirynt:
    def __init__(self, navn):
        with open (navn, "r") as labfil:
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            self.strx= skjerm.get_width()/int(self.kord.split(",")[0])
            self.stry= skjerm.get_height()/int(self.kord.split(",")[1])
    def tegn2(self):
        self.liste=[]
        plassy=0
        
        for z in self.bane:
            print(z)
            liste=z.strip("\n")
            liste=liste.split(".")
            print (liste)
            for x in range (0,(int(self.kord.split(",")[0]))):
                print(x)
                if liste[x]=="x":
                    self.rekt= pygame.Rect((x*self.strx, plassy), (self.strx, self.stry))
                    self.liste.append(self.rekt)
    

            plassy+=self.stry
        print (self.liste)
        for x in self.liste:
            pygame.draw.rect(skjerm, "purple", x)
            



            
        

        

class Fiende (Felles):
    def __init__(self, x, y, akse, xstr, ystr, fart):
        self.x =x
        self.y=y
        self.akse=akse
        self.strx=xstr
        self.stry=ystr
        super().__init__(self.x, self.y, "red", self.strx, self.stry)
        self.fart=fart
    def bevege(self):
        #if self.akse=="y":
            #for x in laberyntlist:
                #if pygame.Rect.colliderect(x.rekt, self.rekt):
                 #   self.fart=self.fart*(-1)
            #self.y+=self.fart
        #if self.akse=="x":
        #    for x in laberyntlist:
         #       if pygame.Rect.colliderect(x.rekt, self.rekt):
        #            self.fart=self.fart*(-1)
         #   self.x+=self.fart
        print("hello")
    def tegn2(self):
        skjerm.blit(blue_image, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
    


class Poeng(Felles):
    def __init__(self):
        self.x= random.randint(0,skjerm.get_width())
        self.y=random.randint(0,skjerm.get_height())
        self.farge="green"
        self.strx= (skjerm.get_width()/40)
        self.stry= (skjerm.get_height()/40)
        super().__init__( self.x, self.y, self.farge, self.strx, self.stry)
        
    def oppdater(self):

        #for x in laberyntlist:
        #    if pygame.Rect.colliderect(self.rekt, x.rekt):
        #        self.x= random.randint(0,skjerm.get_width())
        #        self.y=random.randint(0,skjerm.get_height())
        #        self.farge="green"
        #        self.strx= ((skjerm.get_width()/40))
        #        self.stry= (skjerm.get_height()/40)
        #        break
        #if pygame.Rect.colliderect(self.rekt, pack.rekt):
        #        self.x= random.randint(0,skjerm.get_width())
        #        self.y=random.randint(0,skjerm.get_height())
        #        self.farge="green"
        #        self.strx= (skjerm.get_width()/40)
        #        self.stry= (skjerm.get_height()/40)
        #        return True
        #else:
        #    return False
        print("oink")
    def tegn2(self):
        skjerm.blit(penge, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))






import random
import pygame 

pygame.init()
blue_image= pygame.image.load("MicrosoftTeams-image (6).png")
blue_rect= blue_image.get_rect()
pakman= pygame.image.load("MicrosoftTeams-image (7).png")
pak_rect= blue_image.get_rect()
penge= pygame.image.load("MicrosoftTeams-image (8).png")
penge_rect= blue_image.get_rect()
pygame.font.init()
skjerm= pygame.display.set_mode((500,500))
font= pygame.font.SysFont("Arial", int(skjerm.get_height()/20))
font2= pygame.font.SysFont("Arial", int(skjerm.get_height()/4))

klokke=pygame.time.Clock()
running=True
pack=Packman()

#lager fiende objekter
fiende= Fiende(skjerm.get_width()/12*11, skjerm.get_height()/7, "y", skjerm.get_width()/30, skjerm.get_height()/30,3)
fiende2= Fiende(skjerm.get_width()/12*10, skjerm.get_height()/7*6, "y", skjerm.get_width()/30, skjerm.get_height()/30,5)
fiende3= Fiende(skjerm.get_width()/12, skjerm.get_height()/4, "x", skjerm.get_width()/30, skjerm.get_height()/30,6)
fiende4= Fiende(skjerm.get_width()/12, skjerm.get_height()/12*11, "x", skjerm.get_width()/30, skjerm.get_height()/30,2)
fiende5= Fiende(skjerm.get_width()/7, skjerm.get_height()/10*7, "x", skjerm.get_width()/30, skjerm.get_height()/30,3)
fiende6= Fiende(skjerm.get_width()/12*10, skjerm.get_height()/7*6, "y", skjerm.get_width()/30, skjerm.get_height()/30,5)
fiende7= Fiende(skjerm.get_width()/12*9, skjerm.get_height()/7*6, "y", skjerm.get_width()/30, skjerm.get_height()/30,4)
fiende8= Fiende(skjerm.get_width()/2, skjerm.get_height()/12*5, "x", skjerm.get_width()/30, skjerm.get_height()/30,7)

#lager en liste av alle fiendene slik at vi senere fort kan gå gjennom alle
fiender=[fiende,fiende2, fiende3, fiende4, fiende5, fiende6, fiende7, fiende8]
lab=Labirynt("test.txt")
poeng=Poeng()

start=True
igang=False
slutt=False
sum=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    klokke.tick(30)
    skjerm.fill("black")
    if start:
        tast= pygame.key.get_pressed()
        if tast[pygame.K_SPACE]:
            start=False
            igang=True
        tekst=font.render("Klikk space for å starte", True, "White")
        skjerm.blit(tekst, (skjerm.get_width()/3, skjerm.get_height()/2))
    elif igang:

        pack.oppdater()
        pack.tegn2()
        for x in fiender:
            x.bevege()
            x.tegn2()
        poeng.tegn2()
        if poeng.oppdater():
            sum+=1
        lab.tegn2()
        tekst2= font.render(str(sum), True, "White")
        skjerm.blit(tekst2, (skjerm.get_width()/40, skjerm.get_height()/60))

        if pack.livEllerDød()==False:
            igang=False
            slutt=True
        
    if slutt:
        tekst3= font.render((f"du fikk {sum} poeng"), True, "White")
        skjerm.blit(tekst3, (skjerm.get_width()/3, skjerm.get_height()/2))
    pygame.display.flip()

pygame.quit()