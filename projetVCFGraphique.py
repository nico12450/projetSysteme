#!/usr/bin/env python3

import projetVCF as vcf

import tkinter as tk
import tkinter.scrolledtext as tkst

fenetre = tk.Tk()

"""
label = Label(fenetre, text="Hello World")
label.pack()
"""

frame1 = tk.Frame(
    master = fenetre,
    bg = '#808000'
)

frame1.pack(fill='both', expand='yes')

editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)

editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)



for l in vcf.dico:
	value = tk.StringVar()

	value.set(l + " " + str(vcf.dico[l]))

	editArea.insert(tk.INSERT,value)
"""
	entree = Entry(fenetre, textvariable=value, width=200)
	entree.pack()
"""

"""
canvas = Canvas(fenetre, width=150, height=120)
txt = canvas.create_text(value)
canvas.pack()
"""

fenetre.mainloop()