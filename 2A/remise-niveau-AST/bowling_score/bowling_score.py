from tabulate import tabulate

LINE = "-----------------------------------------------"
STAR_LINE = "********************************************"
TITLE = "******    BOWLING SCORE CALCULATOR    ******"

scores_brut = []


def game():
    print(STAR_LINE)
    print(TITLE)
    print(STAR_LINE)
    print()
    frame_number = int(input("Combien de frames voulez vous faire ?"))
    for i in range(frame_number):
        frame()
        print(tabulate(zip(["Frame %s" % i for i in range(1, i + 2)], scores_brut)))
        recalcul_score()
    print("the end")


def frame():
    """Permet d'ajouter le score d'un round (deux lancés)"""
    print("Nouvelle frame !")
    score_frame = [score_lance()]
    if not score_frame[0] == 10:
        # pas strike donc besoin second lancé
        score_frame.append(score_lance(score_frame))
    scores_brut.append(score_frame)


def score_lance(score_frame=None):
    if score_frame is None:
        score_frame = []
    print(LINE)
    est_correct = False
    score = None
    while not est_correct:
        score = int(input("Veuiller entrez le score de votre lancé"))
        # On regarde si la somme des lancées dépasse 10, si oui erreur !
        temp_round_score = sum(score_frame) + score
        if not temp_round_score > 10:
            if score < 10:
                est_correct = True
            elif score == 10:
                print("Strike !")
                est_correct = True
        else:
            print(
                "Votre score pour le round est %s Ce score trop important ! Veiller saisir un score réaliste !"
                % temp_round_score)
    return score


def recalcul_score():
    """Recalcule tous les scores"""
    scores_updates = []
    for i in range(len(scores_brut)):
        if len(scores_brut[i]) == 1:
            # c'est un strike
            scores_updates.append(recalcul_strike_score(i))
        elif sum(scores_brut[i]) == 10:
            # c'est un spare
            scores_updates.append(recalcul_spare_score(i))
        else:
            scores_updates.append(sum(scores_brut[i]))
    print(scores_updates)
    print("score total %s" % sum(scores_updates))


def recalcul_strike_score(strike_round):
    score_retourne = 10
    # est ce que le score suivant existe ?
    if len(scores_brut) > strike_round + 1:
        # est ce que le score suivant est un strike ?
        if len(scores_brut[strike_round + 1]) == 1:
            # oui on ajoute 10 et on va voir le lancé suivant s'il existe
            score_retourne += 10
            if len(scores_brut) > strike_round + 2:
                score_retourne += scores_brut[strike_round + 2][0]
        else:
            score_retourne += sum(scores_brut[strike_round + 1])
    return score_retourne


def recalcul_spare_score(strike_round):
    score_retourne = 10
    # est ce que le score suivant existe ?
    if len(scores_brut) > strike_round + 1:
        score_retourne += scores_brut[strike_round + 1][0]
    return score_retourne
