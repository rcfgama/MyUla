Resu = 0b0  # Variável que recebe o resultado da ULA.
Oper = ''  # Variável que recebe o sinal da operação desejada.
EntA = ''  # Variavel que recebe a primeira entrada do usuario (1).

while EntA != '8':
    print('Menu Principal da ULA:\n ')

    EntA = input('1. Definir registrador A\n'
                 '2. Definir registrador B\n'
                 '3. Ler registrador A (Acc)\n'
                 '4. Ler Registrador B\n'
                 '5. Ler Registrador de flags\n'
                 '6. Definir operação\n'
                 '7. Executar ULA\n'
                 '8. Sair\n ')

    if EntA != '8':
        while EntA != '1':
            EntA = input('Valor não esperado. Por favor, tecle "1" para definir registrador A:\n ')

        if Resu == 0b0:
            OpeA = input('Insira um valor para o registrador A:\n ')  # Operando A.
            while OpeA == '':
                OpeA = input('Por favor, informe um valor para o registrador A:\n ')
            SF = 0b0  # Sign Flag.
        else:
            OpeA = Resu
            if Resu < 0b0:
                SF = 0b1
            else:
                SF = 0b0

        EntB = input('Registrador A definido. Por favor, tecle "2" para definir registrador B:\n ')
        while EntB != '2':  # Variavel que recebe a segunda entrada do usuario (2)
            EntB = input('Valor não esperado. Por favor, tecle "2" para definir registrador B:\n ')

        OpeB = input('Insira um valor para o registrador B:\n ')  # Operando B.
        while OpeB == '':
            OpeB = input('Por favor, informe um valor para o registrador B:\n ')

        RegA = input('Registrador B definido. Por favor, tecle "3" para ler registrador A:\n ')  # Registrador A.
        while RegA != '3':
            RegA = input('Valor não esperado. Por favor, tecle "3" para ler registrador A:\n ')
        RegA = OpeA

        RegB = input('Leitura realizada no registrador A. Por favor, tecle "4" para ler registrador B:\n')
        while RegB != '4':  # Registrador B.
            RegB = input('Valor não esperado. Por favor, tecle "4" para ler registrador B:\n ')
        RegB = OpeB

        RegF = input('Leitura realizada no registrador B. Por favor, tecle "5" para ler registrador de flags:\n')
        while RegF != '5':  # Registrador de Flags.
            Regf = input('Valor não esperado. Por favor, tecle "5" para ler registrador de Flags:\n ')
        if Resu == 0b100000000:
            CF = 0b1  # Carry Flag
        else:
            CF = 0b0
        if Resu == 0b10000:
            AF = 0b1  # Auxiliary Carry Flag
        else:
            AF = 0b0
        if Resu == 0b0:
            ZF = 0b1  # Zero Flag
        else:
            ZF = 0b0
        RegA = str(RegA)
        PF = RegA  # Parity Flag
        PF = list(PF)
        PF = PF.count('1')
        PF = PF % 2
        if PF == 0:
            PF = 0b1
        else:
            PF = 0b0
        print(f'CF = {CF}, PF = {PF}, AF = {AF}, ZF = {ZF}, SF = {SF}')

        Oper = input('Leitura realizada no registrador de flags. Por favor, tecle "6" para definir operação:\n')
        while Oper != '6':
            Oper = input('Valor não esperado. Por favor, tecle "6" para definir operação:\n ')
        Oper = input('Por favor, tecle o sinal equivalente a operação desejada:\n')
        while Oper != '+' and Oper != '-' and Oper != 'x' and Oper != '*' and Oper != '/':
            Oper = input('Sinal não esperado. Por favor, tecle o sinal equivalente a operação desejada:\n ')
        if Oper == '+':
            Exec = input('Operação soma definida. Por favor, tecle "7" para executar a ULA:\n ')
        elif Oper == '-':
            Exec = input('Operação subtração definida. Por favor, tecle "7" para executar a ULA:\n ')
        elif Oper == '*' or Oper == 'x':
            Exec = input('Operação multiplicação definida. Por favor, tecle "7" para executar a ULA:\n ')
        else:
            Exec = input('Operação divisão definida. Por favor, tecle "7" para executar a ULA:\n ')

        while Exec != '7':  # Variavel para a execução da ULA.
            Exec = input('Valor não esperado. Por favor, tecle "7" para executar a ULA:\n ')

        if Resu != 0b0:
            RegA = int(RegA)
            RegB = int(RegB, base=2)
            RegB = int(RegB)
        else:
            RegA = int(RegA, base=2)
            RegB = int(RegB, base=2)
        if Oper == '+':
            Resu = RegA + RegB
            Resu = bin(Resu)
            print(f'O resultado é: {Resu}\n')
        elif Oper == '-':
            Resu = RegA - RegB
            Resu = bin(Resu)
            print(f'O resultado é: {Resu}\n')
        elif Oper == '*' or Oper == 'x':
            Resu = RegA * RegB
            Resu = bin(Resu)
            print(f'O resultado é: {Resu}\n')
        else:
            Resu = RegA / RegB
            Resu = int(Resu)
            Resu = bin(Resu)
            print(f'O resultado é: {Resu}\n')
        Resu = int(Resu, base=2)
    else:
        print('Obrigado por usar ULA')

