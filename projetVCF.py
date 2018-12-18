#!/usr/bin/env python3

import re, sys, os
import matplotlib.pyplot as plt

def recupererFichier(nomFichier):

	f = open(nomFichier, "r")

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

#cree un dictionnaire de données à partir d'un fichier vcf
def creerDico(lignes):

	dicoVariants = {}
	
	for i in lignes:

		categories = re.search(r"^(?!#)(..?).*?\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*?)\s(.*)",i)

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

#cree un dictionnaire contenant les types de variations et leur nombre
def creerDicoAlternatives(lignes):

	dicoAlternatives = {}

	for i in lignes:
		#on récupère l'alternative pour vcf de differents types

		alt = re.search(r"\s<(.*?)[:>]", i)
		alt2 = re.search(r"^.*?\s.*?\s.*?\s([A,T,G,C]*?)\s([A,T,G,C]*?)\s",i)

		if alt:

			alt = alt.group(1)

			if alt not in dicoAlternatives:

				dicoAlternatives[alt] = 1

			else:

				dicoAlternatives[alt] += 1

		else:

			if alt2:

				ref = alt2.group(1) 
				alt = alt2.group(2)

				#on compare la longueur de la référence et de l'alternative pour determiner le type de variant

				if len(ref) > len(alt):
					alt = "DEL"

				elif len(ref) == len(alt):
					alt = "SUB"

				else :
					alt = "INS"

				if alt not in dicoAlternatives:

					dicoAlternatives[alt] = 1

				else:

					dicoAlternatives[alt] += 1


	return dicoAlternatives


#verifie qu'un nom de fichier entré en paramètre est bien de type vcf
def estVCF(nomFichier):
	r=re.search(".*.(vcf)", nomFichier)
	if r:
		#print("le fichier est bien de type vcf")
		return True
	else:
		print("il ne s'agit pas d'un fichier vcf")
		return False

#verifie qu'un fichier entré en parametre n'est pas vide
def nonVide(fichier):

	taille = os.path.getsize(fichier)

	if taille > 0:

	 	#print("le fichier n'est pas vide")
		return True

	else:

		print("le fichier est vide")
		return False


#verifie qu'ene ligne de format est bien présente dans l'entête du fichier dont la liste des lignes est passée en paramètre
def testerformat(l):
	format = re.search("#fileformat=(.+)",l[0])
	if format:
		return format.group(1)
	else:
		print("pas de format dans l'entete du fichier")
		return null


#renvoie le format vcf du fichier dont la liste des lignes est passée en paramètre
def formatVCF(l):
	format = re.search("#fileformat=(.+)",l[0])
	if format:
		return format.group(1)
	else:
		print("pas de format dans l'entete du fichier")
		return null

"""
entete = extraireEntete(lignes)
afficherListe(entete)
print(testerEntete(entete))
testerFichier(lignes)
"""

lignes = []
dico = {}
dicoAlt = {}

if(len(sys.argv)>1):

	nomF = sys.argv[1]
	print("on utilise le fichier " + nomF)

	if estVCF(nomF) and nonVide(nomF):

		lignes = recupererFichier(nomF)
		print("format du fichier :", formatVCF(lignes))

else:

	print("pas de nom de fichier en entrée, on utilise human_CEU.vcf par défaut")
	lignes = recupererFichier("human_CEU.vcf")
	print("format du fichier :", formatVCF(lignes))

if testerFichier(lignes):
	dico = creerDico(lignes)
	dicoAlt = creerDicoAlternatives(lignes)

#print(dico)
#on récupère la liste des chromosomes du dictionnaire créé précedemment

chromosomes = dico.keys()
#print(chromosomes)

#on va stocker le nombre de variants pour chaque chromosome
variantsParChromosome = []

for c in chromosomes:
    variantsParChromosome.append(len(dico[c]))

#on stocke la liste des alternatives
alternatives = dicoAlt.keys()
variantsParAlternatives = []

for a in alternatives:
	variantsParAlternatives.append(dicoAlt[a])


#print(variantsParChromosome)

#on affiche un diagramme circulaire du nombre de variants par chromosome

plt.pie(variantsParChromosome, labels=chromosomes)
plt.title("diagramme circulaire du nombre de variants par chromosomes")
plt.axis('equal')
plt.show()

#on affiche un diagramme en batonnet du nombre de variants par chromosome

plt.bar(chromosomes,variantsParChromosome)
plt.title("diagramme en batonnet du nombre de variants par chromosome")
plt.show()

#on affiche un diagramme circulaire du nombre de variants par type d'alternative

plt.pie(variantsParAlternatives, labels=alternatives)
plt.title("diagramme circulaire du nombre de variants par type d'alternative")
plt.axis('equal')
plt.show()

#print(dicoAlt)
#afficher le nombre de variants pour le chromosome 4
#print(len(dico["4"]))

#afficher les variants du chromosome 5
#print(dico["5"])



