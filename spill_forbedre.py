
class Packman(): # klasse til spiller (packman)
    def __init__(self, navn): #tar in navn på fil som argument
        self.byttBane(navn) #referer til metode som leser fil og finner den nødvendige informasjonen for å sette opp ny bane
    
    def oppdater(self): 
        tast= pygame.key.get_pressed() 
        #her skjekker vi om spiller har presset noen relevante knapper på tastaturet
        if tast[pygame.K_a]:#(til venstre)
            #her lager vi et ekstra rektangel litt forskjøvet i retningen spilleren vill (i dette tilfelle venstret)
            self.rekttest=pygame.Rect((self.x-self.fart,self.y),(self.strx,self.stry))
            self.pakman=pakmanvenstre #oppdaterer hvilket bilde som skal i bruk
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste: #går gjennom liste med vegger i labirynt og skjekker om den forsøvede spilleren ville ha krasjet 
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status: # dersom det førskjøvede rektangelet (spilleren) ikke krasjer med en vegg (self.status fortsatt er True) gjøres det spilleren ba om (gå til venstre)

                self.x-=self.fart
                
        elif tast[pygame.K_d]:# (til høyre)
            #samme logikk som forklart under "til venstre" bare annen retning
            self.pakman= pakmanhøyre
            self.rekttest=pygame.Rect((self.x+self.fart,self.y),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.x+=self.fart
                
        elif tast[pygame.K_w]:
            #fungerer på samme måte som forklart under "til venstre", bare at den beveger seg oppover i y aksen i stedet
            self.pakman=pakmanopp
            self.rekttest=pygame.Rect((self.x,self.y-self.fart),(self.strx,self.stry))
            self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.y-=self.fart
                
        elif tast[pygame.K_s]:
            #samme logikk som forklart ved "til venstre" bare med annen retning
            self.pakman=pakmaned
            self.rekttest=pygame.Rect((self.x,self.y+self.fart),(self.strx,self.stry))
            #self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
            self.status=True
            #pygame.draw.rect(skjerm, "Blue", self.rekttest)
            for x in lab.liste:
                if (pygame.Rect.colliderect(x, self.rekttest)):
                    self.status=False
            if self.status:

                self.y+=self.fart

    def tegn2(self): #metode som tegner packman
        skjerm.blit(self.pakman, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))

    def byttBane(self, navn): #hver gang vi skal bytte bane/lage nytt packman objekt brukes denne metoden
        #(måten vi har tenkt på er at filen som leses er et rutenett)
        self.pakman=pakmanhøyre #startbilde til packman
        with open (navn, "r") as labfil: #leser av fil 
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            #størelsen på rutenettet står på første lisnje i filen (antall ruter i x og y retning). her deler vi opp størlsen på skjermen i de to retningene på antall ruter for å finne størelsen på hver rute i x og y retning
            self.strxgrid= skjerm.get_width()/int(self.kord.split(",")[0])
            self.strygrid= skjerm.get_height()/int(self.kord.split(",")[1])
            self.strx= self.strxgrid/3 #pacman er da en tredjedel av denne ruten i hver retning
            self.stry= self.strygrid/3
        self.fart=5
        plassy=0
        for x in self.bane: #går gjennom linjene i filen (bortsett fra den første)
            # gjør klar slik at hver bokstav i kartet har sin egen plass i listen
            x=x.strip("\n")
            x=x.split(".")

            plassx=0 #holder syr på hvilken kollone vi er i
            for z in range (0,(int(self.kord.split(",")[0]))): #går igjennom indeksene i raden
                if x[z]=="l": # skjekker om noen av dem er "l" (det vi har bestemt at skal bety at er der packman starter)
                    self.x= self.strxgrid*plassx+ self.strxgrid/2-self.strx/2 # ganger kolonnen vi er i med størrelsen på rutene for å komme i riktig rute. deretter sentrere i midten av ruten
                    self.y= self.strygrid*plassy+self.strygrid/2-self.stry/2 #det samme som x bare i y retning
                plassx+=1
            plassy+=1 #holder styr på raden vi er i
                
    def livEllerDød(self): #metode som skjekker om spiller har tapt
        #går igjennom liste med alle fiendene og skjekker om spiller har kolidert med dem, dersom pacman har kolidert med en fiende vil status (som returneres) bli false ellers vil den forbli true
        status=True
        for x in fiende.rektliste:  
            if pygame.Rect.colliderect(x,self.rekt):
                status=False
        return status

    

class Labirynt:
    def __init__(self, navn): #tar in navn på fil som argument
        self.byttBane(navn) #referer til metode som finner nødvendig info til å sette opp bane

    def tegn2(self):# metode som tegner labirynten
        for x in self.liste:# går igjennom alle labiryntdelene (som er lagt i en liste) og tegner de på skjermen
            pygame.draw.rect(skjerm, "purple", x)
        for x in self.pos:
            skjerm.blit(mur, (x[0], x[1]))

    def byttBane(self, navn): 
        #måten vi har tenkt på er at vi har et rutenett i filen som leses  
        with open (navn, "r") as labfil: #leser av filen til labirynten
            self.kord=labfil.readline() 
            self.bane=labfil.readlines()
            #den første linjen i filen er størelsen på rutenettet (antall ruter i x og y retning). ved å dele sørelsen på skjermen på størelsen på rutenettet i de forskjellige retningene får vi størelsen på rutene
            self.strx= skjerm.get_width()/int(self.kord.split(",")[0])
            self.stry= skjerm.get_height()/int(self.kord.split(",")[1])
        self.liste=[]
        plassy=0
        
        self.pos=[]
        for z in self.bane: #går igjennom linjene i filen lest(bortsett fra nr1)
            print(z)

            #gjør klar slik at hver bokstav har blitt til sitt eget element i liste
            liste=z.strip("\n")
            liste=liste.split(".")

            print (liste)
            #går gjennom raden vi er på
            for x in range (0,(int(self.kord.split(",")[0]))):
                print(x)
                if liste[x]=="x": #vi skjekker om ellementet i listen vi er på er lik "x" (det vi har bestemt betyr vegg)
                    #dersom dette er sant legger vi til et rektangel med denne plaseringen inn i en liste med alle laberyntfirkantene
                    self.rekt= pygame.Rect((x*self.strx, plassy), (self.strx, self.stry))
                    pos=[x*self.strx, plassy]
                    self.pos.append(pos)
                    self.liste.append(self.rekt)
            plassy+=self.stry# holder styr på hvilken rad vi er på
        print (self.liste)

class Fiende:
    def __init__(self, navn):# tar inn navn på fil 
        self.byttBane(navn)# refererer til funksjon som finner ut nødvendig info om ny bane

    def bevege(self):#metode som tar seg af alle findene sine bevegelser
        self.rektliste=[] #liste over rektanglene til fiendene
        for x in self.spøk: #går gjennom en liste som inneholder lister med info til hver av fiendene
            #innhold i listene inni listen [xposisjon, yposisjon, om den beveger seg y eller x retning, fart]
            if x[2]=="s": #"s" er brukt for å vise at fienden skal bevege seg i x aksen
                rekt= pygame.Rect((x[0]+x[-1],x[1]),(self.strx,self.stry)) #lager et nytt rektangel der fienden har beveget seg (x[0] er pos i x og x[-1] er fart)
                for z in lab.liste: #går gjennom liste med alle labiryntfirkantene
                    if pygame.Rect.colliderect(z, rekt): #skjekker om det krasjes med noen av dem
                        x[-1]=x[-1]*-1 # dersom det krasjes bytter fienden retning
                x[0]+=x[-1] #oppdaterer pos
            elif x[2]=="y": # samme men i y retning
                rekt= pygame.Rect((x[0],x[1]+x[-1]),(self.strx,self.stry))
                for z in lab.liste:
                    if pygame.Rect.colliderect(z, rekt):
                        x[-1]=x[-1]*-1
                x[1]+=x[-1]
            
            #rekt= pygame.Rect((x[0],x[1]),(self.strx,self.stry)) #lager rektangel for fiende
            self.rektliste.append(rekt)#legger til rektangelet i liste over fiender

        #print("oink")
    def tegn2(self):
        #skjerm.blit(blue_image, (self.x, self.y))
        #for x in self.rektliste:
        #    pygame.draw.rect(skjerm, "blue", x)
            #pygame.Rect.colliderect(self.rekt, pack.rekt):
        for x in self.spøk:
            skjerm.blit(blue_image, (x[0], x[1]))

            

    def byttBane(self, navn):# benytttes hver gang man skal ha ny bane
        #som skrevet lenger oppe så har vi tenkt på spillebanen som et rutenett
        with open (navn, "r") as labfil: #leser av fil
            self.kord=labfil.readline()
            self.bane=labfil.readlines()
            # øverst i filen står det antall ruter i x og y retning
            self.strxgrid= skjerm.get_width()/int(self.kord.split(",")[0]) #finner størelsen på hver "rute" i x aksen. ved å dele størelsen på skjermen med antall ruter
            self.strygrid= skjerm.get_height()/int(self.kord.split(",")[1])# det samme bare i y aksen
            self.strx= self.strxgrid/3 # en fiende er en tredjedel av ruten i hver retning 
            self.stry= self.strygrid/3

        plassy=0 # hølder styr på hvilken rad vi er på
        self.spøk=[] #skal bli liste over info til alle fiender
        
        print("oink")
        for z in self.bane: #går linjene i filen (bortsett fra nr1)

            # gjør klar slik at alle bokstavene får sin egen plass i listen
            z=z.strip("\n")
            z=z.split(".")

            plassx=0#holder styr på kolonnene
            for y in range (0, int(self.kord.split(",")[0])): #går igjennom indexene i raden
                if z[y]=="y" or z[y]=="s": # skjekker om noen av bokstavene er symbol for fiende ("y" fiende som beveger seg i y aksen eller "s" fiende som beveger seg i x aksen)
                    self.x= self.strxgrid*plassx+ self.strxgrid/2-self.strx/2 # x og y verdier i midten gitt celle 
                    self.y= self.strygrid*plassy+self.strygrid/2-self.stry/2
                    self.fart= random.choice([1,4,2,3,3,4,3,6,4,5,4,4,]) #en tilfeldig fart som har noen mer sansynelige utfall en andre
                    print(plassx)
                    print(plassy)

                    spøk=[self.x,self.y, z[y], self.fart] #lager en liste med plass i x/y retning, bedskjed om hvilken retningden skal gå i og farten den skal ha
                    self.spøk.append(spøk) #legger til denne listen inn i en liste med infoen til alle fiendene
                plassx+=1
                    
            plassy+=1
        print("oink")


    


class Poeng: #klasse for myntene
    def __init__(self):
        self.x= random.randint(0,skjerm.get_width()) #tilfeldig plasering
        self.y=random.randint(0,skjerm.get_height())
        self.farge="green"
        self.strx= (skjerm.get_width()/40)
        self.stry= (skjerm.get_height()/40)
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))
        
    def oppdater(self): #metode som skjekker om noe kræsjer og oppdaterer pos

        for x in lab.liste: #går igjennom liste med laberyntfirkanter
            if pygame.Rect.colliderect(self.rekt, x):# skjekker om mynten kræsjer med labberynten
                self.x= random.randint(0,skjerm.get_width()) #hvis mynten har spawnet inni veggen får den en ny pos
                self.y=random.randint(0,skjerm.get_height())
                #self.farge="green"
                #self.strx= ((skjerm.get_width()/40))
                #self.stry= (skjerm.get_height()/40)
                #break
        if pygame.Rect.colliderect(self.rekt, pack.rekt): #skjekker om spiller koliderer med mynt
                self.x= random.randint(0,skjerm.get_width()) #dersom spiller koliderer med mynt ny tilfeldig posisjon
                self.y=random.randint(0,skjerm.get_height())
                #self.farge="green"
                #self.strx= (skjerm.get_width()/40)
                #self.stry= (skjerm.get_height()/40)
                return True #returnerer true slik at vi lett kan skjekke om spilleren har fått poeng nede i while running løkken
        else:
            return False #hvis ikke spiller har fått poeng returner false slik at vi vet dette
        print("oink")
    def tegn2(self): #tegner penge
        skjerm.blit(penge, (self.x, self.y))
        self.rekt=pygame.Rect((self.x,self.y),(self.strx,self.stry))





#importerer nødvendige biblioteker
import random
import pygame 
import time

#initsialiserer pygame
pygame.init()

#laster ned alle png bildene
blue_image= pygame.image.load("MicrosoftTeams-image (6).png")
blue_rect= blue_image.get_rect()
pakmanvenstre= pygame.image.load("packve.png")
pakmanhøyre= pygame.image.load("packhø.png")
pakmanopp=pygame.image.load("packopp.png")
pakmaned=pygame.image.load("packned.png")
mur=pygame.image.load("mur.png")
mur_rekt=mur.get_rect()
pakman=pakmanvenstre
pak_rect= pakmanvenstre.get_rect()
penge= pygame.image.load("MicrosoftTeams-image (8).png")
penge_rect= penge.get_rect()

#bestemmer størelse på skjerm
skjerm= pygame.display.set_mode((800,800))

#gjør klar slik at vi senere kan skrive på skjerm i bestemte størelser
pygame.font.init()
font= pygame.font.SysFont("Arial", int(skjerm.get_height()/20))
#font2= pygame.font.SysFont("Arial", int(skjerm.get_height()/4))
font3= pygame.font.SysFont("Arial", int(skjerm.get_height()/14))





klokke=pygame.time.Clock()
running=True

#lager objektene og gir dem det første kartet
pack=Packman("test.txt")
fiende=Fiende("test.txt")
lab=Labirynt("test.txt")

poeng=Poeng()

#liste over banene (utenom bane 1)
baner=["bane.txt", "oink.txt", "oink2.txt"]

#variablene som holder styr på stadier i spillet 
start=True
igang=False
slutt=False
sluttvunnet= False

sound=False
# lydfilene
coin = pygame.mixer.Sound("collect.mp3")
game_over=pygame.mixer.Sound("gameover.mp3")
pygame.mixer.music.load("soundtrack.mp3")
vinne=pygame.mixer.Sound("vinnemusikk.mp3")
start_tid=time.time()

bakgrunn= pygame.image.load("bakgrunn.jpg")

sum=0
bane=0
while running:
    for event in pygame.event.get(): #skjekker om spiller har trykket på X knappen i gjørne av skjermen og går ut av spillet dersom dette 
        if event.type==pygame.QUIT:
            running=False

    klokke.tick(30)
    #skjerm.fill("black") # fyller skjermen med svart
    skjerm.blit(bakgrunn,(0, 0))

    if start:
        tast= pygame.key.get_pressed()
        if tast[pygame.K_SPACE]: #skjekker om mellomromknappen er trykket
            #dersom mellomrom er trykket så er spillet ikke i start-fasen lenger men i igang-fasen, derfor oppdaterer vi variablene
            start=False
            igang=True
        #skriver nyttig info til spilleren på skjermen
        tekst=font.render("Klikk mellomrom for å starte", True, "White")
        tekst_rect= tekst.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/2))
        tekst2=font.render("Det er 4 nivåer", True, "White")
        tekst2_rect= tekst2.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/16*9))
        tekst3=font.render("få fem poeng for å nå neste nivå", True, "White")
        tekst3_rect= tekst3.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/16*10))
        tekst4=font3.render("Pyman", True, "yellow")
        tekst4_rect= tekst4.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/5*2))


        skjerm.blit(tekst, tekst_rect)
        skjerm.blit(tekst2, tekst2_rect)
        skjerm.blit(tekst3, tekst3_rect)
        skjerm.blit(tekst4, tekst4_rect)

    elif igang:
        #oppdaterer (ting går dit det skal osv) og tegner delene på skjermen
        pack.oppdater()
        fiende.bevege()
        fiende.tegn2()
        lab.tegn2()
        pack.tegn2()
        if poeng.oppdater(): #denne metoden returnerer true dersom spiller har tatt mynten
            sum+=1 #legger en til i telling av poeng
            coin.play() # Lager lyd hver gang en mynt plukkes opp
        poeng.tegn2()
        if sum>=1: # skjekker om spiller har fått nokk poeng for å komme til neste brett
            sum=0 # resetter tellingen til 0
            if bane>=(len(baner)): #her skjekker vi om vi har kommet gjennom alle banene.
                # måten vi gjør dette er å sammenligne lengden av listen med filer med en variabel som teller hvilken bane vi er på 
                #hvis vi nå har kommet gjennom alle banene vi variabelene som holder styr på fase i spillet opptateres
                igang=False
                sluttvunnet=True
                pygame.mixer.music.stop()
                vinne.play()

            else: #hvis ikke spilleren er ferdig med alle banene vil vi sende neste banefil inn i metoden byttBane for å bytte bane
                lab.byttBane(baner[bane])
                pack.byttBane(baner[bane])
                fiende.byttBane(baner[bane])
                bane+=1 #og oppdatere hvilket banenummer vi foreløpig er på

        #skriver midlertidig poengsum
        tekst2= font.render(str(sum), True, "White") 
        skjerm.blit(tekst2, (skjerm.get_width()/40, skjerm.get_height()/60))
        if pack.livEllerDød()==False: #denne metoden returnerer False dersom packman har truffet en fiende.
            igang=False
            slutt=True #merk denne slutt variabelen har et annet navn enn den som blir true dersom spiller har vunnet
            game_over.play()
            pygame.mixer.music.stop()

        
        # Lager bakgrunnsmusikken for spillet
        print(time.time() - start_tid) # Printer ut hvor lenge musikken har spilt
        if (sound == False): # Sjekker om musikken er pågående
            pygame.mixer.music.play()
            sound = True
        if(time.time() - start_tid >= 156): # Når musikken er spilt ferdig, starter den på nytt
            start_tid = time.time()
            pygame.mixer.music.play()
            sound = False
        
    if slutt: #her har spilleren tapt spillet og denne infoen skrives på skjermen
        tekst3= font.render((f"du tapte"), True, "White")
        tekst3_rect= tekst3.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/2))
        skjerm.blit(tekst3, tekst3_rect)
        tekst4= font.render((f"klikk mellomrom for å starte på nytt"), True, "White")
        tekst4_rect= tekst4.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/3))
        skjerm.blit(tekst4, tekst4_rect)

    if sluttvunnet:# her har spilleren vunnet og dette vises på skjermen
        tekst3= font.render((f"du vant"), True, "White")
        tekst3_rect= tekst3.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/2))
        skjerm.blit(tekst3, tekst3_rect)
        tekst4= font.render((f"klikk mellomrom for å starte på nytt"), True, "White")
        tekst4_rect= tekst4.get_rect(center= (skjerm.get_width()/2, skjerm.get_height()/3))
        skjerm.blit(tekst4, tekst4_rect)
    tast= pygame.key.get_pressed()
    if tast[pygame.K_SPACE] and start==False and igang==False: #skjekker om mellomromknappen er trykket og spille ikke er i startfase eller igang
            #resetter og gjør klar for nytt forsøk
            start=False
            igang=True
            sluttvunnet=False 
            slutt=False
            pygame.mixer.music.stop()
            lab.byttBane("test.txt")
            pack.byttBane("test.txt")
            fiende.byttBane("test.txt")
            sum=0
            bane=0
            sound = False



    pygame.display.flip()

pygame.quit()