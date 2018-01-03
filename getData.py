from pymongo import MongoClient
import networkx as nx


if __name__ == '__main__':

    lista_nodos = []
    client = MongoClient('mongodb://user:password@ds151279.mlab.com:51279/ucuenca')
    db = client.ucuenca
    print('conectado')
    for nodo in db.heroku.find():
        lista_nodos.append((nodo['input'], nodo['output']))
    print('info obtendida')
    grafo = nx.DiGraph()
    grafo.add_edges_from(lista_nodos)

    nx.write_gml(grafo, 'heroku.gml')