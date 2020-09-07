# Remise à niveau en informatique, exercice python algorithmique

Certains exercices de cette fiche sont tirées du cours de Hong-Phuong Dang dispensé aux 1A.

## Les variables

### Exercice 1 : jouons avec les variables, pour se mettre en jambe

À votre avis que valent les variables first et second, ces instructions ?

- Bloc 1 :
    ````python
    first = 6
    second = first + 9
    first = second
    second = 11
    ````
    
- Bloc 2 :

    ````python
    first = 7
    second = first + 5
    first = first - 4
    second = first * 9
    ````

- Bloc 3 :

    ````python
    first = 10
    second = first % 3
    second = second + 2
    first = second //2
    ````

### Exercice 2 : jouons avec des variables, pour comprendre le typage

Vous devez affecter les valeurs des expressions ci-dessous dans une variable puis afficher le résultat. Attention ! ! ! Certaines des expressions ne sont pas valides, dans ce cas expliquez l’erreur et corrigez l’expression.

1. 4-7
2. "il fait " + 20 + "degrés"
3. 3*2.5+4
4. "Je veux avoir " + 20" + "en remise à niveau"

### Exercice 3 : permutation

Ecrivez un script qui permet d'inverser les valeurs de deux variables. Par exemple

- Input : first = "foo"; second = "bar"
- Output : first = "bar"; second = "foo"

### Exercice 4 : encore plus de permutations

Les variables x, y, z et w valent respectivement 7, 2, 0 et 1.Ecrire une programme afin de permuter les valeurs de ces variables selon :

- x prend la valeur de y
- y prend la valeur de z
- z prend la valeur de w
- w prend la valeur de x

Afficher x, y, z et w pour vérifier.

### Exercice 5 : écrivons des phrases

Définissez 4 variables :

- `identifiant` : la valeur est libre
- `profil` : la valeur est libre
- `phrase_debut` : vaut la valeur "Bonjour "
- `phrase_fin` : vaut la valeur ". Votre profil est : "

Afficher la texte qui résulte de la concaténation des 4 variables. Exemple : "Bonjour Bob. Votre profil est : cuisinier"

### Exercice 6 : journée de travail

Considérons maintenant deux variables numériques heure et minute dont les domaines de valeur sont les nombres entiers compris respectivement entre 0 et 23, et 0 et 59, ainsi qu’une variable textuelle jour pouvant prendre les valeurs ’lundi’, ’mardi’, ’mercredi’,’jeudi’, ’vendredi’, ’samedi’, ’dimanche’. La valeur de ces variables servira à indiquer le jour et l’heure actuels. Créez (en utilisant des expressions logiques) une variable booléenne temps qui est vraie (`True`) si la date et l’horaire actuels sont :

1. Un jour de semaine (hors week-end).
2. En dehors des heures de travail, c’est-à-dire soit le week-end, soit avant 8h ou à partir de 18h
3. Un vendredi à partir de 18h30.
4. N’importe quel jour entre 12h30 et 13h45 inclus.
5. Un jeudi à n’importe quelle heure ou entre 15h et 18h15 pour n’importe quel autre jour.

### Exercice 7 : des listes

Définissez une variable de type liste appelé `liste_input` avec les valeurs suivante : 1, 2, "test", True, 4, 5. Définissez une variable qui pointe vers la même liste. Définissez une variable qui est une copie en valeur de `liste_input`.

Modifier le premier et le dernier élément de `liste_input`. Afficher le premier et le dernier éléments des deux autres listes pour voir comment elles ont évolué.

### Exercice 8 : dictionnaire

Copiez le code ci-dessous :

````python
remise_a_niveau = {
    "UE" : "Informatique pour la data science",
    "module" : "remise_a_niveau",
    "nb_eleve":20,
    "eleves": ["eleve1", "eleve2", "eleve3"]
}
````

- Afficher les valeurs associées à toutes les clefs du dictionnaire.

- Modifier la valeur associée à la clef "nb_eleve" et passez la à 3
- Ajouter une clef `annee` qui vaut la valeur `"2020-2021"`

## Conditions

### Exercice 1 : pair/impair

Définissez une variable définie avec une valeur entière. Affichez pair si cette valeur et pair et impaire si elle est impaire.

### Exercice 2 : Fizz/Buzz

Écrivez un script qui prend en entrée un entier et qui va écrire FIZZ si cette entier est multiple de 3, BUZZ s'il est multiple de 5 et FIZZ BUZZ s'il est multiple de 3 et 5. Affichez le nombre dans tous les autres cas

### Exercice 3 : Pile étape 1

Écrivez un script qui prend une liste en entrée, supprime le dernier élément de la liste et l'affiche si elle n'est pas au préalable vide. Si elle est vide, le script affiche "Pile vide, rien à faire"

### Exercice 4 : journée de travail le retour

Considérons maintenant deux variables numériques heure et minute dont les domaines de valeur sont les nombres entiers compris respectivement entre 0 et 23, et 0 et 59, ainsi qu’une variable textuelle jour pouvant prendre les valeurs ’lundi’, ’mardi’, ’mercredi’,’jeudi’, ’vendredi’, ’samedi’, ’dimanche’. La valeur de ces variables servira à indiquer le jour et l’heure actuels. Grâce à ces variables, écrivez uns script qui affiche "temps de pause" si la date et horaire sont :

1. Un jour de semaine (hors week-end).
2. En dehors des heures de travail, c’est-à-dire soit le week-end, soit avant 8h ou à partir de 18h
3. Un vendredi à partir de 18h30.
4. N’importe quel jour entre 12h30 et 13h45 inclus.
5. Un jeudi à n’importe quelle heure ou entre 15h et 18h15 pour n’importe quel autre jour.

## Boucles `for` et `while`

### Exercice 1 : afficher les 10 premiers entiers

Écrivez une boucle qui affiche les 10 premiers entiers. 

- Avec une boucle ` for` : Pour avoir un objet sur lequel faire votre boucle faites `range(11)`
- Avec une boucle `while`

### Exercice 2 : suite de Fibonacci

Implémentez la suite de de Fibonacci. Pour rappel cette suite est définie par récurrence par la formule : $F_n = F_{n-1} + F_{n-2}$ avec $F_0 = 0$ et $F_1=1$. Affichez les 30 premiers termes de cette suite.

### Exercice 3 : suite de Fibonacci 2

Afficher les termes de la suite de Fibonacci inférieurs à 10 000.

- Avec une boucles `while`
- Avec une boucle `for`

### Exercice 4 : crible Eratosthène

Le crible Eratosthène est un algorithme simple pour calculer exhaustivement les nombres premiers dans un certain intervalle. En commençant par 2, on va mettre 2 dans la liste des nombres premiers, puis supprimer de notre intervalle tous les multiples de 2. Puis on prend le supérieur à 2 toujours présent dans notre intervalle qui vaut 3 et on le met dans la liste des nombres premiers. On supprime de notre intervalle les multiples de 3 et on continue jusqu'à avoir un intervalle vide.

### Exercice 5 : pyramide

Utiliser une boucle pour afficher les $n$ premières lignes d’un triangle d’étoiles. Par exemple pour $n= 5$ :

\*\*\*\*\*\*\*\*\*

 \*\*\*\*\*\*\*

   \*\*\*\*\*

​     \*\*\*

​       \*

## Fonctions

### Exercice 1 : suite de Fibonacci 3

Reprenez le code de la suite de Fibonacci et mettez le dans une fonction. Affichez les 10 premiers éléments de la suite

### Exercice 2 : Fizz/Buzz 2

Reprenez le code de l'exercice Fizz/Buzz pour le mettre dans une fonction. Votre fonction devra retourner FIZZ si cette entier est multiple de 3, BUZZ s'il est multiple de 5 et FIZZ BUZZ s'il est multiple de 3 et 5 ou le nombre dans les autres cas.

### Exercice 3 : Hello world

Ecrivez une fonction `hello_world` qui prend un paramètre optionnel `nom`. La fonction retourne "hello [contenu de la variable nom]" ou "hello world" si la variable nom n'est pas passé en paramètre lors de l'appel de la fonction.

### Exercice 4 : max de nombres

Ecrivez une fonction qui prend en paramètre un nombre quelconque de nombre et qui retourne le max de ces nombres.

### Exercice 5 : changement de base

Ecrivez une fonction qui prend un entier `entier_base_10` en entré et un entier `base` et retourne l'écriture de `entier_base_10` dans la base défini par `base`