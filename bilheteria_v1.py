#Escreva um programa em Python que determine o preço do ingresso de um cinema 
#baseado em três fatores: o filme escolhido, a idade do cliente e se ele é estudante.

def main():
    print('-' * 75)
    print('Filmes disponíveis: \nAvatar (12 anos) - R$40,00 | Batman (16 anos) - R$45,00 ' \
    '\nHomem-Aranha (12 anos) - R$40,00 | A Empregada (16 anos) - R$ 45,00')
    print('-' * 75)

    nome_filme = input('Escolha um filme: ')
    dados = busca_filme(nome_filme)
    if dados == None:
        print('Filme não encontrado')
    else:
        preco, classificacao = dados
        idade = int(input('Qual a sua idade: '))
        if idade < classificacao:
            print('Acesso negado. Idade insuficiente para assistir o filme')
        elif idade >= classificacao:
            estudante = input(('Você possui carteirinha de estudante? ')).strip().lower()
            if estudante == 'sim':
                desconto = preco * 0.5
                print(f'Estudante possui 50% de desconto. \nO preço final é R${desconto:.2f}')
            else:
                print(f'O valor é o preço base de R${preco:.2f}')
            print('Aproveite o filme!')

def busca_filme(nome):
    nome = nome.strip().lower()

    match nome:
        case 'avatar' | 'homem-aranha' | 'homem aranha':
            return 40.00, 12
        case 'batman' | 'a empregada':
            return 45.00, 16
        case _:
            return None
        
main()