elevadores = {'A': 0, 'B': 0, 'C': 0}
periodos = {'M': 0, 'V': 0, 'N': 0}


while True:
    elevador = input("Digite o elevador utilizado pelo morador (A, B ou C): ")
    if elevador not in elevadores:
        print("Elevador inválido! Digite A, B ou C.")
        continue
    
    periodo = input("Digite o período utilizado pelo morador (M = Matutino, V = Vespertino, N = Noturno): ")
    if periodo not in periodos:
        print("Período inválido! Digite M, V ou N.")
        continue
    
    
    elevadores[elevador] += 1
    periodos[periodo] += 1
    
    
    continuar = input("Deseja continuar informando dados? (S/N): ")
    if continuar.upper() == "N":
        break


elevador_mais_utilizado = max(elevadores, key=elevadores.get)
periodo_mais_usado = max(periodos, key=periodos.get)
maior_fluxo = max(periodos.values())
percentual = 0


if periodos[periodo_mais_usado] != 0:
    percentual = (maior_fluxo - periodos[periodo_mais_usado]) / periodos[periodo_mais_usado] * 100
else:
    percentual = 100  


periodo_mais_utilizado = max(periodos, key=periodos.get)


print("O elevador mais utilizado é o elevador", elevador_mais_utilizado, "e o período em que se concentra o maior fluxo é o período", periodo_mais_usado)
print("O período mais utilizado é o período", periodo_mais_utilizado)
print("A diferença percentual entre o período mais utilizado e o menos utilizado é de", round(percentual, 2), "%")
