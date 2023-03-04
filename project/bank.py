i = " Welcome System Bank Paco "
menu = (f"""
 {i.center(61, "#")}

    [d] = Deposito
    [s] = Saque
    [e] = Extrato
    [q] = Quit or Exit

    Selecione a opção desejada : 
""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 4
saque = 1

while True:

    opcao = input(menu)


    if opcao == 'd':
        valor = int(input("Qual valor deseja depositar em sua conta :  "))
        saldo += valor
        print(f'Saldo atual com o deposito efetuado : R$ : {float(saldo)}')
        extrato += ( f"Depósito:  R$ {str(float(valor))}\n")
    elif opcao == "s":
        if saque < numero_saques:
            valor = int(input("Qual valor deseja sacar em sua conta :  "))
            if valor > saldo:
                print(f"Seu saldo não possui esta quantidade solicitada, consulta o saldo em extrato")
                if valor > limite:
                        print(f"Limite de saque é de R$ 500,00 e o senhor tentou sacar R$:{valor},00")
                else:
                        pass
                    
            else:
                print(f"Saque efetuada com sucesso no valor de {valor}, consulte em 'extrato' seu saldo atual.")
                extrato += ( f"Saque:  R$ {str(float(valor))}\n")
                saldo -= valor
                saque += 1
        else:
             print("Voce exceu o limite de saque diario, veja o extrato!")
             
    elif opcao == "e":
        print(f'''{extrato}
        
        Saldo atual de R$ : {float(saldo)}
        ''')
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
        
      
        
