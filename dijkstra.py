sommets=("A","B","C","D","E","F","G","H","I","J")
poids=[["A","B",85],["A","C",217],["A","E",173],
        ["B","A",85],["B","F",80],
        ["C","A",217],["C","G",186],["C","H",103],
        ["D","H",183],
        ["E","A",173],["E","J",502],
        ["F","B",80],["F","I",250],
        ["G","C",186],
        ["H","C",103],["H","D",183],["H","J",167],
        ["I","F",250],["I","J",84],
        ["J","E",502],["J","H",167],["J","I",84]]
distances=[float("inf")]*len(sommets)
depart,arrivee=input(),input()

predecesseur=[""]*len(sommets)
distances[sommets.index(depart)]=0

def trouve_min(Q):
    mini=float("inf")
    sommet=-1
    for s in Q:
       if distances[sommets.index(s)]<mini:
           mini=distances[sommets.index(s)]
           sommet=s
    return sommet

def maj_distances(s1,s2):
    for arete in poids:
        if arete[0]==s1 and arete[1]==s2:
            poidsArete=arete[2]
            break
    if distances[sommets.index(s2)]>distances[sommets.index(s1)]+poidsArete:
           distances[sommets.index(s2)]=distances[sommets.index(s1)]+poidsArete
           predecesseur[sommets.index(s2)]=s1

Q=list(sommets)
while Q!=[]:
    s1=trouve_min(Q)
    Q.remove(s1)
    for arete in poids:
        if arete[0]==s1:
            maj_distances(s1,arete[1])

listeEtapes=[]
s=arrivee
while s!=depart:
    listeEtapes.append(s)
    s=predecesseur[sommets.index(s)]
listeEtapes.append(depart)
listeEtapes.reverse()
print(listeEtapes)
