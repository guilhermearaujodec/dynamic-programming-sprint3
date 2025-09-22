# 🧪 Projeto NOA – Sistema de Cadastro e Consulta  

Este projeto é uma simulação acadêmica para o **Projeto NOA (Núcleo de Otimização de Análise)**, utilizando **estruturas de dados e algoritmos clássicos em Python**.  
O software implementa **cadastro, consulta e manipulação de dados** de pacientes e históricos de análises, aplicando conceitos de **Fila, Pilha, Algoritmos de Busca e Ordenação**.  

---

## 📋 Funcionalidades  

- 👤 **Cadastro de Pacientes**  
- 📦 **Registro de Amostras**  
- 🗂️ **Histórico de Análises em ordem cronológica (Fila)**  
- 🔄 **Consultas recentes em ordem inversa (Pilha)**  
- 🔍 **Busca Sequencial** para encontrar pacientes  
- ⚡ **Busca Binária** para localizar rapidamente em lista ordenada  
- 📑 **Ordenação dos nomes de pacientes (QuickSort e Merge Sort)**  

---

## 🏗️ Estruturas de Dados  

### 📌 Fila (FIFO – First In, First Out)  
- Utilizada para armazenar **históricos em ordem cronológica**.  
- Estrutura lógica: o primeiro histórico inserido é o primeiro a ser removido.  
- Operações:  
  - `enqueue()` ➝ adiciona no final  
  - `dequeue()` ➝ remove do início  
- **Complexidade:**  
  - Inserção: **O(1)**  
  - Remoção: **O(1)**  

---

### 📌 Pilha (LIFO – Last In, First Out)  
- Usada para **consultas em ordem inversa**, permitindo acessar o último histórico primeiro.  
- Estrutura lógica: o último inserido é o primeiro removido.  
- Operações:  
  - `push()` ➝ adiciona no topo  
  - `pop()` ➝ remove do topo  
- **Complexidade:**  
  - Inserção: **O(1)**  
  - Remoção: **O(1)**  

---

### 🔍 Algoritmos de Busca  

1. **Busca Sequencial**  
   - Percorre elemento por elemento até encontrar.  
   - Uso: localizar paciente pelo nome sem necessidade de ordenação.  
   - **Complexidade:**  
     - Melhor caso: **O(1)**  
     - Pior caso: **O(n)**  

2. **Busca Binária**  
   - Requer lista ordenada (ordenamos os nomes com QuickSort ou Merge Sort).  
   - Divide a lista ao meio a cada iteração.  
   - **Complexidade:**  
     - Melhor caso: **O(1)**  
     - Pior caso: **O(log n)**  

---

### ⚡ Algoritmos de Ordenação  

1. **QuickSort**  
   - Estratégia **divide and conquer**.  
   - Passos:  
     1. Escolher um pivô.  
     2. Dividir elementos menores/maiores em sublistas.  
     3. Recursivamente ordenar sublistas.  
   - **Complexidade:**  
     - Melhor caso: **O(n log n)**  
     - Pior caso: **O(n²)** (quando pivô é mal escolhido)  

2. **Merge Sort**  
   - Também usa **divide and conquer**.  
   - Passos:  
     1. Dividir a lista em duas metades.  
     2. Ordenar cada metade recursivamente.  
     3. Mesclar as metades em uma única lista ordenada.  
   - **Complexidade:**  
     - Melhor caso: **O(n log n)**  
     - Pior caso: **O(n log n)** (mais estável que o QuickSort)  

---

## 🖥️ Interface no Terminal  

A interface foi construída usando apenas **recursos padrões do Python**, mas com atenção à **usabilidade e estética**.  

### Exemplos de Tela  

📌 Menu Principal  
```

============================================================
🏥 NOA - SISTEMA DE CADASTRO E CONSULTA
=======================================

1 - Cadastrar Paciente
2 - Registrar Amostra
3 - Consultar Histórico (Fila)
4 - Consultar Histórico Inverso (Pilha)
5 - Buscar Paciente (Sequencial)
6 - Buscar Paciente (Binária)
7 - Ordenar Pacientes (QuickSort)
8 - Ordenar Pacientes (Merge Sort)
0 - Sair

```

📌 Cadastro de Paciente  
```

\============================================================
👤 CADASTRAR PACIENTE
=====================

Digite o nome do paciente: João Silva
Digite o CPF: 12345678901
✅ Paciente João Silva cadastrado com sucesso!

```

📌 Busca Binária  
```

\============================================================
🔍 BUSCA BINÁRIA
================

Digite o nome do paciente: Maria
✅ Paciente encontrado: Maria (CPF: 98765432100)

```

---

## ⚙️ Estrutura de Arquivos  

```

📦 noa-sistema
┣ 📜 main.py        # Código principal
┣ 📜 README.md      # Documentação
┗ 📜 requisitos.txt # Dependências (caso necessárias)

````

---

## 🚀 Como Executar  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/guilhermearaujodec/dynamic-programming-sprint3.git
   cd noa-sistema
   ```

2. Execute o software:

   ```bash
   python main.py
   ```

---

## 🎓 Conclusão

Este projeto demonstra na prática como conceitos de **estruturas de dados e algoritmos** são aplicados no contexto de um sistema real de apoio ao trabalho laboratorial.

* ✅ Estruturas de dados (Fila, Pilha)
* ✅ Algoritmos de busca (Sequencial e Binária)
* ✅ Algoritmos de ordenação (QuickSort e Merge Sort)
* ✅ Interface clara e funcional

<h2 id="autores">Autores</h2>

<div align="center">

<ul>
  <li>Augusto Mendonça - RM: 558371</li>
  <li>Gabriel Vasquez - RM: 557056</li>
  <li>Guilherme Araujo - RM: 558926</li>
  <li>Gustavo Oliveira - RM: 559163</li>
</ul><br>

</div>
