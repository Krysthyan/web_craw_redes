import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_gml("heroku.gml")
out_degrees = dict(G.out_degree())
out_values = sorted(set(out_degrees.values()))
out_hist = [list(out_degrees.values()).count(x) for x in out_values]

plt.figure()
plt.grid(True)
plt.loglog(out_values, out_hist, 'bv-')
plt.legend(['Grado Salida'])
plt.xlabel('Grado')
plt.ylabel('Numero de Nodos')
plt.title('Web Crawler, Grado de Salida')
plt.savefig('salidaL.png')
plt.show()