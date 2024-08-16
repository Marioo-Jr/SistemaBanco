menu = """

[d] depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

deposito = 0
saque = 0

while True:
    opcao = input(menu)

    if opcao == 'd':

        deposito = input('quanto deseja depositar: ')
        deposito = float(deposito)
        if deposito > 0:
            print(f'\nvoce depositou R${deposito}')
            saldo += deposito
            print(f'\nseu saldo atual é de R${saldo}')

        else:
            print('\nvoce nao pode depositar um valor negativo')



    elif opcao == 's':
        if LIMITE_SAQUES > 0:
            LIMITE_SAQUES -= 1

            saque =  input('quanto deseja sacar: ')
            saque = float(saque)

            if saque <= 500:
                if saque >0:
                    if saque <= saldo:

                        numero_saques +=1
                        saldo -=saque
                        print(f'\nvoce sacou R$ {saque}, e seu saldo atual é de {saldo}, e voce ainda pode sacar {LIMITE_SAQUES}')
                    else:
                        print(f'\nvoce nao tem saldo suficiente para sacar R${saque}, seu saldo é de: RS {saldo}')
                else:
                    print('\n voce nao pode sacar um valor negativo')
            else:
                print('\nvoce so pode sacar R$ 500 por vez, com um limite de 3 saques por dia')
        else:
            print('\nVoce ja atingiu seu limite de saques diarios')



    elif opcao == 'e':
        if deposito > 0 or saque > 0:

            print(f'\nVoce fez um  deposito de:R${deposito} e seu saldo é de R${saldo}')

            if saque > 0:
                print(f'\nvoce sacou {saque} e seu saldo é de R${saldo}')
            else:
                print('\nvoce nao fez nenhum saque')
        else:
            print('\nvoce nao fez nenhum deposito ou saque')



    elif opcao == 'q':

        break



    else:
        print('\nOperacao invalida, por favor selecione novamente a operaçao desejada')

















