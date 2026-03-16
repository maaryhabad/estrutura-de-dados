class Nodo():
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class Lista():

    def __init__(self):
        self.head = None
        self.contA = 200
        self.contV = 0

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        
        atual = self.head

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
            return
        
        atual = self.head

        while atual.proximo is not None and atual.proximo.cor == "A":
            atual = atual.proximo

        nodo.proximo = atual.proximo
        atual.proximo = nodo

    def inserir(self):
        cor_nodo = "y"

        while cor_nodo not in ["V", "A"]:
            cor_nodo = input("\nDigite a cor da prioridade (V/A): ").upper()
        
        if cor_nodo == "A":
            self.contA += 1
            novo_paciente = Nodo(self.contA, cor_nodo)
            print(f'\nCadastrando paciente prioritário.\nNúmero do paciente: {novo_paciente.numero}')
            self.inserirComPrioridade(novo_paciente)
        else:
            self.contV += 1
            novo_paciente = Nodo(self.contV, cor_nodo)
            print(f'\nCadastrando paciente sem prioridade.\nNúmero do paciente: {novo_paciente.numero:03}')
            self.inserirSemPrioridade(novo_paciente)

    def imprimirListaEspera(self):
        print("----- LISTA DE ESPERA -----")
        if self.head is None:
            print("A lista está vazia.")
            return
        
        atual = self.head

        while atual is not None:
            print(f"Número: {atual.numero:03} | Cor: {atual.cor}")
            atual = atual.proximo

        print("---------------------------")

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na lista de espera.")
            return
        
        paciente_atendido = self.head
        print(f"Paciente atendido: Número {paciente_atendido.numero} | Cor {paciente_atendido.cor}")
        self.head = self.head.proximo
        
def menu():
    print("\n")
    print("----     Santa Julia de la Luz    ----\n")
    print("-  Sistema de controle de prioridade -\n")
    print("|-- 1. Adicionar paciente à fila   --|\n")
    print("|-- 2. Imprimir lista de espera    --|\n")
    print("|-- 3. Atender paciente            --|\n")
    print("|-- 4. Sair                        --|\n")

    opcao = input("Digite a opção desejada: \n")

    while opcao not in ["1", "2", "3", "4"]:
        opcao = input("Opção inválida. Digite novamente: ")

    match opcao:
        case "1":
            lista.inserir()
        case "2":
            lista.imprimirListaEspera()
        case "3":
            lista.atenderPaciente()
        case "4":
            print("Saindo...")
            exit()

lista = Lista()

while True:
    menu()

