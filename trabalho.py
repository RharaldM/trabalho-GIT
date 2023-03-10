#LISTA QUE IRÁ RECEBER AS INF. DOS USUÁRIOS
usuarios = []

while True:

    #NOME DO USUÁRIO
    nom = ''
    nom = input("Nome: ")

    #USUARIO IRÁ INFORMAR A QUANTIDADE DE HORAS TRABALHADAS POR MÊS

    hora_trab = int(input("Digite a quantidade de horas que você trabalhou esse mês: "))

    
    #SALÁRIO MINIMO E QUANT POR HORA TRABALHADA
    sal_min = float(1320.00)
    sal_pht10 = ((sal_min*0.1) + sal_min) / hora_trab
    sal_pht15 = ((sal_min*0.15) + sal_min) / hora_trab
    sal_pht9 = ((sal_min*0.09) + sal_min) / hora_trab
    sal_pht14 = ((sal_min*0.14) + sal_min) / hora_trab

    #SALÁRIO FINAL
    sal_final10 = (sal_min*0.1) + sal_min
    sal_final15 = (sal_min*0.15) + sal_min
    sal_final9 = (sal_min*0.09) + sal_min
    sal_final14 = (sal_min*0.14) + sal_min

    #PERIODO DO USUÁRIO
    periodo = ''
    while periodo not in ["M","V","N"]:
        periodo = input("Selecione seu turno, Matutino = [M], Vespertino = [V], Noturno = [N] : ").upper()

    #CATEGORIA DO USUÁRIO
    categoria = ''
    while categoria not in ["G","O"]:
        categoria = input("Gerente [G] ou Operário [O]: ") .upper()

    #OPÇÕES QUE O USUÁRIO IRÁ ESCOLHER

    if periodo == "M":
        periodo_msg = ("Matutino")

    elif periodo == "V":
        periodo_msg = ("Vespertino")

    else: 
        periodo_msg = ("Noturno")

    if categoria == "G":
        categoria_msg = ("Gerente")
        if periodo == "N":
            sal_pht = sal_pht10
            sal_final = sal_final10
        else:
            sal_pht = sal_final15
            sal_final = sal_final15

        
    if categoria == "O":
        categoria_msg = ("Operário")
        if periodo == "N":
            sal_pht = sal_pht9
            sal_final = sal_final9
        else:
            sal_pht = sal_pht14
            sal_final = sal_final14
    usuarios.append({'nome': nom, 'periodo': periodo_msg, 'categoria': categoria_msg, 'Salário': sal_final, 'Salário_Por_Hora': sal_pht})
    print(usuarios)

    continuar = input("Deseja registar um novo usuário? [S]/[N]: ")
    if continuar.upper() == 'N':
        break
    else:
        if continuar.upper() != 'S':
            break

