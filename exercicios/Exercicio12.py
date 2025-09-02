n = int(input("digite um numero: "))

try:
    resultado = 10 / n
    print(resultado)

except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("ERRO: VALOR INVALIDO")
finally:
    print("erro")