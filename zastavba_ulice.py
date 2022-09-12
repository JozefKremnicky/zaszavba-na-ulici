import tkinter
canvas=tkinter.Canvas(width=800,height=200, background='white') #vytvorenie platna
canvas.pack()

def vykresli():
    subor = open('zastavba.txt','r') #otvorenie suboru a nastavenie ho na citanie
    y = 150
    x = 10
    for riadok in subor: #for cyklus na citanie suboru
        cisla = riadok.split()
        sirka = int (cisla[0])
        vyska = int (cisla[1])
        if vyska > 0:
            canvas.create_rectangle(x,y-vyska,x+sirka,y,fill='grey')#vytvorenie budov
        else:
            canvas.create_line(x,y,x+sirka,y,fill='green',width=5) #vytvorenie zeleneho pasu v meste
        x+= sirka
        
    subor.close()# zavretie suboru
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='vykresli',command=vykresli)#vytvorenie buttonu
button1.pack()

