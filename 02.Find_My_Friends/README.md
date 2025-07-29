# Tuples

Les tuples sont des collections ordonnées qui ne peuvent être modifiées une fois créées. Ils sont idéaux pour stocker des données fixes qui ne doivent pas changer (par exemple, des coordonnées, des valeurs de couleur RVB).

Alors que les listes peuvent changer, les tuples ne le peuvent pas. Cela signifie que les tuples sont immuables.

Cependant, vous pouvez remplacer un tuple par un autre et avoir des doublons dans un tuple.

# Syntaxe

Les listes et les tuples ont quelques points communs :

Ils peuvent stocker plusieurs éléments dans une seule variable.
Leurs valeurs sont séparées par des virgules.
Cependant, les tuples utilisent une syntaxe différente :

tuple_example = (1, '2', True)
navy_blue = (0, 0, 128)

Les tuples sont définis avec ou sans parenthèses et leurs éléments peuvent être un mélange de n'importe quel type de données. Ils peuvent contenir un ou plusieurs éléments.

S'il n'y a qu'un seul élément, assurez-vous qu'il y a une virgule "," à côté :

### valid tuple
t1 = ('a',)

### valid tuple
t2 = 'a',

### NOT a tuple
t3 = ('a')

# Création et accès aux tuples

Par exemple, une séquence d'ADN serait stockée sous forme de tuple car elle contient des valeurs très importantes qui ne doivent pas être modifiées et ne doivent pas changer lorsqu'elles sont référencées sans.

my_dna = ('GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT')

Vous pouvez accéder aux éléments d'un tuple de la même manière qu'avec une liste… grâce à l'index ! Si nous voulons obtenir le troisième élément de notre my_dna tuple :

print(my_dna[2]) # Output: AGG

Étant donné que les tuples sont une collection ordonnée, vous pouvez rechercher leurs éléments par index.

# Utilisation des tuples

Les tuples sont également décompressibles, ce qui permet de les transformer facilement en variables. Le plus souvent, ils sont utilisés comme valeurs de retour, ce qui facilite le traitement de grands ensembles de données.

full_name = ('Ada', 'Lovelace')

first_name = full_name[0]

print(first_name) # Output: Ada

# Combining tuples

Les tuples peuvent également être combinés :

t1 = 'a',
t2 = 'b',
t3 = t1 + t2

print(t3)  # Output: ('a', 'b')

# Instructions

Grâce à Internet, nous pouvons nous connecter avec des amis du monde entier. 🧑‍🤝‍🧑

Lorsque vous et vos amis êtes dispersés dans différentes villes, partager des lieux est quelque chose qui peut vous aider à vous sentir plus proches.

Utilisons la latitude et la longitude 🌐 pour créer des tuples des emplacements de nos amis !

Créez un tuple pour la ville dans laquelle vous vous trouvez.
Créez 3 tuples pour vos amis, chacun avec la latitude et la longitude des villes dans lesquelles ils vivent.
Imprimez les emplacements de tous vos amis.
Lequel de tes amis est le plus loin ?à