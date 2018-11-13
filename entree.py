#!/usr/bin/env python3
import re, sys,os
def testvcf(fichier):
	r=re.search(".*.(vcf)", fichier)
	if r:
		print("le fichier est un vcf")
	else:
		print("il ne s'agit pas d'un fichier vcf")

testvcf(sys.argv[1])

def testtaille(fichier):
	taille = os.path.getsize(fichier)
	if taille > 0:
	 	print("le fichier n'est pas vide")
	else:
	 	print("le fichier est vide")

testtaille(sys.argv[1])