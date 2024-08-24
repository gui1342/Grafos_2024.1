import math
infinito = math.inf

class No:
  def __init__(self, nome):
    self.nome = nome
    self.distancia = infinito
    self.nos_adjacentes = []

  def setDistancia(self, distancia):
    self.distancia = distancia

  def getDistancia(self):
    return self.distancia

  def adicionarAdjacente(self, no, peso):
    self.nos_adjacentes.append((no, peso))

class Grafo:
  def __init__(self, lista_nos, arestas):
    self.nos = {nome: No(nome) for nome in lista_nos}
    self._adicionar_arestas(arestas)

  def getNo(self, nome_no):
    return self.nos.get(nome_no)

  def _adicionar_arestas(self, arestas):
        for origem, destino, peso in arestas:
            no_origem = self.nos[origem]
            no_destino = self.nos[destino]
            no_origem.adicionarAdjacente(no_destino, peso)


def AlgoritmoDijkstra(grafo, nome_no_inicial):
  nao_visitados = list(grafo.nos.values())#adicionando todos os nós, a lista de nós não visitados
  no_inicial = grafo.getNo(nome_no_inicial)
  no_inicial.setDistancia(0)#nó inicial deve ter distancia 0
  menor_distancia = infinito#inicialmente a menor distancia deve ser infinito
  antecessores = {}#dicionario de nós antecessores, necessário para formar o caminho final(menor caminho)

  while(nao_visitados):
    no_atual = min(nao_visitados, key=lambda no: no.distancia)#escolhe o nó de acordo com o nó de menor distancia atualmente
    nao_visitados.remove(no_atual)#remove o nó escolhido na rodada da lista de nós não visitados
    for no_adjacente, peso in no_atual.nos_adjacentes:#percorre os nós adjacentes ao nó atual
      distancia = no_atual.getDistancia() + peso#calcula a distância do nó atual até o nó adjacente
      if distancia < no_adjacente.getDistancia():#se a distância calculada for menor do que a distância atual até o nó adjacente
        no_adjacente.setDistancia(distancia)#atualiza a distância até o nó adjacente
        antecessores[no_adjacente.nome] = no_atual.nome#atualiza o nó antecessor do nó adjacente

  #Montando o caminho do nó inicial até cada um dos outros nós
  distancias = {no.nome: no.getDistancia() for no in grafo.nos.values()}
  caminhos = {}

  for nome_no, no in grafo.nos.items():#percorre o dicionário de nós.
      caminho = []
      atual = nome_no
      while atual in antecessores:
          caminho.insert(0, atual)
          atual = antecessores[atual]
      caminho.insert(0, nome_no_inicial)
      caminhos[nome_no] = caminho

  #Exibindo os resultados
  for nome_no, distancia in distancias.items():
    if distancias[nome_no] == infinito:#não exibe os caminhos que nao existem (entre o nó inicial e o de destino, cuja distancia é inf)
      continue
    print(f"Menor distância de {no_inicial.nome} até {nome_no}: {distancia}")
    print(f"Caminho: {' -> '.join(caminhos[nome_no])}")

lista_nos = ['0', '1', '2', '3', '4']
arestas = [('0', '1', 4), ('0', '2', 1), ('2', '1', 2), ('1', '3', 1), ('2', '3', 5), ('3', '4', 3)]#(nó de origem, nó de destino, peso da aresta)
grafo_teste = Grafo(lista_nos, arestas)
AlgoritmoDijkstra(grafo_teste, "0")#(grafo, nó inicial)
