def sinal(x, y, z):
    if y == '+':
        return x + z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z
    elif y == '-':
        return x - z

def main():
    conta = input('Expression: ')
    x, y, z = conta.split(' ')
    x = int(x)
    z = int(z)
    resposta = sinal(x, y, z)
    print(f'{float(resposta):.1f}')


main()
