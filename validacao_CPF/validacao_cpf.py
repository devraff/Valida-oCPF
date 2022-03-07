while True:

    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    if len(cpf) != 11 and not cpf.isnumeric():
        print('Digite os 11(onze) números do CPF.')

    else:

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)

        sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

        if cpf == novo_cpf and not sequencia:
            print('CPF válido')

        else:
            print('CPF inválido')

