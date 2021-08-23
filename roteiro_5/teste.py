from meu_grafo import MeuGrafo
p = MeuGrafo(['J', 'E'])
p.adicionaAresta('a1', 'J', 'E')
print(p.caminho_euleriano())