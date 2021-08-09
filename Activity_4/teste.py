from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

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

print(grafo_teste.vertices_nao_adjacentes())
print(grafo_teste.ha_laco())
print(grafo_teste.ha_paralelas())
print(grafo_teste.arestas_sobre_vertice("C"))
print(grafo_teste.eh_completo())
print(grafo_teste.grau('P'))