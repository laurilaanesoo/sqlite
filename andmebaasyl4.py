from tkinter import *
import sqlite3

lehekylg = 1 

def loe_andmed(lehekylg):
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sinukasutaja LIMIT ?, 20", ((lehekylg - 1) * 20,))
    andmed = c.fetchall()
    conn.close()
    return andmed

def kuvada_andmed():
    andmed = loe_andmed(lehekylg)
    loend.delete(0, END)
    for rida in andmed:
        loend.insert(END, rida)

def lehekylge_edasi():
    global lehekylg
    lehekylg += 1
    kuvada_andmed()
    sisestus.delete(0, END)
    sisestus.insert(0, lehekylg)

def lehekylge_tagasi():
    global lehekylg
    lehekylg -= 1
    if lehekylg < 1:
        lehekylg = 1
    kuvada_andmed()
    sisestus.delete(0, END)
    sisestus.insert(0, lehekylg)

aken = Tk()
aken.title('Andmete kuvamine')
aken.geometry('600x600')

silt = Label(aken, text="Toodete nimekiri:")
silt.pack()

loend = Listbox(aken, height=10, width=70)
loend.pack(side=LEFT, fill=Y)

kerimine = Scrollbar(aken)
kerimine.pack(side=RIGHT, fill=Y)
loend.configure(yscrollcommand=kerimine.set)
kerimine.configure(command=loend.yview)

nupp = Button(aken, text="Kuva andmed", command=kuvada_andmed)
nupp.pack()

# nupud lehekülje muutmiseks
tagasi_nupp = Button(aken, text="-", command=lehekylge_tagasi)
tagasi_nupp.pack(side=LEFT)

sisestus = Entry(aken, width=5)
sisestus.insert(0, lehekylg)
sisestus.pack(side=LEFT)

edasi_nupp = Button(aken, text="+", command=lehekylge_edasi)
edasi_nupp.pack(side=LEFT)

aken.mainloop()