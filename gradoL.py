import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_gml("heroku.gml")
degrees = dict(G.degree())
values = sorted(set(degrees.values()))
hist = [list(degrees.values()).count(x) for x in values]

plt.figure()
plt.grid(True)
plt.loglog(values, hist, 'g.-')
plt.legend(['Grado'])
plt.xlabel('Grado')
plt.ylabel('Numero de Nodos')
plt.title('Web Crawler, Grado')
plt.savefig('gradoL.png')
plt.show()