#!/usr/bin/env python3

import re, os, sys, projetVCF

liste = projetVCF.recupererFichier("human_CEU_MEI.vcf") #stockage des lignes du fichier dans cette liste
lireentete = projetVCF.extraireEntete(liste)  #extraire les entetes des lignes du fichier

def testerformat(l):
	format = re.search("#fileformat=(.+)",l[0])
	if format:
		return format.group(1)
	else:
		print("pas de format dans l'entete du fichier")
		return null



print("format : ",testerformat(lireentete))







