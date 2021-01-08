import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import matplotlib.pyplot as plt

def NacrtajTacke(naziv, x, y):
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(x, y, color='red', marker='o')
    plt.title(naziv)

def SpojiTacke(nr1, nr2, lista_koordinata):
    x1 = lista_koordinata[nr1]
    x2 = lista_koordinata[nr2]
    x = [x1[0], x2[0]]
    y = [x1[1], x2[1]]
    plt.plot(x, y)

#lista koordinata gradova
koordinate = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]
#, (6, 3), (2, 2), (2, 1)
#test sa github jednog primjera: (radi ispravno)
#koordinate = [(-15.97, 5.02), (-29.39, -12.81), (-0.92, -19.91), (3.64, 14.47), (23.54, 19.58), (-16.45, 20.89)]

#inicijalizacija fitness funkcije
fitness = mlrose.TravellingSales(coords = koordinate)
#definisanje optimizacijskog problema preko TSPOpt
problem = mlrose.TSPOpt(length = len(koordinate), fitness_fn = fitness, maximize=False)
#rjesavanje problema pomocu genetickog algoritma
najbolje_rjesenje, najbolji_fitness = mlrose.genetic_alg(problem, mutation_prob = 0.2, max_attempts = 100, random_state = 2)

print('Najbolje rjesenje je sljedeci put gradova:', najbolje_rjesenje)
print('(svaki broj predstavlja poziciju u listi koordinata)')
print('Najbolji fitness za najbolje rjesenje iznosi:', najbolji_fitness)

#crtanje
fig = plt.figure()
ax = fig.add_subplot(111)
brojac = 0
for cl in koordinate:
    NacrtajTacke('$Travelling Salesman Problem$', cl[0], cl[1])
    ax.text(cl[0] + 0.1, cl[1] + 0.1, brojac, style='italic')
    brojac = brojac + 1

for i in range(len(najbolje_rjesenje)):
    if(i+1 < len(najbolje_rjesenje)):
        SpojiTacke(najbolje_rjesenje[i], najbolje_rjesenje[i + 1], koordinate)
        if(i == 0):
            ax.annotate('pocetni grad', xy = (koordinate[najbolje_rjesenje[i]][0], koordinate[najbolje_rjesenje[i]][1]),
                        xytext = (koordinate[najbolje_rjesenje[i]][0] - 1.9, koordinate[najbolje_rjesenje[i]][1] + 1),
                        arrowprops = dict(facecolor = 'red', shrink = 0.00001))
    else:
        SpojiTacke(najbolje_rjesenje[i], najbolje_rjesenje[0], koordinate)

ax.axis([0, 7, 0, 7])
#ax.axis([-45, 40, -30, 30])
plt.show()

