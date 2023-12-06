nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input ('Digite seu peso: '))

imc = peso / altura ** 2

if 18 <= imc <= 30:
    print(f'Parabéns {nome}, o seu IMC é de {imc:.2f}, o que está dentro do ideal!')
else:
    print(f'{nome}, seu IMC é de {imc:.2f} e está fora ideal.')
