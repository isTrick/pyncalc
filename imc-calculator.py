nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input ('Digite seu peso: '))


imc = peso / altura ** 2

if imc >= 18 and imc <= 30: {
    print(f'Parabéns {nome}, o seu IMC é de {imc:.2f}, o que está dentro do ideal!')
}

if imc < 18: {
    print(f'{nome}, seu IMC é de {imc:.2f} e está abaixo do ideal.')
}

if imc > 30: {
    print(f'{nome}, seu IMC é de {imc:.2f} e está acima do ideal.')
}