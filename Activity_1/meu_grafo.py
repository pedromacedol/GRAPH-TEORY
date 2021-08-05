from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoListaAdjacencia):
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
    