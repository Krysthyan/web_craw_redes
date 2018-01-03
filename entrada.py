import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_gml("heroku.gml")
in_degrees = dict(G.in_degree())
in_values = sorted(set(in_degrees.values()))
in_hist = [list(in_degrees.values()).count(x) for x in in_values]

plt.figure()
plt.grid(True)
plt.plot(in_values, in_hist, 'ro-')
plt.legend(['Grado Entrada'])
plt.xlabel('Grado')
plt.ylabel('Numero de Nodos')
plt.title('Web Crawler, Grado de Entrada')
plt.savefig('entradaN.png')
plt.show()