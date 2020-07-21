

# TP 2: Data Access Objet (DAO)

> :scream: Comme vous pouvez le constater le sujet de ce TP est lui aussi long. Cela ne doit pas vous effrayer. Il mélange explications complètes et manipulations pour être au maximum autosuffisant.
>
> :exclamation: Il est possible que les copiés/collés fonctionnent étrangement (caractère de fin de ligne qui disparaissent, indentation qui change). Faites-y attention !

Dans ce TP vous allez :

- Implémenter le patron de conception DAO
- Voir si votre programme fonctionne avec des tests unitaires reproductibles

## 1 Introduction

Dans ce TP nous allons mettre en place la **persistance** de nos données.

>  :thinking:Pourquoi persister nos données  ? 

Actuellement si rien n'est fait lorsque notre application s'éteint, toutes les objets qu'elle manipulait sont perdus.  Cela est du au fait que python travaille avec la *mémoire vive* de votre ordinateur (mémoire RAM pour *Random Access Memory*). C'est une mémoire très rapide mais volatile, avec une place limitée (plus limitée que la mémoire de votre disque dur). Volatile signifie que quand votre ordinateur éteint, vos barrettes de RAM (l'objet physique qui contient la mémoire) ne sont plus alimentées, et toutes les informations qu'elles contenaient sont perdues. L'autre problème provient de sa gestion par votre ordinateur. Pour faire simple, quand un programme tourne et crée des objets en RAM, lorsque ce programme s'éteint les objets en mémoire RAM deviennent inaccessibles votre ordinateur considère que la place est libre.

Il nous faut donc un moyen de persistez nos données. Pour ça il y a deux grandes solutions :

- **Sérialiser** les données pour les écrire dans un fichier, qui sera stocker sur le disque dur de la machine ou sur sur un serveur distant. On pourrait par exemple les écrire dans un fichier json

  ````json
  {
      "nom" : "Link",
      "force" : 10,
      "agilite" : 20,
      "magie" : 5,
      "defense" : 13,
      "point de vie": 55,
      "arme" : {
          "nom" : "master sword",
          "phrase_attaque" : 
      }
  }
  ````
  

Il nous suffirait ensuite de lire ce fichier pour recréer le personnage. 

- Le sauvegarder dans une base de données (SQL ou no-SQL).

Si les deux méthodes sont utilisables, il faut bien avoir conscience de leurs différences :

- La base de données fournie des outils de requêtage et administration des données. Pour le requêtage vous connaissez le langage SQL (Structured Query Language) pour les bases de données relationnelle, mais d'autres langage existent pour d'autres bases. Le SQL est un langage haut niveau pour manipuler des données. Même s'il est normalisé, tous les systèmes de gestion de bases de données (SGBD) ont leur petites particularités. L'inconvénient de l'utilisation d'une base de données et qu'il faut avoir une base de données à disposition. 
- La gestion de la persistance par sérialisation suppose de redévelopper tout un système de gestion des données, ou d'utiliser une bibliothèque python (appelé par moment API pour *application programming interface*) qui va vous aider à manipuler vos données.

Pour résumer :

- **Base de données** : propose une interface de gestion des données intégrée mais demande l'installation d'une base et son administration. Propose des outils normalisées de manipulation de données.
- **Sérialisation** : développer ses propres outils, ou utiliser des API qui les proposent.

Pour rappel voici les 4 opérations de base de manipulation de données (et leur équivalent en SQL) :

- **C**reate (Insert)

- **R**ead (Select)

- **U**pdate (Update)

- **D**elete (Delete)

  > :thinking:Souvent des élèves se demandent pourquoi l'opération de copie ne fait pas partie des opérations de base. En fait copier une donnée revient à la lire (read) et l'écrire (create). Par exemple copier une ligne en SQL s'écrit :
  >
  > ````sql
  > INSERT INTO table SELECT * FROM table where condition
  > ````

## 2 Mise en place

- Ouvrez deux terminaux vers le cluster de calcul en utilisant PuTTY. Un servira pour git, et un autre pour PyCharm. En cas de difficulté référez-vous au document sur moodle pour la marche à suivre.

- Dans le terminal pour git, retournez dans le dossier où vous avez téléchargé le code du premier TP en naviguant dans le terminal avec des `cd` puis fait un `git checkout`. Si vous avez respecté les instructions du TP1 il vous suffit de faire.

  ````shell
  cd 2A/complement_info_ensai_2020_2021
  git add .
  git commit -m "reste TP1"
  git checkout TP2_ex1
  ````

- Dans le terminal pour Pycharm, lancez Pycharm en tapant `pycharm-community` (vous pouvez utiliser l'auto completion avec la touche `Tab`)

- Ouvrez le dossier contenant le code du TP

- Dans le fichier `propreties` dans le package configuration fixez les valeurs suivantes :

  - host = "sgbd-eleves.domensai.ecole"
  - port = "5432"
  - database = "votre idep"
  - user = "votre idep"
  - password = "votre idep"

- Dans le fichier `script_bdd.sql` dans le dossier ressources vous trouverez un script sql à exécuter pour initialisez votre base. Ce script est à lancer sur votre base de postgres de l'Ensai disponible sur l'ENT ou le lien suivant  [postgresEnsai](http://sgbd-eleves.domensai.ecole/phppgadmin) (accessible uniquement depuis votre VM ou le wifi Ensai). Pour rappel votre nom d'utilisateur et votre mot de passe pour accéder au service sont tous deux votre IDEP Ensai.

- Vérifiez que l'interpréteur est bien configuré et lancez les tests du projet avec un clic droit sur le package test puis "Run Unittests in test". Normalement seuls 3 tests devraient être en erreur, tous dans la classe test_armeDAO

## 3 Data Access Objet (DAO)

###  3.1 Modélisation

Reprenons le diagramme de classe du TP précédent et limitons nous à la partie "arme" (pas les personnage et armure) et réfléchissons où mettre une méthode qui permet de persister les armes.

````mermaid
classDiagram
class AbstractEquipement {
	<<abstract>>
	+String nom
	+int id
	 }
	
class AbstractArme {
<<abstract>>
+String database_label
+String description_attaque
+int degat
+AttaqueInfo utiliser_arme(Statistique stat_pers)
+float calcul_degats(Statistique stat_pers)
}

class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}



Statistique "1"--* AbstractEquipement
AbstractEquipement <|-- AbstractArme
Epee --|> AbstractArme
Baton --|> AbstractArme
Arc --|> AbstractArme
AbstractArme <|-- Couteau
AbstractArme <|-- Lance
AbstractArme <|-- Livre

````

> :mag:  Les plus observateurs d'entre vous auront remarqué l'apparition d'un attribut `id` dans la classe `AbstractEquipement` ainsi que de `database_label` dans `AbstractArme`. Ce ne sont pas les seuls changement comparé à la semaine dernière. Ils ne changent pas le fonctionnement général du code, mais sont là pour éviter la redondance de code, et permettent des tests plus simples.

Vu que les attributs de nos armes sont similaires on ne va pas coder ça dans les classes spécifique des armes. On pourrait mettre les méthodes dans `AbstractArme`.  Ça fonctionnerait bien d'ailleurs. On aurait une classe unique avec nos méthodes pour interagir avec la base. Mais on ne va pas faire ça !

Et là vous êtes en droit de vous demander 

>  :scream: Mais pourquoi ???

Et la réponse est

> :stuck_out_tongue: Car ça n'a aucun sens !

Revenons sur la phrase : **faible couplage, forte cohésion**. Si on met toutes les méthodes de persistance de nos armes dans la classe `AbstractArme` on va avoir une classe qui :

 - :heavy_check_mark: Détermine le comportement des armes.
 - :x: Détermine comment on persiste une arme.

  Mais ça, **ce n'est pas de la responsabilité d'une arme, mais du système de persistance choisi, **ou du moins de **l'intermédiaire entre nos objets et le système de persistance** ! Je n'ai personnellement pas envie d'aller modifier ma classe `AbstractArme` uniquement car j'ai décidé de changer de système de gestion de la persistance. Je risque de modifier quelque chose que je ne devrai pas et créer des régressions (= faire apparaitre des erreurs sur un code existant) dans mon code. Or j'aimerais bien limiter les sources d'erreur.

À la place on va créer une classe qui va s'occuper uniquement de cette tâche. Et on appelle ce type de classe DAO pour **Data Access Object**. C'est une classe technique qui va faire **l'interface entre nos données stockées et notre application**. Voilà ce que cela donne en terme de diagramme de classe

````mermaid
classDiagram
class AbstractEquipement {
	<<abstract>>
	+String nom
	+int id
	 }
	
class AbstractArme {
<<abstract>>
+String database_label
+String description_attaque
+int degat
+AttaqueInfo utiliser_arme(Statistique stat_pers)
+float calculer_degats(Statistique stat_pers)
}

class Statistique {
	 +int force
	 +int agilite
	 +int magie
	 +int defense
	 +int point_de_vie
}


class ArmeDAO{
 +AbstractArme create(AbstractArme arme_to_create)
 +AbstractArme find_by_name(str nom)
 +AbstractArme find_all()
 +boolean update(AbstractArme arme_to_update)
 +boolean delete(AbstractArme arme_to_delete)
}

class PoolConnection{
 - __instance
 +connexion getConnexion()
 +bool closeConnexions()
 +SimpleConnectionPool getInstance()
 +None putBackConnexion(connection connexion)
}

AbstractArme<.. ArmeDAO: <<create>>
ArmeDAO..> PoolConnection: <<use>>

Statistique "1"--* AbstractEquipement
AbstractEquipement <|-- AbstractArme
Epee --|> AbstractArme
Baton --|> AbstractArme
Arc --|> AbstractArme
AbstractArme <|-- Couteau
AbstractArme <|-- Lance
AbstractArme <|-- Livre

````

> :scream_cat: Cela commence à faire beaucoup de classe et ce n'est qu'un début. Je ne cache pas qu'on va terminer avec pas mal de classes. Mais toutes nos classes auront une **tâche bien précise**. Cela aide à la lisibilité du code, sa maintenabilité et son débuggage. Par exemple la classe `ReservoirConnexion` sert uniquement à gérer les connexions avec la base. S'il y a un problème avec les connexion je sais le problème vient de cette classe. Et cela évite d'avoir des bout de code pour gérer les connexions partout.

### 3.2 Gestion des connexions et patern singleton

Pour nous connecter à la base de données nous allons utiliser la bibliothèque python `psycopg2`. C'est elle qui va établir la connexion avec la base, envoyer nos requêtes et nous retourner les résultats. Mais il faut faire un peu attention à la gestion des connexions. Car on pourrait se retrouver à ouvrir des centaines de connexion rapidement et dégrader les performances de notre application. C'est le travail de la classe `PoolConnection`.

La classe `PoolConnection` est une classe singleton ([singleton patern](https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception))), c'est à dire que toutes les instances de la classe `PoolConnection` pointent vers le même objet. La première fois qu'une connexion sera demandée, un *pool* (réservoir) de connexion sera initialisé pour l'application. Et à partir de là chaque fois qu'une connexion sera requise, une connexion de se *pool* sera utilisée. Comme ça, on s'assure d'utiliser un nombre constant de connexion dans notre application.

Cette classe est une solution purement technique alors n'hésitez pas à la réutiliser pour votre projet. Le code de la classe est bien documenté pour les personnes intéressées.

Si vous voulez plus d'information voici un tuto en anglais : [article de pynative](https://pynative.com/psycopg2-python-postgresql-connection-pooling/)

### 3.3 DAO et CRUD

Si vous faites attention, les méthodes de notre DAO ressemblent à celles du CRUD. C'est normal car c'est dans ces méthodes que le code SQL va être stocké, donc il nous faut les méthodes de bases. Néanmoins pour gagner du temps rien n'empêche de créer des méthodes plus complexe. Par exemple il y a deux méthodes pour lire des données :

- `find_by_id()` : qui retourne juste l'enregistrement avec l'id souhaité ;
- `find_all()` : qui va retourner toute une table.

Mais on pourrait imaginer plus de méthode si elles nous sont utiles. Ainsi la liste proposée n'est en rien absolue, elle doit être adaptée à vos besoins.

Voici la fonctionnement général d'une des méthodes de la DAO (avec un exemple de code)

````python
def create(arme):
    # Etape 1 : On récupère une connexion
    connexion = ReservoirConnexion.getConnexion()
    # Etape 2 : on crée un curseur qui va nous permettre d'exécuter la requête
    curseur = connexion.cursor()
    # Etape 3 : on crée un bloc try/except
    try:
        # Etape 4 : on exécute notre requête SQL. Les %s vont être remplacé par les valeurs passé dans la seconde partie du execute
        curseur.execute(
            "INSERT INTO arme (nom, description_attaque,degat)"
            " VALUES (%s, %s, %s) RETURNING id;"
            , (arme.nom, arme.description_attaque, arme.degat))

        # Etape 5 (optionnelle) : on récupère le résultat de la requête
        arme.id = curseur.fetchone()[0]
        # Etape 6 : on commit notre requête pour la rendre permanente.
        connexion.commit()
        except psycopg2.Error as error:
            # Etape 7 : s'il y a une erreur on fait un rollback et on annule la requête
            AbstractDao.connection.rollback()
            raise error
        finally:
            # Etape 8 : on ferme le curseur pour libérer de la mémoire coté base et on remet la connexion dans notre reservoir à connexion.
            curseur.close()
            ReservoirConnexion.putBackConnexion(connexion)
		# Etape 9 : on retourne l'objet demandé.
        return arme
````

Les requêtes que vous allez réaliser se découpent en deux catégories :

- Celles qui lisent la bases (les requêtes de type SELECT)
- Celles qui la modifient (les autres)

Dans le cas de requête de lecture il n'y a pas besoin de valider votre transaction vu que la base ne change pas d'état. Cela permet de retirer la ligne de commit et la gestion du rollback.

> :book: Rappel des cours sur les base des données. Pour assurer l'intégrité et la cohérence des données, les SGBD ne réalisent pas directement les transactions demandées sur les données. Ils les font d'abord "pour de faux" sans les valider. Et c'est seulement quand une transaction est validée (qu'elle est *commit*) que les changements deviennent permanents. Ce fonctionnement en deux étapes rend les retours en arrière (*rollback*) facile. Et comme nous n'avons pas configurer les *auto commit* il faut faire le *commit* à la main. Dans le cas d'opération de lecture, comme on ne modifie pas de données pas besoin de commit la transaction SQL

```` python
connexion = PoolConnection.getConnexion()
curseur = connexion.cursor()
try:
	curseur.execute(requete_sql)
	# du code
finally:
    curseur.close()
    PoolConnection.putBackConnexion(connexion)
return something
````

Pour les autres la structure est la suivante :

````python
connexion = PoolConnection.getConnexion()
curseur = connexion.cursor()
try:
    curseur.execute(requete_sql)
    # du code
    connexion.commit()
except psycopg2.Error as error:
    AbstractDao.connection.rollback()
    raise error
finally:
    curseur.close()
    PoolConnection.putBackConnexion(connexion)
return something
````

L'objet curseur contient un pointeur vers le résultats de votre requête. Vous avez 3 méthodes pour récupérer le résultat :

- `curseur.fetchall()` : retourne l'intégralité des résultats sous forme d'une liste de tuple. Les tuples sont les lignes récupérées. Cette méthode fonctionne très bien quand on veut tout le résultat en une fois, sauf quand on a des millions d'enregistrements car :

  - Le transfert de données sur internet va prendre du temps et bloquer notre application;
  - Notre application va devoir gérer une grande quantité de données, et elle en est peut-être incapable.

   Pour traiter ce tableau

  ````python
  records = curseur.fetchall()
  armes = [] 
  for row in records : # boucle sur les lignes du tableau
      armes.append(Arme(row[0], row[1]...)) #row[X] = la X+1 ième colonnes de la ligne row
  ````

- `curseur.fetchmany(size)`: retourne autant d'enregistrement que demandé sous forme d'une liste de tuple. Elle permet de contrôler le volume de données que l'on traite. Si vous appelez de nouveau `fetchmany(size)` sur votre curseur vous allez récupérer les lignes suivantes (vous obtenez un système de pagination). La contrepartie est que cela demande de garder le curseur ouvert. Le résultat ce traite de la même manière que précédemment ; 

- `curseur.fetchone()` : retourne uniquement un enregistrement (un tuple). Si vous appelez de nouveau  `fetchone()` sur le même curseur vous obtiendrez la ligne suivante.

Pour plus d'information : [article de pynative](https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/)

### Exercice 1 : DAO basique

Dans une première approche on va considérer que l'on manipule uniquement des armes de classe `Epee`.

- Codez les méthodes manquantes de `ArmeDao`. Respectez les structures suivantes :
  
  - Méthodes qui mettent à jour des données :
  
      ```python
      connexion = PoolConnection.getConnexion()
      curseur = connexion.cursor()
      try:
          curseur.execute(requete_sql)
          # du code
          connexion.commit()
      except psycopg2.Error as error:
          AbstractDao.connection.rollback()
          raise error
      finally:
          curseur.close()
          PoolConnection.putBackConnexion(connexion)
      return something

      ```
  
  - Méthode qui ne font que lire les données :
  
      ````python
      connexion = PoolConnection.getConnexion()
      curseur = connexion.cursor()
      try:
      	curseur.execute(requete_sql)
      	# du code
      finally:
          curseur.close()
          PoolConnection.putBackConnexion(connexion)
      return something
      ````
- Complétez les tests de la classe `TestArmeDao` pour qu'ils soit tous au vert. Pourquoi les tests actuels ne sont pas de "bons" tests ? (avec les outils actuellement à votre disposition il est difficile de faire mieux) ;
- Aller voir dans la base si tout se passe correctement.

### Exercice 2 : DAO avec des types d'armes

Notre application ne prend pas en charge que des armes de la classe `Epee`, nous allons maintenant implémenter la gestion différenciée des types d'armes

- Mettez à jour le fichier `script_bdd.sql` avec la requête de création de la table `type_arme` qui va contenir un id pour chaque type et un label ;
- Insérez une lignes pour chaque type d'arme dans la table `type_arme`. Pour les labels vous utiliserez les `database_label` des classes d'armes ;
- Mettez à jour la table `arme` pour gérer les types via une clef étrangère. Le plus simple est de supprimer la table et d'en faire une nouvelle;
- Créez une classe `TypeArmeDao` pour récupérer les id des armes. Vous créerez deux méthodes :
  - `find_id_by_label` pour retourner l'id d'un type d'arme ;
  - `find_all`pour retourner le tableau de tous les types d'arme ;
- Mettez à jours la classe `ArmeDao`pour gérer les types d'arme.

Voici quelques conseils :

- Pour les clés étrangères en postgresSQL : [tuto](https://www.postgresqltutorial.com/postgresql-foreign-key/) ;

- Vous pouvez utiliser l'attribut de classe `database_label` de chaque arme pour avoir son label en base ;

- Dans le cadre du TP limitez vous à 3 types. Dans la correction vous trouverez le code complet ;

- Pour limiter la redondance de code faite une méthode qui à partir d'un enregistrement de la table retourne l'arme instanciée avec la bonne classe. Elle vous sera utile dans les deux méthodes `find_all` et `find_by_id` ;

- Ici vous pouvez faire des `if/elif/else` pour initialisez vos objets :

  ````python
  if label == Epee.database_label:
  	arme = Epee( .... )
  elif label == Lance.database_label:
  	arme = Lance( .... )
  ````

- Seules les méthodes `create`, `find_by_id`et `find_all` ont besoin d'être modifiées ;

- Pensez à mettre à jour vos tests pour voir si votre code fonctionne.

### Exercice 3 : DAO avec les statistiques des armes

Vous allez maintenant terminer la DAO de nos armes en gérant leurs statistiques. Pour cela vous allez devoir :

- Créer une table avec les statistiques des armes
- Mettre à jours votre classe `ArmeDao` pour gérer les statistiques des armes

- Mettre à jour vos tests

Voici quelques conseils :

- Mettez à jour le fichier `script_bdd.sql` avec la requête de création de la table `statistique_objet` qui va contenir les bonus qu'apportent un objet. Votre table devra avoir une référence vers la table `arme` ;

- Pour permettre une suppression en cascade en PostgreSQL ajoutez `ON DELETE CASCADE` a votre clef étrangère. Par exemple

  ````sql
  CONSTRAINT nom_fkey FOREIGN KEY (id_equipement) REFERENCES arme(arme_id)  ON DELETE CASCADE
  ````

- Vous n'avez pas à tous refaire, seulement modifier :

  - Le code SQL de la méthode qui à partir d'une ligne instancie un objet héritant de `AbstractArme`
  - Le code SQL de la  méthode d'insertion d'une nouvelle arme. Vous ferez deux requêtes :
    - Une pour ajouter une ligne dans la table `arme` et récupérer l'id de l'arme
    - Une pour ajouter une ligne table `statistique_objet` (ou tout autre nom que vous avez donné) avec l'id récupéré
  - Le code SQL de la  méthode de mise à jour d'une arme.

- Vos testes doivent vous servir à valider votre code

## 4 Conclusion

Dans ce TP vous avez implémenté votre première DAO. C'est une classe technique qui sert à communiquer avec votre système de persistance des données. L'avantage premier de faire une classe à part est de découpler au maximum la gestion du système de persistance et le code métier de votre application. Si vous décidez d'arrêter d'utiliser une base de données relationnelle et préférez désormais une base de données *no SQL* vous allez devoir changer uniquement les classes DAO tout en exposant toujours les mêmes méthodes.

Vous trouverez les codes des corrections sur les branches suivantes :

- `TP2_ex1_correction` pour l'exercice 1
- `TP2_ex2_correction` pour l'exercice 2
- `TP2_ex3_correction` pour l'exercice 3

## Pour aller plus loin

Dans la correction j'utilise une classe que j'appelle `factory`. L'unique but de cette classe est de construire des objets à partir des paramètres données. Vous pouvez faire un parallèle avec une usine qui fabrique des objets à partir de manière première pour le compte d'une entreprise tierce (externalisation de la production). L'entreprise paie l'usine pour produire des objets car elle ne dispose pas de l'expertise nécessaire pour les produire. 

En programmation c'est la même chose. On va utiliser des intermédiaires ultra spécialisés (comme les *DAO* ou les *factories*) pour nous rendre un besoin technique spécifique car on considère que ce n'est pas à notre code métier de savoir faire cela.  Cela permet en plus une répartition du travail en fonction des spécialités de chacun et une mutualisation du code. Donc moins de code à écrire et à maintenir (une modification impactera peu de lignes de code).

Mais tout ce fonctionnement à un coût. On multiplie le nombre de classes et le code peut sembler imposant. Une comparaison souvent utilisée est l'opposition legos / playmobils. Les legos sont un système extrêmement modulaire et on peut tout faire avec. Le pire comme le meilleur. Mais cela demande du temps et souvent un plan d'assemblage pour comprendre comment les utiliser. Alors que les playmobils sont moins modulaire pour la construction mais plus rapidement utilisable. Et ne nécessitent pas de plan. Chacun à ses avantages et inconvénients et il faut souvent trouver un juste milieu entre les deux approches.

Le projet et les TP sont à but pédagogiques. Vous devez vous forcer à faire quelque chose de bien conçu et de modulaire. Peut-être pas autant que tout ce qui est proposé dans les corrections, mais vous devez vous forcer à sortir de votre zone de confort et appliquer les principes qui vous sont proposés.

Quelques liens intéressant :

- [Gestion de la mémoire en python](https://realpython.com/python-memory-management/)
- [Serialisation](https://fr.wikipedia.org/wiki/S%C3%A9rialisation)
- [DAO](https://fr.wikipedia.org/wiki/Objet_d%27acc%C3%A8s_aux_donn%C3%A9es)
- [psycopg tutorial](https://pynative.com/python-postgresql-tutorial/)