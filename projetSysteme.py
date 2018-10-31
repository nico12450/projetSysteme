#!/usr/bin/env python3

import re

f = open("human_CEU.vcf", "r")

lignes = f.readlines()

f.close()


#affiche chaque élément d'une liste ligne par ligne avec son indice au début
def afficherListe(liste):

	i = 0

	for l in liste:

		print("ligne ", i, " : ", end = '')
		print(l)
		i+=1

#afficherListe(lignes)

#renvoie les lignes de l'entete d'un fichier vcf sous la forme d'une liste de chaines de caractères
def extraireEntete(lignes):

	listeEntete = []

	for l in lignes:

		if(l[0] == "#"):

			listeEntete.append(l)

	return listeEntete

#teste si une entete vcf est valide
def testerEntete(listeEntete):

	format = re.search("fileformat=.+",listeEntete[0])
	structure = re.search("CHROM\s*?POS\s*?ID\s*?REF\s*?ALT\s*?QUAL\s*?FILTER\s*?INFO",listeEntete[-1])

	if not format or not structure:
		return False

	return True

#teste si un fichier vcf est valide
def testerFichier(lignes):

	e = extraireEntete(lignes)

	if testerEntete(e):

		print("le fichier est valide")
		return True

	else:

		print("le fichier n'est pas valide")
		return False



			

entete = extraireEntete(lignes)

#afficherListe(entete)

#print(testerEntete(entete))

testerFichier(lignes)

