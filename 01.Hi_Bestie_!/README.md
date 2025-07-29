# Introduction

Bon retour ! Devinez qui est de retour ? Encore de retour ? C'est Python ! 🐍

Il est temps de passer à un autre niveau avec Python, il est enfin temps d'ajouter des structures de données à votre boîte à outils.

De la création de GIF fantaisistes de Nyan Cat 🌈 à l'optimisation d'algorithmes de machine learning 🤖, les vastes bibliothèques et structures de données de Python en font un langage puissant pour le traitement et la collecte de données. Préparez-vous à libérer votre créativité !

# Retour aux sources

La compréhension des types de données est essentielle pour organiser et manipuler les informations en Python.

Passons en revue nos types de données fondamentaux :

🔢 int: Nombres entiers comme 0, 1, -4, 200.
🎈 float: Nombres décimaux comme 3,14, 0,0, 12,99.
🧵 str: Séquences de caractères, entre guillemets comme « salut ! »
✅ bool: Représentations booléennes d'une valeur True ou False.
Les structures de données sont des conteneurs qui nous permettent d’organiser et de stocker efficacement les données.

Vous vous souvenez des listes Python ? C'étaient des structures de données ! Une liste list stocke différents types d'éléments dans l'ordre, simplifiant ainsi l'organisation et la manipulation des données.

social_platforms = ['TikTok', 'Instagram', 'BeReal']

Dans ce chapitre, nous nous concentrerons sur trois nouvelles structures de données :

Tuples
Dictionnaires
Ensembles
Chaque structure de données possède ses propres atouts et choisir la « bonne » peut considérablement améliorer votre programme. 💪

Apprenons comment chacun d’eux fonctionne et quand les utiliser !

# Instructions

Tout d’abord, un petit rappel rapide sur les listes.

Dans un monde où l'utilisation des réseaux sociaux occupe en moyenne plus de deux heures par jour, il est difficile de se tenir au courant de l'argot. Dressons une liste de vos expressions préférées, à la mode ou galvaudées ! 😎

Par exemple:

genz_slang = ['bestie', 'tea', 'cap', 'sus']

Alors, allez-y et imprimez votre liste !

# Aide

Vous pouvez soit imprimer une liste entière :

millennial_texts = ['lol', 'dude', 'fml', 'jk']

print(millennial_texts)    # Output: ['lol', 'dude', 'fml', 'jk']

Un à la fois avec des indices :

print(millennial_texts[0]) # Output: lol
print(millennial_texts[1]) # Output: dude
print(millennial_texts[2]) # Output: fml
print(millennial_texts[3]) # Output: jk

Ou un élément à la fois avec une for boucle :

for item in millennial_texts:
  print(item)