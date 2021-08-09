import unittest
from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])


        
        # Grafos conexos
        self.g_p_conexo = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_conexo.adicionaAresta('a1', 'J', 'C')
        self.g_p_conexo.adicionaAresta('a2', 'J', 'E')
        self.g_p_conexo.adicionaAresta('a3', 'J', 'P')
        self.g_p_conexo.adicionaAresta('a4', 'J', 'M')
        self.g_p_conexo.adicionaAresta('a5', 'J', 'T')
        self.g_p_conexo.adicionaAresta('a6', 'J', 'Z')
        self.g_p_conexo.adicionaAresta('a7', 'M', 'C')
        self.g_p_conexo.adicionaAresta('a8', 'M', 'E')
        self.g_p_conexo.adicionaAresta('a9', 'M', 'P')
        self.g_p_conexo.adicionaAresta('a10', 'M', 'T')
        self.g_p_conexo.adicionaAresta('a11', 'M', 'Z')
        self.g_p_conexo.adicionaAresta('a13', 'C', 'E')
        self.g_p_conexo.adicionaAresta('a14', 'C', 'P')
        self.g_p_conexo.adicionaAresta('a15', 'C', 'T')
        self.g_p_conexo.adicionaAresta('a16', 'C', 'Z')
        self.g_p_conexo.adicionaAresta('a17', 'E', 'P')
        self.g_p_conexo.adicionaAresta('a18', 'E', 'T')
        self.g_p_conexo.adicionaAresta('a19', 'E', 'Z')

        
        self.g_cn = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_cn.adicionaAresta('a1', 'A', 'B')
        self.g_cn.adicionaAresta('a2', 'B', 'E')
        self.g_cn.adicionaAresta('a3', 'D', 'E')
        self.g_cn.adicionaAresta('a4', 'C', 'D')
        self.g_cn.adicionaAresta('a5', 'A', 'C')

        self.g_cn2 = MeuGrafo(['0','1', '2', '3', '4', '5', '6', '7'])
        self.g_cn2.adicionaAresta('a1', '1', '3')
        self.g_cn2.adicionaAresta('a2', '3', '6')
        self.g_cn2.adicionaAresta('a3', '4', '6')
        self.g_cn2.adicionaAresta('a4', '5', '4')
        self.g_cn2.adicionaAresta('a5', '4', '5')
        self.g_cn2.adicionaAresta('a6', '7', '5')
        self.g_cn2.adicionaAresta('a7', '5', '7')
        self.g_cn2.adicionaAresta('a8', '3', '7')
        self.g_cn2.adicionaAresta('a9', '0', '4')
        self.g_cn2.adicionaAresta('a10', '6', '2')
        self.g_cn2.adicionaAresta('a11', '4', '7')
        self.g_cn2.adicionaAresta('a12', '1', '5')
        self.g_cn2.adicionaAresta('a13', '2', '7')
        self.g_cn2.adicionaAresta('a14', '5', '7')
        self.g_cn2.adicionaAresta('a15', '3', '7')
        self.g_cn2.adicionaAresta('a16', '2', '0')
        self.g_cn2.adicionaAresta('a17', '6', '0')
       
        self.g_cn3 = MeuGrafo(['1', '2', '3', '4'])
        self.g_cn3.adicionaAresta('a1', '1', '2')
        self.g_cn3.adicionaAresta('a2', '2', '1')
        self.g_cn3.adicionaAresta('a3', '2', '2')
        self.g_cn3.adicionaAresta('a4', '3', '2')
        self.g_cn3.adicionaAresta('a5', '1', '3')
        self.g_cn3.adicionaAresta('a6', '3', '4')
        
        self.g_cn4= MeuGrafo(['1', '2', '3', '4', '5','6', '7'])
        self.g_cn4.adicionaAresta('a1', '1', '2')
        self.g_cn4.adicionaAresta('a2', '2', '3')
        self.g_cn4.adicionaAresta('a3', '3', '4')
        self.g_cn4.adicionaAresta('a4', '5', '1')
        self.g_cn4.adicionaAresta('a5', '1', '3')
        self.g_cn4.adicionaAresta('a6', '3', '4')
        self.g_cn4.adicionaAresta('a7', '1', '4')
        self.g_cn4.adicionaAresta('a8', '3', '4')
        self.g_cn4.adicionaAresta('a9', '2', '4')
        self.g_cn4.adicionaAresta('a10', '3', '5')
        self.g_cn4.adicionaAresta('a11', '2', '5')
        self.g_cn4.adicionaAresta('a12', '6', '7')
        self.g_cn4.adicionaAresta('a13', '7', '2')
        self.g_cn4.adicionaAresta('a14', '6', '2')

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['1', '2', '3', '4'])
        self.g_d2.adicionaAresta('a1', '1', '2')
        self.g_d2.adicionaAresta('a2', '2', '1')
        self.g_d2.adicionaAresta('a3', '2', '2')
        self.g_d2.adicionaAresta('a4', '3', '2')
        self.g_d2.adicionaAresta('a5', '1', '3')


        #Grafos de arvores DFS para teste da funcao DFS

        self.g_p_dfs_z = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_dfs_z.adicionaAresta('a9', 'T', 'Z')
        self.g_p_dfs_z.adicionaAresta('a6', 'T', 'C')
        self.g_p_dfs_z.adicionaAresta('a1', 'J', 'C')
        self.g_p_dfs_z.adicionaAresta('a2', 'C', 'E')
        self.g_p_dfs_z.adicionaAresta('a4', 'P', 'C')
        self.g_p_dfs_z.adicionaAresta('a7', 'M', 'C') 


        self.g_p_sem_paralelas_dfs_j = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas_dfs_j.adicionaAresta('a7', 'T', 'Z')

        self.g_a_dfs_nina = MeuGrafo(['Nina', 'Maria'])
        self.g_a_dfs_nina.adicionaAresta('amiga', 'Nina', 'Maria')

        #Grafos de arvores BFS para teste da funcao BFS:
        self.g_p_paralelas_bfs_j = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_paralelas_bfs_j.adicionaAresta('a1', 'J', 'C')
        self.g_p_paralelas_bfs_j.adicionaAresta('a2', 'C', 'E')
        self.g_p_paralelas_bfs_j.adicionaAresta('a4', 'P', 'C')
        self.g_p_paralelas_bfs_j.adicionaAresta('a6', 'T', 'C')
        self.g_p_paralelas_bfs_j.adicionaAresta('a7', 'M', 'C')
        self.g_p_paralelas_bfs_j.adicionaAresta('a9', 'T', 'Z')

        self.g_p_bfs_c = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_bfs_c.adicionaAresta('a1', 'J', 'C')
        self.g_p_bfs_c.adicionaAresta('a2', 'C', 'E')
        self.g_p_bfs_c.adicionaAresta('a4', 'P', 'C')
        self.g_p_bfs_c.adicionaAresta('a6', 'T', 'C')
        self.g_p_bfs_c.adicionaAresta('a7', 'M', 'C')
        self.g_p_bfs_c.adicionaAresta('a9', 'T', 'Z')


        self.g_p_sem_paralelas_bfs_e = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas_bfs_e.adicionaAresta('a7', 'T', 'Z')


        self.g_c2_bfs_nina = MeuGrafo(['Nina', 'Maria'])
        self.g_c2_bfs_nina.adicionaAresta('amiga', 'Nina', 'Maria')

        #Grafos aciclicos:
        self.g_ac = MeuGrafo(['1', '2', '3', '4'])
        self.g_ac.adicionaAresta('a1', '1', '2')
        self.g_ac.adicionaAresta('a2', '2', '3')
        self.g_ac.adicionaAresta('a3', '3', '4')

        self.g_ac2 = MeuGrafo(['1', '2', '3', '4', '5'])
        self.g_ac2.adicionaAresta('a1', '1', '2')
        self.g_ac2.adicionaAresta('a2', '2', '3')
        self.g_ac2.adicionaAresta('a3', '3', '4')
        self.g_ac2.adicionaAresta('a4', '1', '5')

        #Grafos Caminho:
        self.g_cm = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_cm.adicionaAresta('a1', 'J', 'E')
        self.g_cm.adicionaAresta('a2', 'J', 'C')
        self.g_cm.adicionaAresta('a3', 'E', 'P')
        self.g_cm.adicionaAresta('a4', 'P', 'E')
        self.g_cm.adicionaAresta('a5', 'E', 'C')
        
    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))