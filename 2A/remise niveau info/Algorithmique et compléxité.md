# Algorithmique et compléxité

> Ce support de cours est un notebook python. C'est ainsi un support intéractif. Vous pouvez lancer chaque bloc de code via le bouton play en haut de la page une fois le bloc sélectionné. Vous pouvez même (et c'est l'intérêt principal pour un cours) altérer le code ou insérer de nouvelle cellule de code (bandeau en haut > insert > ...) pour faire des tests.

## Pyhton en général

Python est un langage de programmation multi paradigme (imperatif, fonctionnel, objet). Crée par Guido van Rossum ) partir des années 1990, il a vu sa popularité exploser dans les dernières années grâce à sa simplicité, son efficacité. Mais c'est surtout dans les data science où il brille aujourd'hui. Du fait que ce soit un langage de programmation il permet plus de liberté que R dans la création de programme. Et comme c'est un langage libre avec une communauté active il existe de nombreuses bibliothèques pour faire un peu tout et n'importe quoi en python.

Pour votre culture, il existe plusieurs implémentations du python. Les plus connues sont CPython (écrit en C, et c'est l'implémentation stantard) et PyPy (écrit en Python et ça c'est beau !). La grande différence entre les deux est que CPython va compiler en bytecode votre programme avant de l'interpréter, alors que PyPy l'interpréte juste. Cela va influer sur les performances de votre programme.
![](https://raw.githubusercontent.com/HealerMikado/Cours-Ensai-Informatique/master/2A/remise%20niveau%20info/img/type%20langage.png)
Pour votre culture il existe 3 grands types de langage de programmation :

- Les langages interprétés ;
- Les langages compilés ;
- Et les langages qui sont les deux à la fois.

Pour comprendre pourquoi, il faut réaliser qu'un ordinateur ne comprend nativement que le langage dit "assembleur". C'est un langage de bas niveau, quasiment incompréhensible pas un humain. Et il est très fastidieux de coder en assembleur, surtout pour des tâches complexes. C'est pour cela que des langages de haut niveau sont apparus. Ils apportent une abstraction (= cachent certains mécanismes) pour nous permettre de nous concentrer sur l'essentiel. Le problème est que notre ordinateur ne comprend toujours que l'assembleur. Donc nos nouveaux langages ont besoin d'un mécanisme de traduction vers le code assembleur. Et il en existe deux :

- **La compilation** consiste à transformer un fichier contenant du code haut niveau en un fichier contenant du code de bas niveau exécutable par une machine spécifique. Le programme qui va transformer notre code est un **compilateur**. Compiler du code est un long car il faut que le compilateur lise le code en entier (et un programme peut avoir plusieurs dizaine de milliers de lignes assez facilement). Comme il connait l'intégralité du code il en profite pour réaliser quelques optimisations. Le majeur problème de cette solution, c'est que le code produit n'est utilisable que par un type de machine, et il faudra le compiler autant de fois qu'il y a de machine cible (avec des performance pouvant varier grandement d'un type machine à l'autre). 
  Une comparaison du monde courant est la traduction d'une livre. Si je demande à un traducteur de traduire un livre il va devoir le lire en entier, et va prendre son temps pour trouver les meilleurs formulations. Si je veux la traduction dans une autre langue, je vais devoir recommencer le travail de zéro et embaucher un nouveau traducteur.
  Exemple de langage compilée : C
- **L'interprétation** consiste exécuter le code à la volée. Notre code source va être lu par l'interpréteur qui va traduire le code en commande que la machine va exécuter. Par contre ici pas d'optimisation car le code et lu au fur et à mesure. L'avantage, c'est que si vous voulez juste tester une fonction de quelques lignes, seules ces lignes vont être lues.
  Une comparaison du monde courant pourrait être la lecture d'un menu dans une langue étrangère. Vous allez lire le menu à la volée, et une fois que vous savez ce que vous voulez vous allez arrêter votre lecture.
  Exemple de langage compilée : JavaScript

Mais ces deux mécanismes ne sont pas opposé, et on peut les assembler pour faire des langages compilé et interprété. C'est le cas de Python (avec la distribution CPython) et Java par exemple. Votre code source est d'abord compilé dans un langage appelé le *bytecode*, c'est un langage bas niveau pas pas directement exécutable. Ce code est ensuite lu par un interpréteur qui va exécuter au fur et à mesure.

Vous êtes en droit de vous demander pourquoi ? En effet on peut avoir l'impression de subir le pire des deux mondes. Et en fait, pas tant que ça. La compilation en bytecode permet de réaliser quelques optimisations, et le fait de dépendre d'un interpréteur permet un portage facile de votre code. Si vous codez en Python, vous pouvez envoyer votre code à n'importe qui, tant qu'il a Python sur sa machine il pourra exécuter votre programme et le modifier sans problème. Pour un développeur, cela permet d'envoyer son code directement sur un serveur sans savoir quel type de serveur c'est tant que Python est dessus.



## Algorithmique

Bien qu'appliqué au langage Python, les notions de la partie qui suit ne sont pas spécifiques à Python. Certes les syntaxes le sont, mais les idées sous jacentes ([variables](#Les-variables), [structure de contrôle](#Les-structures-de-contrôle-du-flux), [Les fonctions](#Les-fonctions) et la récursivité) sont applicables pour tous les langages impératifs, et la description d'algorithme en général.

Petit point vocabulaire :
- Algorithme : Ensemble d'opérations élémentaires dans le but de résoudre un problème.
  - pas forcément informatique
  - pas forcément implémenté
- Programme informatique : l'implémentation informatique d'un algorithme
- Script : programme informatique qu'on fait que lancer avec peu interaction avec l'utilisateur (abus de langage).

## Les variables

Un programme Pyhton accède aux données via des **références**. Une référence est un simple "nom" auquel est liée une donnée. Il y en a plusieurs type :

- **variables**
- attributs (discuté plus longtemps lors du cours de programmation orientée objet)

### Déclaration

À la différence d'autres langages, en Python il n'y a pas de syntaxe spécifique à la déclaration d'une variable. Vous avez juste à écrire le nom de votre variables et lui lier une valeur. Vous pouvez également si vous le souhaitez lier une nouvelle valeur à une variable déjà existante.

Voici quelques exemples de base

### Typage

Python est une langage avec un **typage forte** mais il est également **dynamique**.

- Typage fort : si vous essayez de réaliser une opération sur un type de variable qui ne dispose pas de cette opération cela va générer une erreur.
- Typage dynamique : Python va typer dynamiquement les variables que vous lui passez. Vous n'avez pas besoin de savoir le type à l'avance, Python l'infère à la volée. On appelle cela le *Duck Typing*. Pour python "Si cela ressemble à un canard, nage comme un canard et fait le bruit d'un canard, alors c'est sûrement un canard", vous n'avez pas à donner le type explicitement. Le principe est que c'est la donnée qui détermine son comportement et pas le développeur. Cela permet d'écrire du code très rapidement, mais le rend compliqué à lire.

![](https://i.imgflip.com/48fifm.jpg)

### Les types de données

Il existe une grande variété de type de variable en python. En voici une petit sélection :

- Type numérique
    - integer (nombre entier, potentiellement infini)
    - float (décimal avec une précision de 53²)
    - complex (nombre complexe)
- str (string, chaîne de caractère)
- tuple (séquence ordonnée non mutable d'objet )
- list (séquence ordonnée mutable d'objet)
- set (séquence ordonnée non mutable d'objet unique)
- dictionnaire (collection de couple clef-valeur)
- booléen (true/false)

#### Les types numériques

Comme noté au dessus, il existe plusieurs types de données numériques en python, chacun avec des spécificités.

##### Integer

Les integers représentent un nombre entier (positif ou négatif). Ils ne sont pas bornés (donc potentiellement infini si vous avez une mémoire infinie), et peuvent être représenté de différentes formes

- littéralement (la forme la plus usuelle. Exemple 42, 12, 1456)
- sous forme binaire (0b101010, 0b110, 0b10110110000)
- sous forme octal (0o52, 0o14, 0o2660 )
- sous forme hexadecimal (0x2A, 0xC, 0c5B0) 

Je ne vous cache pas que la première forme sera la plus utilisée.

##### Float

Les floats (floating point) représentent un nombre décimal. Ils ont une précision de 53² et peuvent s'écrire soit avec un . ou avec un suffixe *e* pour les puissances de 10

- 0., 0.1, .2
- 1e10, 231e-5

##### Complex

Les complexs représentent un nombre complexe. Se définissent comme les floats avec un préfixe j à la fin pour la partie imaginaire.

- 2j, 0.3j, 23e-1j : uniquement imaginaire
- 1+2j, 0.3 + 1e-6j : partie réelle et imaginaire

##### Opérations sur les types numériques

Voici quelques opération sur des types numériques





#### Les chaînes de caractères (string ou str)

Les chaînes de caractères représentent un texte en python. Ils doivent être défini entre " ou '. Certains opérateurs agissent différemment sur les chaînes de caractères

- \+ : concaténation
- \* : répétition
- [] : indexation

Quelques exemples



Comme vous allez le voir, on peut considérer un string comme une collection de caractères. Il est important de s'en souvenir, car cela permet de récupérer facilement le caractère à une certaines position et d'itérer sur les lettes qui composent un string.

#### Les listes

La liste (list) est un des types de variable le plus utilisé en python. C'est un tableau **ordonné**, **dynamique** d'élements qui peuvent être de type différents. Pour définir une liste il faut utiliser les []

Voici une liste des principales opérations sur les listes :

- ma_liste[*i*]  avec i un entier : permet d'accéder à la valeur à l'indice i. Attention, l'indice du premier élément est 0 en Python. Il est également possible de faire maListe[*-i*] pour partir de la fin. Dans ce cas le dernier élément est d'indice -1. Donc pour accéder au dernier élément il faut faire ma_liste[-1]
- ma_liste[*i:j*] : extrait une sous liste de ma_liste qui commence à l'indice *i* inclue et va jusqu'à l'indice *j* exclu
- ma_liste[*i*] = *valeur* : permet de modifier l'élément à l'indice i en le rendant égal à *valeur* 
- ma_liste.append(*valeur*) : ajoute un élément égale à *valeur* à la liste 
- lent(ma_liste) : retourne le nombre d'élément dans la liste
- ma_liste.pop() : supprime le dernière élément de la liste
- ma_liste.pop(*i*) : supprime l'élément d'indice *i*
- ma_liste.extend(mon_autre_liste) : concatène deux listes



Les listes sont des variables très souples qui peuvent contenir beaucoup de choses et sont très facile d'utilsattion. Un peu plus tard on va voir  comment itérer sur les éléments d'une liste pour exécuter des opérations sur chaque élément.

En plus de la version manuelle de création d'une liste, python permet également de créer une liste de manière un peu plus automatique. Par  exemple si je veux créer une liste avec les 10 premiers multiples de 3  voici une syntaxe plus rapide qu'écrire tous les nombres à la main. On appelle cette façon de faire la *list comprehension*

**Attention** du fait qu'une liste soit une variable *mutable* l'opérateur "=" fonctionne par référence (on ne passe pas une valeur,  mais une référence mémoire). Cela peut vous apporter quelques surprises. C'est un concept un peu compliqué que l'on reverra plus tard. Il faut garder en tête que dans les langage moderne les variables complexes (comme les listes) l'opération d'égalité n'est pas toujours une égalité de valeur, mais peut être une égalité de référence. 

![](https://raw.githubusercontent.com/HealerMikado/Cours-Ensai-Informatique/master/2A/remise%20niveau%20info/img/mutation.png)



#### Les booléens

Les booléens (boolean) représentent une valeur True ou False. Sauf qu'en python tout type de donnée peut être utilisé  comme un booléen. Toute variable non égale à 0 ou vide vaut pour une valeur True, alors que 0, None ou un container (list, set, dictionnaire) vide vaut pour False



#### Les dictionnaires

Autre type de données très pratique en Python, les dictionnaires permettent de stocker des couples clefs-valeurs de données et accéder facilement aux valeur quand on connait la clef. Ce sont des variables mutables également. Voici un exemple :





### Mutable / non mutable qu'est ce que cela va dire ?

Voici une petite explication sur le concept de mutabilité. Ceci est une notion un peu fine d'informatique donc si vous ne la comprenez pas de suite ce n'est pas grave.

En python (et plus généralement en langage informatique), **la mutablilité représente la capacité d'un objet à être modifié**. Donc un objet mutable est une objet que l'on va pouvoir modifier alors qu'un objet non mutable ne pourra pas l'être.

🤔"Cela veut dire qu'une fois une variable non mutable créée je ne vais pas pouvoir la modifier ?"

Oui et non. En effet vous n'allez pas pouvoir la modifier, par contre vous allez pouvoir lui associer une nouvelle valeur sans problème. Petit exemple :



Petite explication :
- j'ai crée une variable x égale à 10 et une variable y égale à x.
- j'ai changé la valeur à x, ce qui devrait changer celle de y car y=x
- sauf que comme y est immutable il n'a pas subi la modification apportée à x.

Pareil mais avec une liste (donc un objet mutable)



Avec des objets mutables modifier un objet va automatiquement modifier tous les objets pointant vers le même espace en mémoire. Et même si cela à l'air super bien, je vous assure que par moment cela va vous poser problème car vous allez vouloir modifier un objet sans modifier ses clones (concept de *shallow copy* et *deep copy*).



## Les structures de contrôle du flux

Naturellement l'interpréteur python va exécuter les instructions les unes après les autres sans se poser de question et ainsi exécuter le programme de haut en bas. Si cela suffit pour des programmes très très simple, rapidement cela va poser des problèmes quand on va chercher à réutiliser des bouts de codes un nombre variable de fois, ou exécuter du code suivant des conditions.

Il existe 3 structures de contrôle

- Les conditions if/elif/else
- Les boucles for/while
- La gestions des exceptions (non abordée)

### Les blocs d'instruction

**En Python il n'y a pas de caractère spécial pour créer un bloc d'instructions** à la différence de nombreux autres langages, à la place c'est l'indentation qui va faire foi. En général  on privilégie et indentation de 4 espaces pour dessiner nos bloc. Ainsi pour définir un bloc cohérent d'instruction il va falloir faire

```python
structure de controle :
    instruction 1
    instruction 2
```

### Les conditions if/elif/else

Cette structure est à utiliser quand vous souhaiter exécuter une bout de code quand une condition est remplie. Voici sa forme générale

```python
if expression1:
  #some code
elif expressionn2:
  #some code
elif expression3:
  #some code
  ...
else :
  #some code
```

À part la condition if initiale qui est nécessaire, les autres sont parfaitement optionnelles. Pyhton va exécuter la première expression et si elle renvoie True exécuter le premier bloc puis sortir de la structure if/elif/else. Si elle renvoie False, alors c'est la seconde expression qui sera calculée et ainsi de suite jusqu'à arriver au bloc else qui sera exécuter si toutes les conditions sont fausses. Voici quelques exemples :





 	#### Boucle for

Une boucle for va répéter un bloc d'instruction pour une liste d'éléments sur laquelle on peut itérer. Ça syntaxe de base est

```python
for target in liste:
    #some code
```

Voici différents exemples :





#### Quand utiliser les boucle for et while

S'il y a deux types de boucle c'est qu'il y a une raison. Bien qu'on puisse les interchanger car fondamentalement elles font la même chose, la logique derrière est différente.

Une boucle for vous permet d'itérer sur tous les éléments d'une collection d'objet (list, set, map ...). Dans un cas où vous voulez appliquer des instructions sur tous les éléments d'une collection d'objet alors la boucle for est le bon choix.

Si par contre vous voulez exécuter un bout de code tant qu'une condition zst vrai alors c'est une boucle while (les noms aide beaucoup à comprendre l'utilité des boucles).

Globalement voici un moyen de décider assez facile :
- Si vous savez exactement le nombre d'itération à l'avance => for
- Sinon while

#### Les instructions break et continue

Par moment vous allez avoir besoin de sauter ou de sortir prématurément de vos boucles, pour cela vous avez les instructions break (sortir de la structure) et continue (sauter une étape).

> À titre personnel je déconseille leur utilisation. En effet si dans de rare cas elles peuvent être utiles, dans d'autre elles rajoutent de la complexité cognitive au programme en le rendant plus dur à comprendre et analyser. Et globalement je pense qu'utiliser un break implique d'avoir pris une boucle for alors qu'il fallait une while.

##### Break

Comme dit au dessus, un break permet de sortir d'une boucle. Dans le cas de boucles imbriquées cela permet de sortir uniquement de la boucle dans laquelle vous vous trouvez.

Exemple :



Il est rare d'utiliser un `else` dans une boucle (à titre personel je n'ai jamais eu à utiliser cette instruction, mais vous pouvez la rencontrer)

## Les fonctions

Dernière notion de base de l'algorithmique, **les fonctions**. Les fonctions sont des blocs de code que vous allez pouvoir exécuter à la demande. Une fonction peut prendre des paramètres en entrée (mais ce n'est pas obligé), et elle peut retourner une valeur en sortie (mais ce n'est pas obligé). Elles servent uniquement à mieux organiser votre code et à le rendre plus lisible. En effet des fonctions bien faite sont des fonctions qui font peu de choses avec un nom clair pour comprendre leur utilité. Théoriquement il doit être possible de savoir ce que fait une fonction juste avec son nom.

### Création du fonction

Voici la syntaxe pour créer une fonction. Avec :
- `def` : un mon clef propre à Pyhton permettant de déclarer une fonction
- ma_fonction : le nom de ma fonction
- paramètres : une liste optionnelle de paramètres non typé. 
- #some code : un bloc d'instruction python quelconque
- `return` : le mot clef qui permet de dire ce que la fonction renvoie. Attention, une fois le return exécuté on sort de la fonction
- result : une valeur que je retourne

### Appel d'une fonction

Pour appeler une fonction il suffit juste d'utiliser le nom que vous lui avez donnée et de passer les paramètres entre parenthèses.

### Notes 

- Le corps d'une fonction ne peut pas être vide. Si un tel cas se présent utilisez l'instruction `pass`
- Le nom des fonctions doit être unique. Deux fonctions ne peuvent pas partager le même nom même si leur nombre de paramètres est différent 
- Si une fonction nerenvoie rien il est possible de se passer de instruction `return`. Dans ce cas la fonction retournera `None`
- De la même manière que vous ne typez pas les variables lors de leur déclaration, on ne type pas les variables en paramètre des fonctions.
- Pour que votre code soit lisible, vos nom des fonctions doivent être signifiant
- Vous pouvez (et dans un vrai projet devez) rajouter une docstrings à vos fonctions. Elle est entre """ et doit contenir une explication rapide de ce que fait votre fonction.



## Les modules

Les modules permettent d'éclater votre code entre différents fichiers pour qu'il soit plus lisible et maintenable. Un peu comme les fonctions, chaque module va contenir du code relatif à un thème ou un type de manipulation. Plus factuellement, un module est un fichier *.py* qui peut contenir des variables, des fonctions, des classes (cf python orienté objet). Ce fichier peut être appelé par votre programme principal ou un autre module. Python dispose de bases de plusieurs modules importables mais rapidement pour des taches spécifique (machine larning par exemple), vous aller devoir télécharger des module supplémentaire.

Pour réaliser un import deux syntaxes :

- ```python
   import modname [as alias]
  ```
  Permet d'importer le module souhaité en entier et de l'utiliser en préfixant l'objet que l'on souhaite utiliser par le nom du  module. Par exemple