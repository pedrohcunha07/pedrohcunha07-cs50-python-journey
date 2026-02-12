def main():
    tempo = str(input('What time is it? '))
    convertido = convert(tempo)

    if 7.0 <= convertido <= 8.0:
        print('breakfast time')
    elif 12.0 <= convertido <= 13.0:
        print('lunch time')
    elif 18.0 <= convertido <= 19.0:
        print('dinner time')


def convert(time):
    if ' ' in time:
        #separa o espaço que tem entre a hora e o am/pm
        horario, ampm = time.split(' ')

        #mesma coisa do horário c=do formato 24 horas
        horas, minutos = horario.split(':')
        horas = float(horas)
        minutos = float(minutos)

        #condicional, se horas for igual a 12 am (meia noite) é igual a 0 (0.00)
        if ampm == 'a.m.' and horas == 12:
            horas = 0
        #condicional, se horas for igual a 12 pm (meio dia), soma mais 12 para virar \n
        #o relógio do 24h e funcionaar no formato 12h
        elif ampm == 'p.m.' and horas != 12:
            horas = horas + 12

    #formato 24 horas
    else:
        horas, minutos = time.split(':')

        horas = float(horas)
        minutos = float(minutos)
    resultado = horas + (minutos/60)
    return resultado


if __name__ == '__main__':
    main()
