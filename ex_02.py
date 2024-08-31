# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci(num):

    n1, n2 = 0, 1

    if num == 0 or num == 1:
        return True

    while n2 <= num:
        if n2 == num:
            return True
        n1, n2 = n2, n1 + n2
    
    return False

input_num = int(input("Digite um número: "))

while input_num < 0:
    input_num = int(input("Digite um número positivo: "))

if(fibonacci(input_num)):
    print(f"O número {input_num} pertence a sequência.")

else:
    print(f"O número {input_num} NÃO pertence a sequência.")
  