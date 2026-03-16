class Nodo():
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def hash(self, sigla):
        if len(sigla) != 2 or not sigla.isalpha():
            raise ValueError("A sigla deve conter 2 letras.")

        sigla = sigla.upper()

        if sigla == "DF": return 7

        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, nodo):
        posicao = self.hash(nodo.sigla)
        nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = nodo

    def imprimirTabela(self):
        print("Posição | Estados")
        for i in range(10):
            atual = self.tabela[i]
            
            if atual is None:
                print("Vazia")
            else:
                print(f"{i:7} |", end=" ")
                while atual is not None:
                    print(f"{atual.sigla}", end=" -> ")
                    atual = atual.proximo
                print("None")


estados_brasil = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", 
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo", 
    "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul", 
    "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná", 
    "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", 
    "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", 
    "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"
}

minha_tabela = TabelaHash()

print("\n--- TABELA RECÉM CRIADA ---\n")
minha_tabela.imprimirTabela()

for sigla, nome in estados_brasil.items():
    novo_estado = Nodo(sigla, nome)
    minha_tabela.inserir(novo_estado)

print("\n--- TABELA COM ESTADOS ---\n")
minha_tabela.imprimirTabela()

minha_tabela.inserir(Nodo("MA", "Mariana Abad"))
print("\n--- TABELA COM ESTADO FICTÍCIO ---\n")
minha_tabela.imprimirTabela()