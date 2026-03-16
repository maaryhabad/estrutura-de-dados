import unittest
from questao2_hash.questao2 import Nodo, TabelaHash

class TestListaEstados(unittest.TestCase):
    def setUp(self):
        self.tabela = TabelaHash()

    def test_exigencia_df_na_posicao_7(self):
        # [EC 2.1] Verifica se DF cai obrigatoriamente na posição 7
        posicao = self.tabela.hash("DF")
        self.assertEqual(posicao, 7)

    def test_calculo_hash_comum(self):
        # Teste manual: PR -> P(80) + R(82) = 162. 162 % 10 = 2
        self.assertEqual(self.tabela.hash("PR"), 2)
        # Teste manual: SC -> S(83) + C(67) = 150. 150 % 10 = 0
        self.assertEqual(self.tabela.hash("SC"), 0)

    def test_validacao_sigla_invalida(self):
        # Testa se a função recusa números ou siglas com tamanho errado
        with self.assertRaises(ValueError):
            self.tabela.hash("P1")
        with self.assertRaises(ValueError):
            self.tabela.hash("PRR")
        with self.assertRaises(ValueError):
            self.tabela.hash("A")

    def test_insercao_no_inicio_colisao(self):
        # [EC 3.2] Verifica se o novo nodo entra no INÍCIO da lista daquela posição
        # PR e MA caem na posição 2
        nodo1 = Nodo("PR", "Paraná")
        nodo2 = Nodo("MA", "Maranhão")
        
        self.tabela.inserir(nodo1)
        self.tabela.inserir(nodo2)
        
        # O head da posição 2 deve ser o último inserido (MA)
        self.assertEqual(self.tabela.tabela[2].sigla, "MA")
        # O próximo de MA deve ser o PR
        self.assertEqual(self.tabela.tabela[2].proximo.sigla, "PR")

    def test_estado_ficticio_mariana_abad(self):
        # Testando seu estado fictício: MA -> M(77) + A(65) = 142. % 10 = 2
        # Note que ele vai colidir com PR (2) e MA (2)
        sigla_ficticia = "MA" 
        posicao = self.tabela.hash(sigla_ficticia)
        self.assertEqual(posicao, 2)

if __name__ == '__main__':
    unittest.main()