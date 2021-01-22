import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def NacrtajTacke(naziv, x, y):
    plt.plot(x, y, color='red', marker='o')
    plt.title(naziv)

def SpojiTacke(nr1, nr2, lista_koordinata):
    x1 = lista_koordinata[nr1]
    x2 = lista_koordinata[nr2]
    x = [x1[0], x2[0]]
    y = [x1[1], x2[1]]
    plt.plot(x, y)

#lista koordinata gradova
koordinate = []
#koordinate = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]
#koordinate = [(-15.97, 5.02), (-29.39, -12.81), (-0.92, -19.91), (3.64, 14.47), (23.54, 19.58), (-16.45, 20.89)]

print("Unesite minimalnu veličinu koordinata: ")
min = int(input())
print("Unesite maksimalnu veličinu koordinata: ")
max = int(input())

x = np.arange(min,max)
y = np.arange(min,max)
fig = plt.figure()
ax = fig.add_subplot(111)
img1 = mpimg.imread('evropa.png')
imgplot = plt.imshow(img1, extent=[min, max, min, max])
plt.grid(True)
plt.title("Izađite iz prozora kada izaberete sve željene tačke i pričekajte")
plt.xlabel('$x$')
plt.ylabel('$y$')

def onclick(event):
    x, y = event.xdata, event.ydata
    global koordinate
    koordinate.append((x, y))
    return koordinate

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

#RACUNANJE RJESENJA ZA TRAVELLING SALESMAN PROBLEM
#stavljen uslov zbog izuzetka do kojeg dodje kada nema koordinata u listi
if(len(koordinate) != 0):
    #inicijalizacija fitness funkcije
    fitness = mlrose.TravellingSales(coords = koordinate)
    #definisanje optimizacijskog problema preko TSPOpt
    problem = mlrose.TSPOpt(length = len(koordinate), fitness_fn = fitness, maximize=False)
    #rjesavanje problema pomocu genetickog algoritma
    najbolje_rjesenje, najbolji_fitness = mlrose.genetic_alg(problem, mutation_prob = 0.2, max_attempts = 100, random_state = 2)

    print('Najbolje rješenje je sljedeći put gradova:', najbolje_rjesenje)
    print('(svaki broj predstavlja poziciju u listi koordinata)')
    print('Najbolji fitness za najbolje rješenje iznosi:', najbolji_fitness)
else:
    najbolje_rjesenje = []

#crtanje
fig = plt.figure()
ax = fig.add_subplot(111)
img2 = mpimg.imread('evropa.png')
brojac = 0

for cl in koordinate:
    NacrtajTacke('$Travelling Salesman Problem$', cl[0], cl[1])
    #ispis broja pored tacke
    ax.text(cl[0] + 0.1, cl[1] + 0.1, brojac, style='italic')
    brojac = brojac + 1

string = 'Najbolje rješenje je sljedeći put gradova: '
for i in range(len(najbolje_rjesenje)):
    if(i+1 < len(najbolje_rjesenje)):
        string = string + str(najbolje_rjesenje[i]) + ' -> '
        SpojiTacke(najbolje_rjesenje[i], najbolje_rjesenje[i + 1], koordinate)
    else:
        string = string + str(najbolje_rjesenje[i]) + ' -> ' + str(najbolje_rjesenje[0])
        SpojiTacke(najbolje_rjesenje[i], najbolje_rjesenje[0], koordinate)

plt.xlabel(string)
ax.axis([min, max, min, max])
#dodavanje slike
imgplot = plt.imshow(img2, extent=[min, max, min, max])
plt.grid(True)
plt.show()