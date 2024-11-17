livres = []
av_livres = []
duree = []

nb_livres, nb_jours = [int(x) for x in input().split()]

livres = [i for i in range(nb_livres)]
av_livres = [1 for i in range(nb_livres)]
duree = [0 for i in range(nb_livres)]


for _ in range(nb_jours):
    nb_clients = int(input())
    for _ in range(nb_clients):
        nm_liv, dure = [int(x) for x in input().split()]
        if av_livres[nm_liv] == 1:
            av_livres[nm_liv] = 0
            duree[nm_liv] = dure
            print(1)
        else:
            print(0)
    for ii in range(nb_livres):
        if duree[ii] > 0:
            duree[ii] -= 1
            if duree[ii] == 0:
                av_livres[ii] = 1
        else:
            av_livres[ii] = 1
