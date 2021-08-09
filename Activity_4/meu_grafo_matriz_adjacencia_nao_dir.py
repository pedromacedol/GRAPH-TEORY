from unittest.loader import defaultTestLoader
from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):
    def posicao_vertice(self, V):
        '''
        Provê a coluna e a linha referente ao vértice V na matriz.
        :return: a posição do vertice na lista dos vértices 
        '''
        return self.N.index(V)

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] == {} and i != j:
                    lista.append(f'{self.N[i]}-{self.N[j]}')
        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] != {} and i == j:
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
            posicao_vertice = self.posicao_vertice(V)
            grau = 0

            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] != {} and self.M[i][j] != '-':
                        if posicao_vertice == i and posicao_vertice == j:
                            grau += 2 * len(self.M[i][j])
                        elif posicao_vertice == i or posicao_vertice == j:
                            grau += 1 * len(self.M[i][j])
            return grau

        else:
            raise VerticeInvalidoException('O vértice ' + V + ' não existe no grafo.')
    
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if len(self.M[i][j]) >= 2:
                        return True
        
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if self.existeVertice(V) == True:
            posicao_vertice = self.posicao_vertice(V)
            lista = []

            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] != {} and self.M[i][j] != '-':
                        if posicao_vertice == i or posicao_vertice == j:
                            for aresta in list(self.M[i][j]):
                                lista.append(aresta)
            return lista

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


