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

class Packman():
    def __init__(self, navn):
        self.byttBane(navn)
    
    def oppdater(self):
        tast= pygame.key.get_pressed()
        if tast[pygame.K_a]:
            self.rekttest=pygame.Rect((self.x-self.fart,self.y),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.x-=self.fart
                
        elif tast[pygame.K_d]:
            self.rekttest=pygame.Rect((self.x+self.fart,self.y),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.x+=self.fart
                
        elif tast[pygame.K_w]:
            self.rekttest=pygame.Rect((self.x,self.y-self.fart),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.y-=self.fart
                
        elif tast[pygame.K_s]:
            self.rekttest=pygame.Rect((self.x,self.y+self.fart),(self.strx,self.stry))
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.y+=self.fart
    def tegn2(self):
        skjerm.blit(pakman, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
    def byttBane(self, navn):

        with open (navn, "r") as labfil:
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            self.strxgrid= skjerm.get_width()/int(self.kord.split(",")[0])
            self.strygrid= skjerm.get_height()/int(self.kord.split(",")[1])
            self.strx= self.strxgrid/3
            self.stry= self.strygrid/3
        self.fart=5
        plassy=0
        for x in self.bane:
            x=x.strip("\n")
            x=x.split(".")
            plassx=0
            for z in range (0,(int(self.kord.split(",")[0]))):
                if x[z]=="l":
                    self.x= self.strxgrid*plassx+ self.strxgrid/2-self.strx/2
                    self.y= self.strygrid*plassy+self.strygrid/2-self.stry/2
                plassx+=1
            plassy+=1
                
    def livEllerDød(self):
        status=True
        for x in fiende.rektliste:
            if pygame.Rect.colliderect(x,self.rekt):
                status=False
        return status

    

class Labirynt:
    def __init__(self, navn):
        self.byttBane(navn)
    def tegn2(self):
        for x in self.liste:
            pygame.draw.rect(skjerm, "purple", x)
    def byttBane(self, navn):     
        with open (navn, "r") as labfil:
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            self.strx= skjerm.get_width()/int(self.kord.split(",")[0])
            self.stry= skjerm.get_height()/int(self.kord.split(",")[1])
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

class Fiende:
    def __init__(self, navn):
        self.byttBane(navn)

    def bevege(self):
        self.rektliste=[]
        for x in self.spøk:    
            if x[2]=="s":
                rekt= pygame.Rect((x[0]+x[-1],x[1]),(self.strx,self.stry))
                for z in lab.liste:
                    if pygame.Rect.colliderect(z, rekt):
                        x[-1]=x[-1]*-1
                x[0]+=x[-1]
            elif x[2]=="y":
                rekt= pygame.Rect((x[0],x[1]+x[-1]),(self.strx,self.stry))
                for z in lab.liste:
                    if pygame.Rect.colliderect(z, rekt):
                        x[-1]=x[-1]*-1
                x[1]+=x[-1]
            
            rekt= pygame.Rect((x[0],x[1]),(self.strx,self.stry))
            self.rektliste.append(rekt)

        #print("hello")
    def tegn2(self):
        #skjerm.blit(blue_image, (self.x, self.y))
        for x in self.rektliste:
            pygame.draw.rect(skjerm, "blue", x)
            #pygame.Rect.colliderect(self.rekt, pack.rekt):

    def byttBane(self, navn):
        with open (navn, "r") as labfil:
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            self.strxgrid= skjerm.get_width()/int(self.kord.split(",")[0])
            self.strygrid= skjerm.get_height()/int(self.kord.split(",")[1])
            self.strx= self.strxgrid/3
            self.stry= self.strygrid/3

        plassy=0
        self.spøk=[]
        
        print("oink")
        for z in self.bane:
            z=z.strip("\n")
            z=z.split(".")
            plassx=0
            for y in range (0, int(self.kord.split(",")[0])):
                if z[y]=="y" or z[y]=="s":
                    self.x= self.strxgrid*plassx+ self.strxgrid/2-self.strx/2
                    self.y= self.strygrid*plassy+self.strygrid/2-self.stry/2
                    self.fart= random.choice([4,2,1,3,3,6,6,8,4,6,7,4,])
                    print(plassx)
                    print(plassy)

                    spøk=[self.x,self.y, z[y], self.fart]
                    self.spøk.append(spøk)
                plassx+=1
                    
            plassy+=1
        print("oink")


    


class Poeng(Felles):
    def __init__(self):
        self.x= random.randint(0,skjerm.get_width())
        self.y=random.randint(0,skjerm.get_height())
        self.farge="green"
        self.strx= (skjerm.get_width()/40)
        self.stry= (skjerm.get_height()/40)
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
        
    def oppdater(self):

        for x in lab.liste:
            if pygame.Rect.colliderect(self.rekt, x):
                self.x= random.randint(0,skjerm.get_width())
                self.y=random.randint(0,skjerm.get_height())
                self.farge="green"
                self.strx= ((skjerm.get_width()/40))
                self.stry= (skjerm.get_height()/40)
                break
        if pygame.Rect.colliderect(self.rekt, pack.rekt):
                self.x= random.randint(0,skjerm.get_width())
                self.y=random.randint(0,skjerm.get_height())
                self.farge="green"
                self.strx= (skjerm.get_width()/40)
                self.stry= (skjerm.get_height()/40)
                return True
        else:
            return False
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
skjerm= pygame.display.set_mode((800,800))
font= pygame.font.SysFont("Arial", int(skjerm.get_height()/20))
font2= pygame.font.SysFont("Arial", int(skjerm.get_height()/4))

klokke=pygame.time.Clock()
running=True
pack=Packman("test.txt")
fiende=Fiende("test.txt")
lab=Labirynt("test.txt")

poeng=Poeng()
baner=["bane.txt"]
start=True
igang=False
slutt=False
sluttvunnet= False
sum=0
bane=0
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
        tekst2=font.render("Det er 4 nivåer", True, "White")
        tekst3=font.render("få ti poeng for å nå neste nivå", True, "White")
        skjerm.blit(tekst, (skjerm.get_width()/3, skjerm.get_height()/2))
        skjerm.blit(tekst2, (skjerm.get_width()/3, skjerm.get_height()/2+40))
        skjerm.blit(tekst3, (skjerm.get_width()/3, skjerm.get_height()/2+80))
    elif igang:

        pack.oppdater()
        fiende.bevege()
        fiende.tegn2()
        
        lab.tegn2()
        pack.tegn2()
        if poeng.oppdater():
            sum+=1
        poeng.tegn2()
        if sum>=10:
            sum=0
            if bane>=(len(baner)):
                igang=False
                sluttvunnet=True
            else:
                lab.byttBane(baner[bane])
                pack.byttBane(baner[bane])
                fiende.byttBane(baner[bane])
                bane+=1

        tekst2= font.render(str(sum), True, "White")

        skjerm.blit(tekst2, (skjerm.get_width()/40, skjerm.get_height()/60))
        if pack.livEllerDød()==False:
            igang=False
            slutt=True
        
    if slutt:
        tekst3= font.render((f"du tapte"), True, "White")
        skjerm.blit(tekst3, (skjerm.get_width()/3, skjerm.get_height()/2))
    if sluttvunnet:
        tekst3= font.render((f"du vant a"), True, "White")
        skjerm.blit(tekst3, (skjerm.get_width()/3, skjerm.get_height()/2))

    pygame.display.flip()

pygame.quit()