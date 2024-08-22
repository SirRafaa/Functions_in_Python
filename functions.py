import random

# 1- Comparar paridade de 2 números. 

def comparar_paridade(num1, num2):
    """Verifica se dois números têm a mesma paridade e retorna um tupla indicando a paridade de cada número."""
    return num1 % 2, num2 % 2

def imprimir_resultado(paridade1, paridade2):
    """Imprime uma mensagem informativa sobre a paridade dos números."""
    if paridade1 == paridade2:
        print("Os dois números têm a mesma paridade.")
        if paridade1 == 0:
            print("Ambos são pares.")
        else:
            print("Ambos são ímpares.")
    else:
        print("Os dois números têm paridades diferentes.")
        print(f"O número {numero1} é {'par' if paridade1 == 0 else 'ímpar'}.")
        print(f"O número {numero2} é {'par' if paridade2 == 0 else 'ímpar'}.")

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))

print('')

paridade1, paridade2 = comparar_paridade(numero1, numero2)
imprimir_resultado(paridade1, paridade2)

print('')

#  2- Função ´para multiplicar dois números.
  
def multiplicar_3_numeros(num1, num2, num3):
  """Fazer a multiplicação de 3 números aleatorios de 0 a 10."""
  return  num1 * num2 * num3


numero1 = random.randint(0, 10)
numero2 = random.randint(0, 10)
numero3 = random.randint(0, 10)

print(f'Número 1: {numero1} \nNúmero 2: {numero2} \nNúmero 3: {numero3}')

resultado = multiplicar_3_numeros(numero1, numero2, numero3)
print(f'O resultado da multiiplicação é: {resultado}')

print('')


# 3- Função para descobrir o valor elevado do número

def valor_elevado(num1, elevado):
    """Descobrir o valor elevado de um número digitado pelo usuário"""
    return num1 ** elevado

num1 = int(input('Digite a Base da Potência: '))
elevado = int(input('Digite um Expoente: '))

resultado_potenciacao = valor_elevado(num1, elevado)
print(f'o Resultado da Potenciação é: {resultado_potenciacao}')

print('')

# 4- Função mensagem personalizada

def mensagem_personalizada():
  """Exibe uma mensagem personalizada com base na idade do usuário."""

  idade = int(input("Digite sua idade: "))

  if idade == 18:
    print("Parabéns! Você está completando 18 anos. Bem-vindo(a) à maioridade!")
  elif idade >= 18:
     print(f"Parabéns! Você já passou {idade - 18} anos da maioridade")
  else:
    anos_faltantes = 18 - idade
    print(f"Sua idade é {idade} anos. Obrigado por participar!")
    print(f"Faltam apenas {anos_faltantes } anos para você chegar a maioridade")

mensagem_personalizada()

print('')

# 5- Função para identificar a idade da pessoa sem o uso de datatime.

def calcular_idade_manual(ano_nascimento, mes_nascimento, dia_nascimento):
    """Calcula a idade de uma pessoa sem utilizar a biblioteca datetime."""

    ano_atual = 2024  
    mes_atual = 8   
    dia_atual = 22   

    """ É Bissexto? Para verificar se um ano é bissexto em Python, pode analisar dois casos: 
O ano é divisível por 4, mas não é divisível por 100 
O ano é divisível por 4, por 100 e também por 400. """

    bissexto = True if (ano_atual % 4 == 0 and ano_atual % 100 != 0) or ano_atual % 400 == 0 else False

    # Dicionário com o número de dias em cada mês
    dias_por_mes = {1: 31, 2: 28 + bissexto, 3: 31, 4: 30, 5: 31, 6: 30, 
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    idade = ano_atual - ano_nascimento

    if mes_nascimento > mes_atual or (mes_nascimento == mes_atual and dia_nascimento > dia_atual):
        idade -= 1

    return idade

ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

idade = calcular_idade_manual(ano, mes, dia)
print(f"A idade da pessoa é: {idade} anos")

print('')

# 6- Função para saber quem ganhou a Copa América 1999

def ganhador_copa_america99():
  """Retorna True se o Brasil venceu a Copa América de 1999, False caso contrário."""
  return True

resultado = ganhador_copa_america99()
print("O Brasil ganhou a Copa América de 1999?", resultado)