# Les échanges sur le web et l'architecture client-serveur

Ce document couvre les connaissances de bases que vous êtes sensé avoir à la fin de ce cours sur des notions de base d'internet et du web et de l'échange de données sur le web. Comme tout outil, savoir comment il fonctionne vous permettra de mieux l'utiliser et de savoir ce qui est possible et impossible avec. 

> :hourglass: La lecture du document et des différentes vidéos devrait vous prendre environ une heure et quart. C'est le temps passé l'an dernier pour couvrir les même notions en cours. Des espaces pour prendre des notes sont disponibles dans ce document si vous voulez y ajouter des informations (il vous faudra par contre l'imprimer sous forme de pdf pour conserver vos notes ce qui vous fera perdre les vidéos).
>
> Une fois ce FOAD fait vous devrez tester vos connaissances avec un QCM sur Moodle. Une note de 15/20 est attendue pour le valider, vous pouvez faire ce QCM plusieurs fois. **S'il n'est pas validé, un malus d'un point sera appliqué sur votre note du module.**

## Le web ![](web.svg)

### <img src="internet.svg" style="height:1em;" />Internet et le web ![](web.svg)

Si dans la vie de tous les jours, l'internet et le web sont souvent considérés comme des notions interchangeables, il n'en est rien, et le web et internet sont bien deux choses différentes.

> <img src="internet.svg" style="height:1em;" /> **Internet** : l'internet ou l'inter-connexion des réseaux, ou réseau des réseaux désigne l'ensemble des infrastructures physiques et protocoles logiques qui permettent l'inter-connexion des réseaux et l'échange des données sans présupposer de leur type. 
>
> ![](web.svg) **Le web** : le web est une des applications d'internet, mais elle n'est pas la seule. Le web désigne l'échange d'information décrite dans des documents, historiquement des pages HTML (**H**yper**T**ext **M**arkup **L**anguage). Mais ce n'est pas la seule application du web. Les mails avec le SMTP (**S**imple **M**essage **T**ransfer **P**rotocole, les chats IRC (**I**nternet **R**elay **C**hat), le *peer-to-peer* avec BitTorrent sont d'autres services qui utilisent internet.
>
> Pour simplifier internet désigne les infrastructure dans lesquels les données circulent alors que le web désigne les pages qui sont liées les unes aux autres par des liens hypertexte et la manière de le récupérer. Donc le web dépend internet, mais la réciproque est fausse.

<iframe src="https://www.youtube.com/embed/CX_HyY3kbZw" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%; style="text-align: center;">
            Notes internet vs web
</textarea>



### Le protocole HTTP et HTTPS <img src="3499791-certificate-https-ssl_107639.svg" style="height:1em;" />

Le web est fondamentalement lié au protocole HTTP (**H**yper**T**ext **T**ransfer **P**rotocol).

> :book: **Protocole** : un protocole informatique défini l'ensemble des règles qui vont définir des échanges. Il normalise la communication et donne un cadre à respecter pour rendre la communication possible entre une multitude d'éléments différents car ils suivent les même règles.

Le HTTP est un protocole qui fonctionne sur le principe de requête - réponse. Un client demande une ressource à un serveur (c'est la requête), et le serveur lui fournit s'il le peut (c'est la réponse).

<iframe src="https://www.youtube.com/embed/eesqK59rhGA" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

> :exclamation: Il est dit dans la vidéo que le HTTP est *connectionless* **ce n'est pas vrai**. Ce qu'il faut comprendre c'est qu'il n'y a pas de canal de communication qui s'ouvre entre les deux et que les communications sont toujours des couples de demandes - réponses. 

<iframe src="https://www.youtube.com/embed/hExRDVZHhig?start=35" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<iframe src="https://www.youtube.com/embed/dut9EnbFym0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%;">
            Note http, https
</textarea>

Pour sécuriser les échanges le HTTP a dû évoluer pour devenir le HTTPS (**H**yper**T**ext **T**ransfer **P**rotocol **S**ecure). Le principe est simple, on garde le principe du HTTP mais on chiffre les données échangé grâce à l'ajout d'une couche de sécurité (SSL pour **S**ecure **S**ockets **L**ayer,  ou TSL pour **T**ransport **L**ayer **S**ecurity). La théorie de la cryptographie est assez complexe, mais il n'y a pas besoin d'être un expert du domaine pour comprendre comment le HTTPS fonctionne et les choix de ce protocole. 

Il existe deux grands types de chiffrement :

- Le symétrique 🔐;
- Et le asymétrique 🔑🔒🗝.

Dans les deux cas le principe général consiste **à prendre un message le transformer pour le rendre impossible à comprendre pour toutes personne qui n'a pas la clef de déchiffrement** (on parle alors de *cypher*). Un message correctement crypté pourrait être affiché dans la rue sans que quiconque à part les personnes qui dispose de la clef de déchiffrement ne puisse le comprendre. Fondamentalement le cryptage consiste juste à rendre illisible un message sauf pour quelques personnes.  La clef de déchiffrement peut être un objet physique (un clef, la machine enigma), une connaissance spécifique (le décalage de caractère dans le code césar) ou une fonction mathématique (fonction cryptographique). Ce n'est donc pas un précédé informatique par nature. Mais l'informatique excelle dans ce domaine car elle permet de réaliser rapidement des calculs complexes.

#### Chiffrement symétrique 🔐

Dans le chiffrement symétrique l'émetteur du message et le récepteur dispose de la même clef qui leur permet à la fois de chiffrer et de déchiffrer les données. On pourrait croire que le problème de ce fonctionnement c'est que dans un système à $n$ machines, il faut $\frac{n(n-1)}{2}$clefs (donc un $\Theta(n^2)$ clefs). Mais en fait non, ce n'est pas un réel problème. La grande difficulté se pose sur l'échange des clefs. **En effet il faut s'assurer qu'on arrive à échanger toutes ces clefs de manière sécurisée**. Car si une clef est compromise entre deux machines, un attaquant va pouvoir lire les communications (car la clef sert à déchiffrer) et insérer ses propres messages entre elles (car la clef permet de chiffrer également). Si vous voulez mettre ce genre de communication avec des amis vous pouvez par exemple vous échanger des clefs USB avec un code qui sert à chiffrer/déchiffrer, mais imaginez le calvaire si, quand vous voulez accéder à un site sécurisé, vous deviez attendre une clef USB avec la clef de chiffrement ! (en plus l'échange postal n'est pas le plus sécurisé du monde). C'est clairement intenable et ne permet pas à des milliards d'équipement de communiquer entre eux. 

#### Chiffrement asymétrique  🔑🔒🗝

Le chiffrement asymétrique quand à lui permet de résoudre ce problème. Au lieu d'avoir une clef entre émetteur et récepteur, le récepteur dispose de deux clefs, une clef dite publique et une clef dite privée. Chacune de ces clefs a un rôle bien précis. **La clef publique permet uniquement de chiffrer un message, alors que la clef privé va le déchiffrer**. Cela permet de rendre la clef publique accessible à tous car elle ne permet que de déchiffrer des données. Ainsi l'émetteur va demander au récepteur sa clef publique, chiffrer son message et lui envoyer. Ce message peut être intercepté par tous sans risque car seul le récepteur peut le déchiffrer (théoriquement). Par contre si le récepteur veut répondre, il ne peut pas le faire de manière sécurisée. En effet s'il chiffre la réponse avec sa clef publique, l'émetteur ne pourra pas lire la réponse. Mais au moins on a un chiffrement dans un sens.

On pourrait imaginer alors qu'émetteur et récepteur aient un couple clef publique, clef privée, mais ce n'est pas la solution retenue pour le HTTPS. Avez-vous une idée pourquoi ce système ne serait pas bon ?[^1] 

[^1]: Si tous le monde possédait un couple de clefs les échanges pourraient être chiffrés et illisible par tous sauf le destinataire c'est vrai, par contre l'usurpation d'identité sera assez simple. Un attaquant pourrait très bien surveiller vos communications, et intercepter toutes les réponses que vous recevez pour les remplacer par les siennes. Comme il dispose de votre clef publique, il pourra chiffrer ses messages et vous n'aurez pas de moyen de détecter l'usurpation d'identité. Sauf si au début de la communication vous vous mettez d'accord sur un code secret avec le récepteur. Si vous avez pensez cette solution, bravo vous avez presque deviné le fonctionnement du HTTPS. L'autre problème également avec un système de clefs publique et privée généralisé sera la qualité de la sécurité des clefs sur les ordinateurs personnel. Si la sécurité des serveurs est en général assurée, celle des ordinateurs de M et Mme tout le monde ne l'est pas. Donc il faut trouver un système qui ne demande aucune manipulation aux utilisateurs, et également des clefs facilement révocables.

#### Fonctionnement du HTTPS <img src="3499791-certificate-https-ssl_107639.svg" style="height:1em;" />

La solution retenue pour le HTTPS est de faire un **échange en deux temps, d'abord asymétrique puis symétrique**. Le client (que j'appelais émetteur avant) va demander la clef publique su serveur (récepteur). Le clef publique sera contenu dans le certificat du serveur. Le certificat est en quelque sorte sa carte d'identité. Un organisme tiers de confiance (autorité de certification) valide l'identité du serveur. C'est la même chose avec une carte d'identité. Un état sert d'organisme tiers en "validant" votre identité légale. L'émetteur va aller vérifier auprès de l'autorité de certification si ce certificat est véridique (pour éviter l'usurpation d'identité de serveur).

Si l'autorité valide le certificat, le client va ensuite générer une clef secrète et l'envoyer au serveur en la chiffrant  avec la clef publique. Ce message ne peut être déchiffré que par le récepteur, donc il peut transiter tranquillement sur internet. Une fois qu'il a déchiffré la clef générée, le serveur utilise la clef pour générer la clef de session qui va servir à chiffrer les futurs échanges. Le client va lui aussi déterminer la clef de session avec la clef secrète qu'il a généré. À partir de maintenant les échanges seront chiffrés de manière symétrique entre client et serveur. 

> 🕵️‍♀️🕵️‍♂️ La clef de session à une durée de vie assez courte, donc si vous vous faites voler votre ordinateur, aucun risque de ce côté. Par contre pour vos mots de passe enregistrés dans votre navigateur c'est une autre histoire. Utilisez plutôt un gestionnaire de mot de passe comme keypass.

Rassurer vous, tout ça est fait automatiquement par votre navigateur ou les bibliothèque que vous allez utiliser. Mais il est important de comprendre ce qu'il se passe, car par moment on peut aller sur des sites où notre navigateur nous alerte sur le certificat du site (autosigné, périmé). Cela n'est pas forcément grave quand on comprend le problème. Dernière chose, un certificat est payant. Par extrêmement cher, mais pas gratuit pour autant.

> ![](aN0X3YK_460swp.webp)
>
> Par exemple utiliser un certificat autosigné consiste à dire "Moi, Rémi Pépin, confirme que je suis bien Rémi Pépin". Si vous me faite confiance, vous n'aller pas remettre ma parole en doute. Il arrive assez souvent que les entreprises génèrent des certificats autosignés pour les services en cours de développement accessible uniquement depuis leurs réseaux internes. Et les navigateurs web s'ils ne sont pas configurés correctement vont vous signaler un problème de sécurité car le serveur dit "Moi, serveurX, confirme que je suis bien serveurX". À vous de déterminer si vous faite confiance à ce serveur. Si c'est un service internet à une entreprise la réponse est en général oui, si c'est un service accessible sur le web, la réponse est généralement non.

Pour vous aider à comprendre le processus, voici un diagramme de séquence simplifié d'un échange avec le protocole HTTPS. Voyez bien que l'échange se produit en 2 temps. D'abord client et serveur se mettent d'accord sur la clef de session et ensuite elle est utilisée pour les échanges.

````mermaid
sequenceDiagram
    participant C as Client
    participant S as Serveur
    rect rgb(0, 0, 255, .1)
    participant A as Autorité certif.
    note left of C: Génération d'une <br/> clef de session
    C->>S: Connexion à une URL sécurisés
    S->>C: Certificat SSL (clef publique)
    C->>A: Verification certificat
    A->>C: Certificat valide
    note over C : génère une clef <br/> secrète
    note over  C : Encrypte la clef <br/> secrète avec <br/>  la clef publique
    C ->>S: Clef secrète encryptée
    note over C, S : Client et serveur génère la même <br/> clef de sesion avec la clef secrète
    end
    rect rgb(255, 0,0, .1)
    note left of C: Echanges chiffrée
    C->>S : Requête chiffrée avec clef de session
    S->>C : Réponse chiffrée avec clef de session
    end
````

> 🧙‍♂️ Si vous vous rappeler la second vidéo, il est dit que le HTTP est *connectionless* et je vous ai dit que c'était faux. Dans le cas présent du HTTPS c'est asse clair. S'il n'y avait pas de notion de connexion il faudrait générer une clef de session par requête :scream_cat:. Cela serait inutilement coüteux.

<textarea rows = "5" name = "description" style="width:100%;">
            Notes chiffrement
</textarea>

### URI, URL, URN et DNS :world_map:

Maintenant que vous comprenez comment les données sont échangées, il reste encore un gros mystère, comment les données sont localisées. En effet pour un ordinateur www.ensai.fr ne le renseigne pas sur la localisation de la ressource demandé. Bien que URL signifie **U**niform **R**essource **L**ocator c'est surtout une localisation essentiellement humaine, et non pas machine. Vous avez déjà dû entendre parler d'adresse IP (**I**nternet **P**rotocol). L'adresse IP est la vraie adresse de votre machine. L'URL est seulement son nom *human friendly* pour qu'on s'en souvienne facilement. Votre ordinateur va avoir besoin d'un annuaire pour faire faire le lien entre cette URL et l'IP de machine qui héberge la ressource. Ce système appelle le DNS pour **D**omain **N**ame **S**ystem. 

<iframe src="https://www.youtube.com/embed/vpYct2npKD8" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>
<iframe src="https://www.youtube.com/embed/Rck3BALhI5c?start=35" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%;">
            Notes URL, URN, URI, DNS
</textarea>

## Le modèle client serveur :computer:<img src="servers_119542.svg" style="height:1em" />

### L'architecture client-serveur​ :computer:<img src="servers_119542.svg" style="height:1em" />

Le modèle **client-serveur est l'architecture qui domine le web actuellement**. Son résumé est simple, des clients font des requêtes HTTP à des  serveurs qui y répondent. Les client fonts seulement des actions de temps en temps, alors que le serveur doit pouvoir répondre à toutes les requêtes qui lui arrive, jour et nuit. Ainsi la différence entre client et serveur n'est finalement que liée au fonctionnement du modèle, le client demande et le serveur répond. Ce qui fait que presque tout équipement informatique peut être client et serveur en fonction du contexte. Vous pouvez très bien utiliser une raspberry pie comme petit serveur de contenu web ou comment client pour récupérer des données. Ou vous pouvez héberger votre site web sur votre pc portable. Par contre dés que votre pc s'éteint votre site devient inaccessible.

<iframe src="https://www.youtube.com/embed/L5BlpPU_muY" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%;">
            Note client serveur
</textarea>

### API/web services REST et requête http en python 🐍<img src="servers_119542.svg" style="height:1em" />

Maintenant que vous avez du comprendre la notion de client-serveur, abordons la notion d'API ou de *web services*. Il est important que vous compreniez dans les grandes lignes comment ils fonctionnent car de plus en plus de données sont échangées par leur biais.

Vous pouvez vous arrêter quand la vidéo parle de nodejs. C'est une plateforme logicielle en JavaScript. Comme vous ne connaissez pas ce langage la fin de la vidéo va vous sembler compliquée (pour info le cours de visualisation des données et de technologie mobile du second semestre vont vous faire découvrir le JavaScript, et dernière chose Java et  JavaScript n'ont rien à voir)

<iframe src="https://www.youtube.com/embed/FOZtRzY5x8E?start=35" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

Voici par contre comment réaliser des requêtes HTTP/HTTPS en python


<iframe src="https://www.youtube.com/embed/qriL9Qe8pJc" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%;">
            Notes webservices
</textarea>

## Un peu de culture informatique :robot:

Terminons ce FOAD par 3 petites vidéos sur des notions que vous avez sûrement déjà entendu, à savoir:

- Proxy
- VPN
- Coockies

Ce sont des notions que l'on entend de plus de plus en plus et que vous devez comprendre, pas pour ce cours, mais pour devenir des personnes conscientes du fonctionnement d'internet et du web.

<iframe src="https://www.youtube.com/embed/i23KIs9ybDM" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>


<iframe src="https://www.youtube.com/embed/DhYeqgufYss" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<iframe src="https://www.youtube.com/embed/BTlq6WmWqMk" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<textarea rows = "5" name = "description" style="width:100%;">
            Notes diverses
</textarea>