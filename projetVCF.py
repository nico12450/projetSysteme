#!/usr/bin/env python3

import re, sys, os

def recupererFichier(nomFIchier):

	f = open("human_CEU.vcf", "r")

	lignes = f.readlines()

	f.close()

	return lignes

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
	structure = re.search(r"CHROM\s*?POS\s*?ID\s*?REF\s*?ALT\s*?QUAL\s*?FILTER\s*?INFO",listeEntete[-1])

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


def creerDico(lignes):

	dicoVariants = {}
	
	for i in lignes:

		categories = re.search(r"^(.\d?)\s(\d*?)\s(.*?)\s([A-Z]*?)\s(.*?)\s(\d*?)\s(.*?)\s(.*?)\n",i)

		if categories:

			chromosome = categories.group(1)
			position = categories.group(2)
			identifiant = categories.group(3)
			reference = categories.group(4)
			alternative = categories.group(5)
			qualite = categories.group(6)
			filtre = categories.group(7)
			informations = categories.group(8)

			if chromosome not in dicoVariants:
				dicoVariants[chromosome] = {}

			dicoVariants[chromosome][position] = {"identifiant" : identifiant, "reference" : reference, "alternative" : alternative, "qualite" : qualite, "filtre" : filtre, "informations" : informations}


	return dicoVariants			

def estVCF(fichier):
	r=re.search(".*.(vcf)", fichier)
	if r:
		#print("le fichier est bien de type vcf")
		return True
	else:
		print("il ne s'agit pas d'un fichier vcf")
		return False

def nonVide(fichier):

	taille = os.path.getsize(fichier)

	if taille > 0:

	 	#print("le fichier n'est pas vide")
		return True

	else:

		print("le fichier est vide")
		return False

"""
entete = extraireEntete(lignes)
afficherListe(entete)
print(testerEntete(entete))
testerFichier(lignes)
"""

lignes = []
dico = {}

if(len(sys.argv)>1):

	nomF = sys.argv[1]
	print("on utilise le fichier " + nomF)

	if estVCF(nomF) and nonVide(nomF):

		lignes = recupererFichier(nomF)

else:

	print("pas de nom de fichier en entrée, on utilise human_CEU.vcf par défaut")
	lignes = recupererFichier("human_CEU.vcf")

if testerFichier(lignes):
	dico = creerDico(lignes)

print(dico)




