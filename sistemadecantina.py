j = 1
cantina = 0

print("seja bem vindo à nossa cantina, veja as opções abaixo:")

while j == 1:
    print("OPÇÃO     PRODUTO               PREÇO                ")
    print("1         Suco                  R$5,00               ")
    print("2         Salgado               R$7,00               ")
    print("3         sanduíche             R$10,00              ")
    print("4         Finalizar Compra")

    p = int(input("Qual produto você deseja comprar? "))

    if p == 1:
        cantina += 5

    elif p == 2:
        cantina += 7

    elif p == 3:
        cantina += 10

    elif p == 4:
        print("Compra finalizada com sucesso!")
        print(f"Valor da compra: R${cantina}")
        break

    else:
        print("Por favor, digite uma opção existente!")