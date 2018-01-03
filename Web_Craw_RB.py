import re
import requests
from bs4 import BeautifulSoup
import networkx as nx

class RedesB():
    def __init__(self, url, limits_nodes):
        self.grafo = 0
        self.url = url
        self.limits_nodes = limits_nodes
        self.list_urls = dict()
        self.used_urls = []

    def get_links(self, new_url):
        try:
            page = requests.get(new_url, timeout=1)

            if len(page.content) < 500000:
                soup = BeautifulSoup(page.text, 'html.parser')
                self.list_urls[new_url] = set()

                for link in soup.find_all('a', href=True):
                    link_new = re.match('/[a-z]...+', link['href'])
                    if link_new is not None:
                        link_new = link_new.string
                        if link_new[len(link_new) - 1] == '/':
                            self.list_urls[new_url].add(new_url + link_new[:len(link_new) - 1])
                        else:
                            self.list_urls[new_url].add(new_url + link_new)

                    link_new = re.match('http', link['href'])
                    if link_new is not None:
                        link_new = link_new.string
                        if link_new[len(link_new) - 1] == '/':
                            self.list_urls[new_url].add(link_new[:len(link_new) - 1])
                        else:
                            self.list_urls[new_url].add(link_new)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        except requests.Timeout:
            print('Se ha pasado del tiemmpo limite... siguiente perra :v')

        except requests.HTTPError:
            print('Se ha pasado del tiemmpo limite... siguiente perra :v')

    def run(self, db):
        print(self.grafo, self.limits_nodes)
        self.get_links(self.url)

        while self.grafo <= self.limits_nodes and len(self.list_urls) > 0:
            print(self.grafo, self.limits_nodes)

            for save_url in self.list_urls[self.url]:

                db.cnn.insert({"input": self.url, "output": save_url})
                self.grafo += 1
                if self.url not in self.used_urls and save_url not in self.list_urls.keys():
                    self.get_links(save_url)
                    print(self.grafo, self.url, save_url)
                if self.grafo >= self.limits_nodes:
                    break

            self.used_urls.append(self.url)
            del self.list_urls[self.url]
            self.url = list(self.list_urls.keys())[0]

    def save_graph(self):
        nx.write_gml(self.grafo, self.file_name + '.gml')
