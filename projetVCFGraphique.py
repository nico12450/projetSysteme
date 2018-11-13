#!/usr/bin/env python3

import projetVCF as vcf

from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

for l in vcf.dico:
	value = StringVar()

	value.set(l + " " + str(vcf.dico[l]))

	entree = Entry(fenetre, textvariable=value, width=200)
	entree.pack()

"""
canvas = Canvas(fenetre, width=150, height=120)
txt = canvas.create_text(value)
canvas.pack()
"""

fenetre.mainloop()