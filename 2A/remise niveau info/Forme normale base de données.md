# Forme normale base de données

## Première forme normale (1NF) : atomicité

Chaque colonne de vos tables doit être atomique, contenir une et une seule information. Cela implique :

- Pas de colonne qui contiennent de liste
- Pas de colonne calculée

Par exemple si la table LIVRE suivante:



| <u>id</u> | Titre          | Auteur Nom | Auteur Prénom | Auteur      | Thème                             |
| --------- | -------------- | ---------- | ------------- | ----------- | --------------------------------- |
| 1         | Les Miserables | Hugo       | Victor        | Victor Hugo | Misère, justice sociale           |
| 2         | Bakuman.       | Tsugumi    | Ōba           | Tsugumi Ōba | Magaka, ascension professionnelle |

Présente deux problèmes :

- La colonne Auteur se déduit de Auteur Nom et Auteur Prénom, elle est donc inutile
- La colonne Thème contient une liste d'information.

Une solution est de supprimer la colonne Auteur, et de créer une table thème et de faire une association multiple à multiple entre les deux tables.

## Seconde forme normale (2NF)

Un attribut non clé ne dépend pas d’une partie de la clé mais de toute la clé.

| <u>NoClient</u> | <u>NoArticle</u> | NomClient | NomArticle | Prix | qte  |
| --------------- | ---------------- | --------- | ---------- | ---- | ---- |
| 1               | 1                | Bob       | Tondeuse   | 100  | 1    |
| 2               | 1                | Alice     | Tondeuse   | 100  | 3    |
| 1               | 2                | Bob       | Stylo      | 1    | 50   |

Le problème ici :

NomClient dépend uniquement de NoClient, de même pour NomArticle et Prix qui dépendent de NoArticle. Une solution est deux faire deux tables supplémentaire.

Table Client

| NoClient | NomClient |
| -------- | --------- |
| 1        | Bob       |
| 2        | Alice     |

Table Article :

| NoArticle | NomArticle | Prix |
| --------- | ---------- | ---- |
| 1         | Tondeuse   | 100  |
| 2         | Stylo      | 1    |

Table Commande :

| NoArticle | NoClient | qte  |
| --------- | -------- | ---- |
| 1         | 1        | 1    |
| 1         | 2        | 3    |
| 2         | 1        | 20   |

## Troisième forme normale (3NF)

Il n'y a des dépendances qu'entre la clef et les attributs non clef. Par exemple un attributs non clef ne peut pas dépendre d'une autre attribut non clef. Par exemple, la table Tournoi à un problème. En effet la colonne   Winner's date of birth dépend uniquement de Winner qui n'est pas la clef. Il faut alors faire une table supplémentaire.

| Tournament           | Year | Winner         | Winner's date of birth |
| -------------------- | ---- | -------------- | ---------------------- |
| Indiana Invitational | 1998 | Al Fredrickson | 21 July 1975           |
| Cleveland Open       | 1999 | Bob Albertson  | 28 September 1968      |
| Des Moines Masters   | 1999 | Al Fredrickson | 21 July 1975           |
| Indiana Invitational | 1999 | Chip Masterson | 14 March 1977          |

| Tournament           | Year | Winner         |
| -------------------- | ---- | -------------- |
| Indiana Invitational | 1998 | Al Fredrickson |
| Cleveland Open       | 1999 | Bob Albertson  |
| Des Moines Masters   | 1999 | Al Fredrickson |
| Indiana Invitational | 1999 | Chip Masterson |

| Winner         | Date of birth     |
| -------------- | ----------------- |
| Chip Masterson | 14 March 1977     |
| Al Fredrickson | 21 July 1975      |
| Bob Albertson  | 28 September 1968 |