def fraction(x, y):
    fracao = round((x / y) * 100)

    if fracao <= 1:
        return 'E'
    elif fracao >= 99:
        return 'F'
    else:
        return f'{fracao}%'
def main():
    while True:
        try:
            fuel = input('Fraction: ').split('/')
            if len(fuel) != 2:
                continue

            x = int(fuel[0])
            y = int(fuel[1])


            if y == 0:
                continue
            elif x > y:
                continue
            elif x < 0 or y < 0:
                continue

            resultado = fraction(x, y)
            print(resultado)

            break

        except(ValueError, ZeroDivisionError):
            continue
main()

# n pode ter nada entre o try e o except, tudo tem questar aninhados entre eles
# o try tem que ser dentro da main, n fora, e dentro do loop para repetir a pergunta
