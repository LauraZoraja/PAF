def trecina(N):
    x = 5
    for n in range(N):
        x += 1./3.
    print(x)

    for n in range(N):
        x -= 1./3.
    print(x)
    #print(round(x,100))

trecina(200)
trecina(2000)
trecina(20000)

#python vraca tocan matematicki rezultat, sto jos jednom nije po ocekivanjima, vjerojatno zbog verzije windowsa