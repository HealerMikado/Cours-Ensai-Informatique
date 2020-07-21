# Créer une base PostgreSQL sur Amazon Web Service

## Avant propos

- Cette note part du principe que vous avez déjà un compte AWS educate
- Vous n'êtes pas obligé de faire une base sur AWS, mais certains d'entre vous veulent peut-être créer une base accessible depuis l'extérieur de l'Ensai
- Vous êtes responsable de cette base
- Vous allez devoir installer sur votre poste personnel pgadmin4 pour exécuter des requêtes SQL à la main ([lien d'installation](https://www.pgadmin.org/download/pgadmin-4-windows/))

## Créer la base

- Allez sur la page authentification d'AWS educate [Se connecter à AWS Educate](https://www.awseducate.com/signin/SiteLogin) et authentifiez vous

- Allez dans vos "Classrooms" puis connectez vous à la classroom "Python Project 2020"

- La fenêtre ci-dessous s'ouvrira, cliquez sur "Continue"

  ![](C:\Users\VEDA\Documents\Ensai-cours\2A\big data\panorama-bigdata\img\educate\Screenshot_2020-01-23 My Classrooms(1).png)

- Sur l'interface "Vocareum" cliquez sur "AWS console"

- Sur l'interface AWS cherchez le service RDS

  ![](C:\Users\VEDA\Documents\Ensai-cours\2A\complement info 2020-2021\aides\rds aws.png)

- Sur le service RDS allez sur "Bases de données" puis "Créer une base de données"

- Voici les options à utiliser :

  - **Choisir une méthode de création de bases de données** : "Standard Create (Création standard)"
  - **Configuration** : 
    - **Type de moteur** : PostgreSQL
    - **Taille d'instance DB** : Offre gratuite (ce n'est pas réellement gratuit du fait de votre compte starter, mais c'est seulement 0.024\$/h ce qui vous permet d'utiliser votre base pendant plus de 2 mois avec les 50\$ de votre compte)
    - **Identifiant d'instance DB** : projet-info-python (ou tout autre nom)
    - **Identifiant principal** : laissez la valeur par défaut
    - **Mot de passe principal** : saisissez un mot de passe "fort" (+12 caractères, avec un mélange de lettre, chiffres, majuscules, caractère spéciaux)
  - **Taille d'instance DB** : Classe à capacité extensible (inclut les classes t), db.t2.micro (1 vCPU, 1GiB RAM)
  - **Stockage** :
    - **Type de stockage** : valeur par défaut
    - **Stockage alloué** : valeur par défaut
    - **Mise à l'échelle automatique du stockage** : décochez la case
  - **Disponibilité et durabilité** : valeur par défaut
  - **Connectivité** : 
    - **Virtual Private Cloud (VPC)** : valeur par défaut
    - **Configuration de connectivité supplémentaire** : activez l'accessibilité publique de votre base, et laissez le reste pas défaut
  - **Authentification de base de données** : valeur par défaut
  - **Configuration supplémentaire** :
    - **Nom de la base de données initiale** : postgres
    - **Groupe de paramètres DB** : par défaut
    - **Sauvegarde** : désactivez les sauvegardes automatiques
    - **Analyse des performances** : désactivez l'analyse des performances
  - Puis créer votre base de données

## Se connecter à la base

Pour vous connecter via `psycopg2` avec votre code python voici les paramètres à remplir : 

- L'host de votre base est se trouve sur la page de votre base. C'est le "point de terminaison" de votre base.

   Vous pouvez y accéder en faisant : "Bases de données" dans le menu de gauche, puis cliquez sur votre base.

  ![](C:\Users\VEDA\Documents\Ensai-cours\2A\complement info 2020-2021\aides\rds host.png)

- Le port est 5432
- Le nom de la database est postgres (paramètre saisi dans les configurations supplémentaires)
- Le user est la valeur de "Identifiant principal" que vous avez saisi (par défaut admin)
- Et le mot de passe est celui que vous avez défini.