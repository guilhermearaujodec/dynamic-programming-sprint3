# RELATÓRIO DE NOTAÇÃO O GRANDE DAS FUNÇÕES ESTÁ PRESENTE NO README E NO PDF QUE ACOMPANHAM O CÓDIGO

from collections import deque
import csv
import os

# ---------------------------
# Utilidades visuais
# ---------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    largura = 60
    print("\033[1;36m" + "═" * largura + "\033[0m")
    print("\033[1;37m" + texto.center(largura) + "\033[0m")
    print("\033[1;36m" + "═" * largura + "\033[0m")

def linha():
    print("\033[1;36m" + "-" * 60 + "\033[0m")

def sucesso(msg):
    print("\033[1;32m✔ " + msg + "\033[0m")

def erro(msg):
    print("\033[1;31m✘ " + msg + "\033[0m")

def aviso(msg):
    print("\033[1;33m⚠ " + msg + "\033[0m")

# ---------------------------
# Estruturas principais
# ---------------------------
pacientes = []
historicos = deque()   # fila de históricos
consultas = []         # pilha de consultas

# ---------------------------
# Funções de ordenação
# ---------------------------
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = mergesort(lista[:meio])
    direita = mergesort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

# ---------------------------
# Busca Sequencial
# ---------------------------
def busca_sequencial(nome):
    for p in pacientes:
        if p["nome"].lower() == nome.lower():
            return p
    return None

# ---------------------------
# Busca Binária
# ---------------------------
def busca_binaria(lista_ordenada, alvo):
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio].lower() == alvo.lower():
            return lista_ordenada[meio]
        elif lista_ordenada[meio].lower() < alvo.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

# ---------------------------
# Funções de consulta com busca
# ---------------------------
def consultar_por_sequencial():
    clear()
    titulo("BUSCA SEQUENCIAL")
    if not pacientes:
        aviso("Nenhum paciente cadastrado.")
        return
    nome = input("Digite o nome do paciente: ")
    resultado = busca_sequencial(nome)
    if resultado:
        sucesso(f"Paciente encontrado: {resultado['nome']} (CPF: {resultado['cpf']})")
    else:
        erro("Paciente não encontrado.")

def consultar_por_binaria():
    clear()
    titulo("BUSCA BINÁRIA")
    if not pacientes:
        aviso("Nenhum paciente cadastrado.")
        return
    nomes = quicksort([p["nome"] for p in pacientes])  # precisa estar ordenado
    nome = input("Digite o nome do paciente: ")
    resultado = busca_binaria(nomes, nome)
    if resultado:
        sucesso(f"Paciente encontrado: {resultado}")
    else:
        erro("Paciente não encontrado.")


# ---------------------------
# CRUD de Pacientes
# ---------------------------
def cadastrar_paciente():
    clear()
    titulo("CADASTRAR PACIENTE")
    id_paciente = len(pacientes) + 1
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    convenio = input("Convênio: ")
    paciente = {"id": id_paciente, "nome": nome, "cpf": cpf, "nascimento": nascimento, "convenio": convenio}
    pacientes.append(paciente)
    sucesso("Paciente cadastrado com sucesso!")

def listar_pacientes():
    clear()
    titulo("LISTA DE PACIENTES")
    if not pacientes:
        aviso("Nenhum paciente cadastrado.")
        return
    print(f"{'ID':<5} {'Nome':<20} {'CPF':<15} {'Nascimento':<12} {'Convênio'}")
    linha()
    for p in pacientes:
        print(f"{p['id']:<5} {p['nome']:<20} {p['cpf']:<15} {p['nascimento']:<12} {p['convenio']}")

def atualizar_paciente():
    listar_pacientes()
    try:
        id_p = int(input("\nDigite o ID do paciente a atualizar: "))
        for p in pacientes:
            if p["id"] == id_p:
                p["nome"] = input(f"Novo nome ({p['nome']}): ") or p["nome"]
                p["cpf"] = input(f"Novo CPF ({p['cpf']}): ") or p["cpf"]
                p["nascimento"] = input(f"Nova data ({p['nascimento']}): ") or p["nascimento"]
                p["convenio"] = input(f"Novo convênio ({p['convenio']}): ") or p["convenio"]
                sucesso("Paciente atualizado com sucesso!")
                return
        erro("Paciente não encontrado.")
    except ValueError:
        erro("Entrada inválida.")

def excluir_paciente():
    listar_pacientes()
    try:
        id_p = int(input("\nDigite o ID do paciente a excluir: "))
        for p in pacientes:
            if p["id"] == id_p:
                pacientes.remove(p)
                sucesso("Paciente excluído com sucesso!")
                return
        erro("Paciente não encontrado.")
    except ValueError:
        erro("Entrada inválida.")

# ---------------------------
# Histórico (Fila)
# ---------------------------
def registrar_historico():
    clear()
    titulo("REGISTRAR HISTÓRICO")
    if not pacientes:
        aviso("Nenhum paciente cadastrado.")
        return
    listar_pacientes()
    try:
        id_p = int(input("\nDigite o ID do paciente: "))
        paciente = next((p for p in pacientes if p["id"] == id_p), None)
        if paciente:
            descricao = input("Descrição da análise: ")
            historico = {"paciente": paciente["nome"], "descricao": descricao}
            historicos.append(historico)
            sucesso("Histórico registrado na fila!")
        else:
            erro("Paciente não encontrado.")
    except ValueError:
        erro("Entrada inválida.")

def listar_historicos():
    clear()
    titulo("HISTÓRICO DE ANÁLISES (FILA)")
    if not historicos:
        aviso("Nenhum histórico registrado.")
        return
    for i, h in enumerate(historicos, 1):
        print(f"{i}. Paciente: {h['paciente']} | Descrição: {h['descricao']}")

# ---------------------------
# Consultas (Pilha)
# ---------------------------
def consultar_paciente():
    listar_pacientes()
    try:
        id_p = int(input("\nDigite o ID do paciente para consultar: "))
        paciente = next((p for p in pacientes if p["id"] == id_p), None)
        if paciente:
            consultas.append(paciente)
            sucesso(f"Consulta registrada! Paciente {paciente['nome']}.")
        else:
            erro("Paciente não encontrado.")
    except ValueError:
        erro("Entrada inválida.")

def listar_consultas_recentes():
    clear()
    titulo("CONSULTAS RECENTES (PILHA)")
    if not consultas:
        aviso("Nenhuma consulta realizada.")
        return
    for i, p in enumerate(reversed(consultas), 1):
        print(f"{i}. {p['nome']} (CPF: {p['cpf']})")

# ---------------------------
# Relatórios
# ---------------------------
def exportar_csv():
    with open("relatorio_pacientes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nome", "CPF", "Nascimento", "Convênio"])
        for p in pacientes:
            writer.writerow([p["id"], p["nome"], p["cpf"], p["nascimento"], p["convenio"]])
    sucesso("Relatório exportado para relatorio_pacientes.csv")

def exportar_txt():
    with open("relatorio_pacientes.txt", "w", encoding="utf-8") as f:
        for p in pacientes:
            f.write(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Nascimento: {p['nascimento']} | Convênio: {p['convenio']}\n")
    sucesso("Relatório exportado para relatorio_pacientes.txt")

# ---------------------------
# Menu principal
# ---------------------------
def menu():
    while True:
        clear()
        titulo("SISTEMA DE CADASTRO - PROJETO NOA")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Atualizar Paciente")
        print("4 - Excluir Paciente")
        print("5 - Ordenar Pacientes (QuickSort)")
        print("6 - Ordenar Pacientes (MergeSort)")
        print("7 - Exportar Relatórios (CSV e TXT)")
        print("8 - Registrar Histórico (Fila)")
        print("9 - Listar Históricos (Fila)")
        print("10 - Consultar Paciente (Pilha)")
        print("11 - Consultas Recentes (Pilha)")
        print("12 - Buscar Paciente (Sequencial)")
        print("13 - Buscar Paciente (Binária)")
        print("0 - Sair")
        linha()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
            input("\nPressione ENTER para voltar...")
        elif opcao == "3":
            atualizar_paciente()
            input("\nPressione ENTER para voltar...")
        elif opcao == "4":
            excluir_paciente()
            input("\nPressione ENTER para voltar...")
        elif opcao == "5":
            nomes = [p["nome"] for p in pacientes]
            print("\nOrdenado (QuickSort):", quicksort(nomes))
            input("\nPressione ENTER para voltar...")
        elif opcao == "6":
            nomes = [p["nome"] for p in pacientes]
            print("\nOrdenado (MergeSort):", mergesort(nomes))
            input("\nPressione ENTER para voltar...")
        elif opcao == "7":
            exportar_csv()
            exportar_txt()
            input("\nPressione ENTER para voltar...")
        elif opcao == "8":
            registrar_historico()
            input("\nPressione ENTER para voltar...")
        elif opcao == "9":
            listar_historicos()
            input("\nPressione ENTER para voltar...")
        elif opcao == "10":
            consultar_paciente()
            input("\nPressione ENTER para voltar...")
        elif opcao == "11":
            listar_consultas_recentes()
            input("\nPressione ENTER para voltar...")
        elif opcao == "12":
            consultar_por_sequencial()
            input("\nPressione ENTER para voltar...")
        elif opcao == "13":
            consultar_por_binaria()
            input("\nPressione ENTER para voltar...")
        elif opcao == "0":
            clear()
            titulo("ENCERRANDO O SISTEMA...")
            break
        else:
            erro("Opção inválida!")
            input("\nPressione ENTER para voltar...")

# ---------------------------
# Execução
# ---------------------------
menu()
