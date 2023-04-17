# Programa cálculo de valores:
#     Ao digitar valores, retorna se é maior, menor ou igual valor.

first = input('Digite um valor: ')
second = input('Digite outro valor: ')

if first < second:
    print(
        f'O valor {first} é menor que {second}'
    )
elif first == second:
    print(
        f'O valor {first} é igual a {second}'
    )
else:
    print(
        f'O valor {first} é maior que {second}'
    )
