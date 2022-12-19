# verze 14.x2
from tkinter import *
import random

class Okno:
    # vlastnosti
        
    # konstruktor
    def __init__(self):
        self.okno = Tk()
        self.cisilka=[4,8,16,32,64,128,256,512,1024,2048]
        self.barvicky=["#EDE0C8","#F2B179","#F59563","#EDC74F","#F65E3B","#EDCF72","#EDCC61","#EDC850","#EDC53F","#EDC22E"]
        self.highscore=0
        self.vyhra=2048
                
        self.inicializaceOkna()
        self.obsahOkna()
        self.zviditelneniOkna()
        
    # metody
    def inicializaceOkna(self):        
        self.okno.title(self.vyhra)
        self.okno.geometry("468x500+200+120")
        self.okno.option_add('*Font', 'Curier 24')
        self.okno.configure(bg='#BBADA0')
            
    def obsahOkna(self):
        self.pocetBodu=0
        self.pokracuj=True
        self.obsahujeCislo=False
        self.tlacitko=[]
        self.obsazeno=0
        
        self.body=Frame(self.okno, pady="6", padx="6", bg="#BBADA0")
        nazev=Label(self.body, text=2048, bg="#BBADA0", fg="#CCC0B3")
        nazev.pack(side=LEFT)
        self.best=Label(self.body, bg="#CCC0B3", font='Calibri 12', fg="#FAF8EF", text="  BEST  \n"+str(self.highscore))
        self.best.pack(side=RIGHT)
        self.score=Label(self.body, bg="#CCC0B3", font='Calibri 12', fg="#FAF8EF", text="SCORE\n0")
        self.score.pack(side=RIGHT, padx="6")
        self.body.pack(fill="x", expand=1)
        
        self.pole=Frame(self.okno, bg='#BBADA0')
        for i in range(4):
            self.radek = []
            for j in range(4):
                self.radek.append(Label(self.pole, width="5", height="2", bg="#CCC0B3", relief="flat", fg="#776E65"))
                self.radek[j].grid(row=i, column=j, padx="6", pady="6")
            self.tlacitko.append(self.radek)
        self.pole.pack(anchor="center")

        self.okno.bind("<Left>", self.vlevo)
        self.okno.bind("<Right>", self.vpravo)
        self.okno.bind("<Up>", self.nahoru)
        self.okno.bind("<Down>", self.dolu)
        self.okno.bind("<Return>" , self.novy)

        self.generuj()
        self.generuj()

                
    def zviditelneniOkna(self):     
        self.okno.mainloop() 

        
    def vlevo(self, udalost):
        if self.pokracuj:
            akce=False
            for j in range(4):
                for i in range(4):
                    if self.tlacitko[j][i]["text"]:
                        for x in range(i+1,4): #tady se to sečte
                            if self.tlacitko[j][i]["text"]==self.tlacitko[j][x]["text"]:
                                self.soucet(j,i,x,1)
                                akce=True
                                break
                            elif self.tlacitko[j][x]["text"]:
                                break
                        for x in range(i): #tady se to posune
                            if not self.tlacitko[j][x]["text"]:
                                self.posun(j,i,x,1)
                                akce=True
                                break
                            
            if akce: 
                self.generuj() #tady se vygeneruje dvojka
            else:
                self.volno()
        
               
    def vpravo(self, udalost):
        if self.pokracuj:
            akce=False
            for j in range(3,-1,-1):
                for i in range(3,-1,-1):
                    if self.tlacitko[j][i]["text"]:
                        for x in range(i-1,-1,-1): #tady se to sečte
                            if self.tlacitko[j][i]["text"]==self.tlacitko[j][x]["text"]:
                                self.soucet(j,i,x,1)
                                akce=True
                                break
                            elif self.tlacitko[j][x]["text"]:
                                break
                        for x in range(3,i,-1): #tady se to posune
                            if not self.tlacitko[j][x]["text"]:
                                self.posun(j,i,x,1)
                                akce=True
                                break
                            
            if akce: 
                self.generuj() #tady se vygeneruje dvojka
            else:
                self.volno()

       
    def nahoru(self, udalost):
        if self.pokracuj:
            akce=False
            for i in range(4): #i=sloupec
                for j in range(4): #j=řádek
                    if self.tlacitko[j][i]["text"]:
                        for x in range(j+1,4): #tady se to sečte
                            if self.tlacitko[j][i]["text"]==self.tlacitko[x][i]["text"]:
                                self.soucet(j,i,x,2)
                                akce=True
                                break
                            elif self.tlacitko[x][i]["text"]:
                                break
                        for x in range(j): #tady se to posune
                            if not self.tlacitko[x][i]["text"]:
                                self.posun(j,i,x,2)
                                akce=True
                                break
                            
            if akce: 
                self.generuj() #tady se vygeneruje dvojka
            else:
                self.volno()

        
    def dolu(self, udalost):
        if self.pokracuj:
            akce=False
            for i in range(3,-1,-1):
                for j in range(3,-1,-1):
                    if self.tlacitko[j][i]["text"]:
                        for x in range(j-1,-1,-1):  #tady se to sečte
                            if self.tlacitko[j][i]["text"]==self.tlacitko[x][i]["text"]:
                                self.soucet(j,i,x,2)
                                akce=True
                                break
                            elif self.tlacitko[x][i]["text"]:
                                break 
                        for x in range(3,j,-1): #tady se to posune
                            if not self.tlacitko[x][i]["text"]:
                                self.posun(j,i,x,2)
                                akce=True
                                break
                            
            if akce: 
                self.generuj() #tady se vygeneruje dvojka
            else:
                self.volno()
            

    def soucet(self,j,i,x,smer):
        self.tlacitko[j][i]["text"]=self.tlacitko[j][i]["text"]*2 #součet hodnot
        barva=self.cisilka.index(self.tlacitko[j][i]["text"]) #zjištění barvy
        self.tlacitko[j][i]["bg"]=self.barvicky[barva] #aplikování barvy
        self.pocetBodu+=self.tlacitko[j][i]["text"]
        self.score["text"]="SCORE\n"+str(self.pocetBodu)
        if self.pocetBodu > self.highscore:
            self.highscore = self.pocetBodu
            self.best["text"] = "  BEST  \n"+str(self.pocetBodu)
        self.obsazeno-=1
        if barva>0:
            self.tlacitko[j][i]["fg"]="white" #aplikování barvy textu
        if self.tlacitko[j][i]["text"]==self.vyhra:
            self.obsahujeCislo=True
            self.volno()
        if smer==1: #doprava/doleva
            self.tlacitko[j][x]["text"]=""
            self.tlacitko[j][x]["bg"]="#CCC0B3"
            self.tlacitko[j][x]["fg"]="#776E65"
        else: #nahoru/dolů
            self.tlacitko[x][i]["text"]=""
            self.tlacitko[x][i]["bg"]="#CCC0B3"
            self.tlacitko[x][i]["fg"]="#776E65"
            

    def posun(self,j,i,x,smer):
        if smer==1: #doprava/doleva
            self.tlacitko[j][x]["text"]=self.tlacitko[j][i]["text"]
            self.tlacitko[j][x]["bg"]=self.tlacitko[j][i]["bg"]
            self.tlacitko[j][x]["fg"]=self.tlacitko[j][i]["fg"]
        else: #nahoru/dolů
            self.tlacitko[x][i]["text"]=self.tlacitko[j][i]["text"]
            self.tlacitko[x][i]["bg"]=self.tlacitko[j][i]["bg"]
            self.tlacitko[x][i]["fg"]=self.tlacitko[j][i]["fg"]
        self.tlacitko[j][i]["text"]=""
        self.tlacitko[j][i]["bg"]="#CCC0B3"
        self.tlacitko[j][i]["fg"]="#776E65"


    def generuj(self):
        i=random.randint(0,3)
        j=random.randint(0,3)
        while self.tlacitko[i][j]["text"]:
            i=random.randint(0,3)
            j=random.randint(0,3)
        self.tlacitko[i][j]["text"]=2
        self.tlacitko[i][j]["bg"]="#EEE4DA"
        self.obsazeno+=1           


    def volno(self):
        self.pokracuj=False
        if not self.obsazeno==16:
            self.pokracuj=True
            
        if self.obsahujeCislo: #2048 = musí se skončit
            self.konec1=Label(self.pole,text="Vyhrál jste!", bg="#BBADA0")
            self.konec1.grid(column=0,row=0,columnspan=4, rowspan=4)
            self.konec2=Label(self.pole,text="Pokračujte stiskem ENTER", font=("Arial", 9))
            self.konec2.grid(column=0,row=3, sticky=S+W, columnspan=2)
            self.pokracuj=False
            return False

        if not self.pokracuj:
            self.konec1=Label(self.pole,text="Konec hry", bg="#BBADA0")
            self.konec1.grid(column=0,row=0,columnspan=4, rowspan=4)
            self.konec2=Label(self.pole,text="Pokračujte stiskem ENTER", font=("Arial", 9))
            self.konec2.grid(column=0,row=3, sticky=S+W, columnspan=2)
            
        return self.pokracuj
    

    def novy(self,udalost):
        self.body.destroy()
        self.pole.destroy()
        self.obsahOkna()
        
O = Okno()  
