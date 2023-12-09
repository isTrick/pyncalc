while True:
    operadores_permitidos = '+-/*'
    ã
    num_1 = input('Digite um número: ')
    operador = input(f'Qual é a operação? ({operadores_permitidos}) ')
    num_2 = input('Digite um número: ')

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except:
        print('Um ou mais numeros sao invalidos')
        continue

    if operador not in operadores_permitidos:
        print('Digite um operador válido.')
        continue

    if operador == operadores_permitidos[0]:
        resultado = num_1 + num_2
        print(f'O resulado de {num_1} {operador} {num_2} é {resultado}.')
    elif operador == operadores_permitidos[1]:
        resultado = num_1 - num_2
        print(f'O resulado de {num_1} {operador} {num_2} é {resultado}.')
    elif operador == operadores_permitidos[2]:
        resultado = num_1 / num_2
        print(f'O resulado de {num_1} {operador} {num_2} é {resultado}.')
    elif operador == operadores_permitidos[3]:
        resultado = num_1 * num_2
        print(f'O resulado de {num_1} {operador} {num_2} é {resultado}.')
    else:
        print('Houve algum erro. Tente novamente')

    sair = input('Deseja sair? [s]im [n]ão ').lower()

    if sair[0] == 's':
        print('Espero ter ajudado! "Depois que o trabalho esta concluido nao importa a ferramenta."')
        break
    elif sair[0] == 'n':
        continue
    else:
        print('Não entendi')
