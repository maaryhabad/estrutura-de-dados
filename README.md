# Estruturas de Dados: Fila Hospitalar e Tabela Hash de Estados
Este repositório contém as soluções desenvolvidas para a disciplina de Estrutura de Dados. O projeto foca na implementação prática de listas encadeadas, filas com prioridade e tabelas hash, utilizando Python.

## 🚀 O Projeto
O projeto é dividido em duas frentes principais:

### 1. Gestão de Fila Hospitalar (questao1_hospital)

Simulação de um sistema de triagem hospitalar onde a prioridade de atendimento é definida por cores (Amarelo > Verde).

**Estrutura:** Lista Encadeada Simples.

**Destaque Técnico:** Implementação de lógica de inserção com prioridade, onde pacientes com a cor "A" são posicionados à frente dos pacientes "V", respeitando a ordem de chegada dentro de cada grupo.

### 2. Tabela Hash de Estados Brasileiros (questao2_hash)

Implementação de uma Tabela Hash com 10 posições para armazenamento de estados.

**Estrutura:** Tabela Hash com encadeamento externo (cada posição da tabela é uma Lista Encadeada).

**Função Hash:** Baseada no cálculo da soma dos valores ASCII da sigla do estado com tratamento especial para o Distrito Federal (DF).

**Tratamento de Colisões:** Inserção no início da lista encadeada para otimização de performance.

## 🧪 Qualidade e Testes (QA)
Um diferencial deste projeto é a aplicação de Testes Unitários utilizando a biblioteca unittest.

O objetivo foi garantir que:

- A prioridade da fila hospitalar nunca seja violada.
- A função hash distribua os estados corretamente nas posições (gavetas) planejadas.
- O tratamento de colisões ocorra sem perda de dados.

Para rodar os testes, utilize os comandos:

```bash
python3 -m unittest questao1_hospital/tests_questao1.py
python3 -m unittest questao2_hash/tests_questao2.py
```

