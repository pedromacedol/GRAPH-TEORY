from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
import copy

class MeuGrafo(GrafoListaAdjacencia):
    def __init__(self, x):
        super().__init__(x)
        self.dfs_grafo = GrafoListaAdjacencia()
        self.dfs_visitados = []

        self.bfs_grafo = GrafoListaAdjacencia(self.N)
        self.bfs_visitados = []
        self.bfs_vertices = []

        self.ciclo_visitados = []

        self.Chave = False
        self.c = 0

        self.nv = ''
        self.lista_N = (self.N)
        self.lista_A = []

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
        :raises: raise VerticeInvalidoException
        '''
        if self.verticeValido(V) == True:
            if self.dfs_visitados == []:
                self.grafo = copy.deepcopy(self)
                self.grafo.caminho_remover_paralelas()
        
            if V not in self.dfs_visitados:
                self.dfs_visitados.append(V)
                if V not in self.dfs_grafo.N:
                    self.dfs_grafo.adicionaVertice(V)
            
            if self.grafo.A != []:
                self.dfs_recursiva(V)

            return self.dfs_grafo
        else:
            raise VerticeInvalidoException
            
    def dfs_recursiva(self, v):
        '''
        Verifica os vertices adjacentes a v e retorna o vertice para prosseguir
        :return: funcao dfs com um vertice como parâmetro
        '''
        
        if self.grafo.arestas_sobre_vertice(v) == []:
            for n in reversed(self.dfs_grafo.N):
                if self.grafo.arestas_sobre_vertice(n) != []:
                    v = n
        
        for a in self.grafo.arestas_sobre_vertice(v):
            
            vertice_1 = self.grafo.A[a].getV1()
            vertice_2 = self.grafo.A[a].getV2()
    
            if vertice_1 == v and vertice_2 not in self.dfs_grafo.N:
               
                self.dfs_grafo.adicionaVertice(vertice_2)
                self.dfs_grafo.adicionaAresta(a, vertice_1, vertice_2)
                self.grafo.removeAresta(a)
                return self.dfs(vertice_2)
            
            elif vertice_2 == v and vertice_1 not in self.dfs_grafo.N:
                self.dfs_grafo.adicionaVertice(vertice_1)
                self.dfs_grafo.adicionaAresta(a,vertice_1, vertice_2)
                self.grafo.removeAresta(a)
                return self.dfs(vertice_1)

            else:
                self.grafo.removeAresta(a)
                return self.dfs_recursiva(v)
    
    def bfs(self, V=''):

        '''
        Realiza a busca pela árvore BFS do grafo a partir do vértice indicado.
        :parametro V: O vértice a ser analisado
        :return: Uma árvore BFS, representada por meio de um outro grafo que contém apenas as arestas que fazem parte da árvore.
        :raises: raise Exception se o vértice não existe ou existe laço no grafo.
        '''
        
        if self.conexo() == True and self.verticeValido(V):
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
                if self.bfs_vertices != []:
                    return(self.bfs(self.bfs_vertices[0]))
                else:
                    bfs_grafo = self.bfs_grafo 
                    self.bfs_grafo = GrafoListaAdjacencia(self.N)
                    return bfs_grafo 
                    
            if V in self.bfs_vertices and chave == True:
                self.bfs_vertices.pop(0)
                return(self.bfs(self.bfs_vertices[0]))
            if V not in self.bfs_vertices and chave == True:
                return(self.bfs(self.bfs_vertices[0]))

        else:
            raise Exception('Grafo inválido, digite um grafo conexo.')
    
    def ha_ciclo(self):
        '''
        Provê um valor booleano (False) que indica se não existe um ciclo ou uma lista no formato 
        [v1, a1, v2, a2, v3, a3, …, an, v1] (onde vx são vértices e ax são arestas) indicando os 
        vértices e arestas que formam o ciclo.
        :return: Valor booleano(False) ou lista
        '''
        maior_grau = 0
        V_maior_grau = ''

        for ar in self.A:
            self.lista_A.append(ar)
            
        if self.ha_laco() == True:
            for a in self.A:
                if self.A[a].getV1() == self.A[a].getV2():
                    laco = self.A[a].getV1()
                    self.lista_A.remove(a) 

        remover = []
        for N in self.lista_N:
            if self.grau_ciclo(N) == 1:
                for a in self.lista_A:
                    if N == self.A[a].getV1() or N == self.A[a].getV2():
                        self.lista_A.remove(a)
                        remover.append(N)

        if remover != []:
            for x in self.lista_N:
                if x in remover:
                    self.lista_N.remove(x)
       
        for n in self.lista_N:
            if maior_grau == '':
                maior_grau = self.grau_ciclo(n)
                V_maior_grau = n
            else:
                if self.grau_ciclo(n) > maior_grau and maior_grau != self.grau_ciclo(n):
                    maior_grau = self.grau_ciclo(n)
                    V_maior_grau = n

        x = ""
        y = ""
        c = 0
        r = V_maior_grau
        while self.nv != r:
            a = self.lista_A[c]
            va = self.verificar_arestas(r, self.nv)
            if self.nv != '' and va not in self.ciclo_visitados:
                if a != va and va != None:
                    a = va
                    c = 0
            x = self.A[a].getV1()
            y = self.A[a].getV2()
            if self.ciclo_visitados == [] and x == r:
                self.ciclo_visitados.append(x)
                self.ciclo_visitados.append(a)
                self.ciclo_visitados.append(y)
                self.nv = y
                self.lista_A.remove(a)
                c = 0

            elif self.ciclo_visitados == [] and y == r:
                self.ciclo_visitados.append(y)
                self.ciclo_visitados.append(a)
                self.ciclo_visitados.append(x)
                self.nv = x
                self.lista_A.remove(a)
                c = 0 

            elif x in self.ciclo_visitados and y == r or x == r and y in self.ciclo_visitados:
                self.ciclo_visitados.append(a)
                if x == r:
                    self.ciclo_visitados.append(x)
                    return self.ciclo_visitados
                else:
                    self.ciclo_visitados.append(y)
                    return self.ciclo_visitados
            
            elif x == self.nv and y not in self.ciclo_visitados:
                self.ciclo_visitados.append(a)
                self.ciclo_visitados.append(y)
                self.nv = y
                self.lista_A.remove(a)
                c = 0
               
            elif y == self.nv and x not in self.ciclo_visitados:
                self.ciclo_visitados.append(a)                    
                self.ciclo_visitados.append(x)
                self.nv = x
                self.lista_A.remove(a)
                c = 0
        
            else:
                c += 1
                if c == len(self.lista_A):
                    self.nv = r
        else:
            return False

    def grau_ciclo(self, vc):   
        '''
        Verifica  o grau do vertice no grafo_ciclo.
        :return: Um valor inteiro indicando o grau do vertice.
        '''     
        c = 0
        V = vc
        for v in self.lista_A:
            if V == self.A[v].getV1() or V == self.A[v].getV2():
                c += 1
        return c

    def conexo(self):
        '''
        Verifica se o grafo é ou não conexo
        :return: Um valor booleano que indica se o grafo é conexo.
        '''
        if len(self.dfs(self.N[0]).N) == len(self.N):
            return True
        else:
            return False
    
    def caminho(self, n):
        '''
        Pecorre o grafo e retonar um caminho de tamanho 'n' em lista no formato [v1, a1, v2, a2, v3, a3, ...] ou
        um valor booleano false caso o caminho não exista.
        :parametro n: Valor inteiro indicando o tamanho do caminho
        :return: Uma lista no formato [v1, a1, v2, a2, v3, a3, ...] onde vx são vértices e ax são arestas ou False.
        '''
        grafo_caminho = self.caminho_remover_paralelas()
        caminho = []
        aresta_visitadas = []
        vertice = ''
        for i in range(n):
            for aresta in grafo_caminho.A:
                vertice_1 = grafo_caminho.A[aresta].getV1()
                vertice_2 = grafo_caminho.A[aresta].getV2()
                if aresta_visitadas == []:
                    aresta_visitadas.append(aresta)
                    caminho.append(vertice_1)
                    caminho.append(aresta)
                    caminho.append(vertice_2)
                    vertice = vertice_2
                    break

                elif aresta not in aresta_visitadas:
                    if vertice_1 == vertice:
                        if vertice_2 == caminho[0]:
                            caminho.append(aresta)
                            caminho.append(vertice_2)
                            vertice = vertice_2
                            aresta_visitadas.append(aresta)
                            

                        elif grafo_caminho.grau(vertice_2) > 1 and vertice_2 not in caminho :
                            caminho.append(aresta)
                            caminho.append(vertice_2)
                            vertice = vertice_2
                            aresta_visitadas.append(aresta)
                            break


                    elif vertice_2 == vertice:

                        if vertice_1 == caminho[0]:
                            caminho.append(aresta)
                            caminho.append(vertice_1)
                            vertice = vertice_1
                            aresta_visitadas.append(aresta)
                            break

                        elif grafo_caminho.grau(vertice_1) > 1 and vertice_1 not in caminho:
                            caminho.append(aresta)
                            caminho.append(vertice_1)
                            vertice = vertice_1
                            aresta_visitadas.append(aresta)
                            break               
                        
        if len(aresta_visitadas) == n:
            return caminho

        else:
            return False

    def caminho_remover_paralelas(self):
        '''
        Pecorre o grafo e retira as arestas paralelas existentes.
        :return: O grafo sem arestas paralelas.
        '''
        grafo_novo = self
        if grafo_novo.ha_paralelas()== True:
            lista_paralelas = []
            lista = []
            for vertice in self.N:
                for aresta in self.A:
                    par_vertice = [vertice, self.A[aresta].getV2()]
                    if vertice == self.A[aresta].getV1():
                        if lista == []:
                            lista.append(par_vertice)
                        elif par_vertice in lista or list(reversed(par_vertice)) in lista:
                            lista.append(par_vertice)
                            lista_paralelas.append(aresta)
                        else:
                            lista.append(par_vertice)

            for aresta_paralela in lista_paralelas:
                grafo_novo.removeAresta(aresta_paralela)

        return grafo_novo     

    def verificar_arestas(self, v0, v):
        '''
        Verifica se existe uma aresta adjacente aos vertices v0 e v.
        :return: A aresta adjacente a v0 e v, se houver.
        '''

        lv = []
        lv0 = []

        for asv in self.lista_A:
            if self.A[asv].getV1() == v or self.A[asv].getV2() == v:
                lv.append(self.A[asv].getRotulo())

        for asv in self.A:
            if self.A[asv].getV1() == v0 or self.A[asv].getV2() == v0:
                lv0.append(self.A[asv].getRotulo())

        for a in lv:
            if a in lv0:
                print(a, v, lv , v0, lv0)
                return a
