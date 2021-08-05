from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoListaAdjacencia):
    def __init__(self, x):
        super().__init__(x)
        self.dfs_grafo = GrafoListaAdjacencia(self.N)
        self.dfs_visitados = []

        self.bfs_grafo = GrafoListaAdjacencia(self.N)
        self.bfs_visitados = []
        self.bfs_vertices = []
        
        self.c = 0
      
    def vertices_nao_adjacentes(self):

        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        ''' 

        dic_vertices = {}
        lista_adj = []

        for vertice in self.N:
            lista = []
            for aresta in self.A:
                if vertice == self.A[aresta].getV1():
                    lista.append(self.A[aresta].getV2())
                    lista_adj.append([vertice, self.A[aresta].getV2()])
            dic_vertices[vertice] = lista
                
        
        lista_nao_adj = []
        for vertice in self.N:
            for vertice_2 in self.N:
                if vertice != vertice_2:
                    if vertice_2 not in dic_vertices[vertice] and vertice not in dic_vertices[vertice_2]:
                        dic_vertices[vertice].append(vertice_2)
                        lista_nao_adj.append(f"{vertice}-{vertice_2}")

        return lista_nao_adj

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if self.existeVertice(V) == True:
            grau = 0
            for aresta in self.A:
                    if V == self.A[aresta].getV1() or V == self.A[aresta].getV2():
                        if V == self.A[aresta].getV1() and V == self.A[aresta].getV2():
                            grau += 2
                        else:
                            grau += 1
            return grau

        else:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo.')

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        lista = []
        lista_paralelas = []
        for vertice in self.N:
            for aresta in self.A:
                par_vertice = [vertice, self.A[aresta].getV2()]
                if vertice == self.A[aresta].getV1():
                    if lista == []:
                        lista.append(par_vertice)
                    elif par_vertice in lista or list(reversed(par_vertice)) in lista:
                        lista.append(par_vertice)
                        lista_paralelas.append(par_vertice)
                    else:
                        lista.append(par_vertice)

        if lista_paralelas != []:
            return True
        else:
            return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista_asv = []
        if self.existeVertice(V) == True:
            for asv in self.A:
                if self.A[asv].getV1() == V or self.A[asv].getV2() == V:
                    lista_asv.append(self.A[asv].getRotulo())
            return lista_asv

        else:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo.')

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.vertices_nao_adjacentes() == [] and self.ha_laco() == False:
            return True
        else:
            return False
    
    def dfs(self, V=''):

        '''
        Realiza a busca pela árvore DFS do grafo a partir do vértice indicado.
        :parametro V: O vértice a ser analisado
        :return: Uma árvore DFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore.
        :raises: raise Exception se o vértice não existe ou existe laço no grafo 
        '''

        if self.ha_laco() == False and self.verticeValido(V) == True:
            chave = False

            if len(self.N) == len(self.dfs_visitados):
                    self.c = 0
                    self.dfs_visitados = []
                    dfs_grafo = self.dfs_grafo
                    self.dfs_grafo = GrafoListaAdjacencia(self.N)
                    return dfs_grafo
            
            if V not in self.dfs_visitados:

                self.dfs_visitados.append(V)

            # PECORRENDO AS ARESTAS SOBRE O VERTICE 
            for a in self.A:
                    
                V1 = self.A[a].getV1()
                V2 = self.A[a].getV2()
                    
                if V1 == V and V2 not in self.dfs_visitados:
                    
                    self.dfs_grafo.adicionaAresta(a, V1, V2)
                    chave = True
                    self.c += 1
                    return self.dfs(self.A[a].getV2())

                elif V2 == V and V1 not in self.dfs_visitados:
                    
                    self.dfs_grafo.adicionaAresta(a, V1, V2)
                    self.c += 1
                    chave = True
                    return self.dfs(self.A[a].getV1())        

            if chave == False:
                self.c -= 1
                return self.dfs(self.dfs_visitados[self.c])
            
        else:
            raise Exception('Grafo inválido, digite um grafo conectado e/ou sem laço(s).')
    
    def bfs(self, V=''):

        '''
        Realiza a busca pela árvore BFS do grafo a partir do vértice indicado.
        :parametro V: O vértice a ser analisado
        :return: Uma árvore BFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore.
        :raises: raise Exception se o vértice não existe ou existe laço no grafo.
        '''

        if self.ha_laco() == False and self.verticeValido(V):

            chave = False

            self.bfs_visitados.append(V)

            for ar in self.arestas_sobre_vertice(V):

                V1 = self.A[ar].getV1()
                V2 = self.A[ar].getV2()

                if V1 == V and V2 not in self.bfs_visitados and V2 not in self.bfs_vertices:
                    
                    self.bfs_grafo.adicionaAresta(ar, V1, V2)
                    self.bfs_vertices.append(V2)
                    chave = True

                elif V2 == V and V1 not in self.bfs_visitados and V1 not in self.bfs_vertices:  
                    
                    self.bfs_grafo.adicionaAresta(ar, V1, V2)
                    self.bfs_vertices.append(V1)
                    chave = True


            if len(self.bfs_visitados) == len(self.N):
                bfs_grafo = self.bfs_grafo 
                self.bfs_grafo = GrafoListaAdjacencia(self.N)
                self.bfs_vertices = []
                self.bfs_visitados = []
                return(bfs_grafo)

            if chave == False:
                self.bfs_vertices.pop(0)
                return(self.bfs(self.bfs_vertices[0]))

            if V in self.bfs_vertices and chave == True:
                self.bfs_vertices.pop(0)
                return(self.bfs(self.bfs_vertices[0]))

            if V not in self.bfs_vertices and chave == True:
                return(self.bfs(self.bfs_vertices[0]))

        else:
            raise Exception('Grafo inválido, digite um grafo conectado e/ou sem laço(s).')