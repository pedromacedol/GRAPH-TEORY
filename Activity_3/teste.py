from meu_grafo import MeuGrafo

grafo_teste = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
grafo_teste.adicionaAresta('a1', 'J', 'C')
grafo_teste.adicionaAresta('a2', 'C', 'E')
grafo_teste.adicionaAresta('a3', 'C', 'E')
grafo_teste.adicionaAresta('a4', 'P', 'C')
grafo_teste.adicionaAresta('a5', 'P', 'C')
grafo_teste.adicionaAresta('a6', 'T', 'C')
grafo_teste.adicionaAresta('a7', 'M', 'C')
grafo_teste.adicionaAresta('a8', 'M', 'T')
grafo_teste.adicionaAresta('a9', 'T', 'Z')
print(grafo_teste.caminho(7))
print(grafo_teste.caminho(3))