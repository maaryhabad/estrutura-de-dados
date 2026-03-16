import unittest
from questao1 import Nodo, Lista

class TestListaHospital(unittest.TestCase):
    def setUp(self):
        self.lista = Lista()

    def test_inserir_primeiro_verde(self):
        novo_nodo = Nodo(1, "V")
        self.lista.inserirSemPrioridade(novo_nodo)
        # Verifica se o head aponta para o nodo correto
        self.assertEqual(self.lista.head.numero, 1)
        self.assertEqual(self.lista.head.cor, "V")

    def test_inserir_multiplos_verdes(self):
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        self.lista.inserirSemPrioridade(Nodo(2, "V"))
        # O head deve ser o 1, o próximo deve ser o 2
        self.assertEqual(self.lista.head.numero, 1)
        self.assertEqual(self.lista.head.proximo.numero, 2)
        # O último deve apontar para None (Lista Não Circular)
        self.assertIsNone(self.lista.head.proximo.proximo)

    def test_inserir_amarelo_lista_vazia(self):
        # [Exigência 4.1] Se a lista estiver vazia, head aponta para o nodo
        novo_a = Nodo(201, "A")
        self.lista.inserirComPrioridade(novo_a)
        self.assertEqual(self.lista.head.numero, 201)

    def test_inserir_amarelo_antes_de_verdes(self):
        # Cenário: Já existem Verdes, entra um Amarelo
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        self.lista.inserirComPrioridade(Nodo(201, "A"))
        
        # O Amarelo deve ser o novo head 
        self.assertEqual(self.lista.head.numero, 201)
        self.assertEqual(self.lista.head.proximo.numero, 1)

    def test_inserir_amarelo_apos_outro_amarelo(self):
        # Cenário: Amarelo (201) -> Verde (1). Insere Amarelo (202)
        self.lista.inserirComPrioridade(Nodo(201, "A"))
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        
        self.lista.inserirComPrioridade(Nodo(202, "A"))
        
        # Ordem correta: 201 -> 202 -> 1 
        self.assertEqual(self.lista.head.numero, 201)
        self.assertEqual(self.lista.head.proximo.numero, 202)
        self.assertEqual(self.lista.head.proximo.proximo.numero, 1)

    def test_prioridade_fura_fila_verde(self):
        # Cenário: Lista só com verdes [V,1] -> [V,2]
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        self.lista.inserirSemPrioridade(Nodo(2, "V"))
        
        # Inserindo Amarelo: Deve virar o primeiro da lista
        self.lista.inserirComPrioridade(Nodo(201, "A"))
        self.assertEqual(self.lista.head.numero, 201)
        self.assertEqual(self.lista.head.proximo.numero, 1)

    def test_prioridade_apos_outros_amarelos(self):
        # Cenário: [A,201] -> [V,1]
        self.lista.inserirComPrioridade(Nodo(201, "A"))
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        
        # Novo Amarelo: Deve ficar entre o 201 e o 1
        self.lista.inserirComPrioridade(Nodo(202, "A"))
        self.assertEqual(self.lista.head.numero, 201)
        self.assertEqual(self.lista.head.proximo.numero, 202)
        self.assertEqual(self.lista.head.proximo.proximo.numero, 1)

    def test_incremento_contadores(self):
        # Simula o que a função inserir faria para um Verde
        self.lista.contV += 1
        n1 = Nodo(self.lista.contV, "V")
        self.lista.inserirSemPrioridade(n1)
        
        self.assertEqual(self.lista.head.numero, 1)
        self.assertEqual(self.lista.contV, 1)

        # Simula para um Amarelo
        self.lista.contA += 1
        n2 = Nodo(self.lista.contA, "A")
        self.lista.inserirComPrioridade(n2)
        
        # O Amarelo deve virar o head por causa da prioridade
        self.assertEqual(self.lista.head.numero, 201)
        self.assertEqual(self.lista.contA, 201)

    def test_caminhamento_lista(self):
        n1 = Nodo(201, "A")
        n2 = Nodo(1, "V")
        self.lista.head = n1
        n1.proximo = n2

        nos_visitados = []
        atual = self.lista.head
        while atual is not None:
            nos_visitados.append(atual.numero)
            atual = atual.proximo
        
        self.assertEqual(nos_visitados, [201, 1])
        self.assertEqual(len(nos_visitados), 2)

    def test_lista_vazia_nao_trava(self):
        atual = self.lista.head
        count = 0
        while atual is not None:
            count += 1
            atual = atual.proximo
        self.assertEqual(count, 0)

    def test_atender_em_lista_vazia(self):
        try:
            self.lista.atenderPaciente()
            atendeu_sem_erro = True
        except Exception:
            atendeu_sem_erro = False
        self.assertTrue(atendeu_sem_erro)

    def test_atender_unico_paciente(self):
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        self.lista.atenderPaciente()
        self.assertIsNone(self.lista.head)

    def test_atender_passa_para_o_proximo(self):
        self.lista.inserirSemPrioridade(Nodo(1, "V"))
        self.lista.inserirSemPrioridade(Nodo(2, "V"))
        
        self.lista.atenderPaciente()
        
        self.assertIsNotNone(self.lista.head)
        self.assertEqual(self.lista.head.numero, 2)

    def test_integridade_dos_contadores_pos_insercao(self):
        self.lista.contA += 1
        n_a = Nodo(self.lista.contA, "A")
        self.lista.inserirComPrioridade(n_a)
        
        self.lista.contV += 1
        n_v = Nodo(self.lista.contV, "V")
        self.lista.inserirSemPrioridade(n_v)
        
        self.assertEqual(self.lista.contA, 201)
        self.assertEqual(self.lista.contV, 1)
        self.assertEqual(self.lista.head.numero, 201) 

if __name__ == '__main__':
    unittest.main()