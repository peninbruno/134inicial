import csv

import pytest

from main import somar, subtrair, multiplicar, dividir

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')




def print_hi(name):

    print(f'Hi, {name}')

def somar(numero_a, numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return "nao dividas por zero"


def subtrair(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b



if __name__ == '__main__':
    print_hi('Bruno')

    # Chamar a definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'A soma: {resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(25, 8)
    print(f'A subtração: {resultado}')


def test_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def test_subtrair():
        # 1 - Prepara / Configura
        # 1.1 - Dados de Entrada / Valores do Teste
        numero_a = 15
        numero_b = 10



def test_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resultados Esperados
    resultado_esperado = 9


    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def test_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resultados Esperados
    resultado_esperado = 9


    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

# lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)

]

@pytest.mark.parametrize("numero_a, numero_b, resultado_esperado", lista_de_valores)
def test_somar(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como nossa massa de teste


    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\Users\BrunoVictorioPenin\PycharmProjects\pythonProject\vendors\csv\massa_teste_somar_positivo.csv'))

def test_somar_csv(numero_a, numero_b, resultado_esperado):
        # 1 - Configura
        # utilizamos a lista como nossa massa de teste

        # 2 - Executa
        resultado_obtido = somar(int(numero_a), int(numero_b))

        # 3 - Valida
        assert resultado_obtido == int(resultado_esperado)