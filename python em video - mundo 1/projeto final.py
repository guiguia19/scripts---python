linha = '-=' * 28
linhas = '-' * 28
iguais = '=' * 28
print(linha)
print(f"{'SISTEMA DE DIAGNÓSTICO DE TREINO':^56}")
print(linha)
print(f'\n--> REGISTRO DE ATLETA E SESSÃO')
nome = str(input("Nome do atleta: ")).upper().strip()
distancia = float(input('Distancia percorrida (KM): ').strip())
tempo = float(input('Tempo total da sessão (minutos): ').strip())
frequencia = int(input('Frequência cardíaca média (bpm): ').strip())
idade = int(input('Idade do atleta: ').strip())
peso = float(input('Peso do atleta (KG): ').strip())

pace_min = int(tempo // distancia)
pace_seg = int(((tempo / distancia) % 1) * 60)
calorias = distancia * peso * 0.92
fcmax = 208 - (0.7 * idade)
porcentagem_fc = (frequencia / fcmax) * 100

print(f'\n{linha}')
print(f"{'RELATÓRIO DE TREINO':^56}")
print(linha)
print(f'\nAtleta: {nome}\nResumo: {distancia:.2f} km em {tempo:.0f} min')
print(f'\n[ RITMO E EVOLUÇÃO ]')
print(f'• Pace Médio: {pace_min}\'{pace_seg:02d}/km')
print(f'• Gasto Calórico Estimado: {calorias:.0f} kcal')

print(f'\n[ ZONAS CARDÍACAS ]')
print(f'• Frequência Cardíaca Máxima Estimada: {fcmax:.0f} bpm')
print(f'• FC Média Registrada: {frequencia} bpm ({porcentagem_fc:.1f}% da FC Máx)')
if porcentagem_fc < 60:
    print("• Classificação da FC: Zona 1 - Recuperação / Muito Leve")
elif porcentagem_fc < 70:
    print("• Classificação da FC: Zona 2 - Leve / Aeróbico")
elif porcentagem_fc < 80:
    print("• Classificação da FC: Zona 3 - Moderado / Limiar Aeróbico")
elif porcentagem_fc < 90:
    print("• Classificação da FC: Zona 4 - Intenso / Limiar Anaeróbico")
else:
    print("• Classificação da FC: Zona 5 - Esforço Máximo")

if porcentagem_fc < 70:
    classificacao = "Treino Regenerativo / Leve"
    parecer = ("Ótima sessão de recuperação ativa.\n"
               "  A FC se manteve baixa, ideal para promover regeneração\n"
               "  muscular sem somar fadiga ao corpo.")

elif 70 <= porcentagem_fc < 85:
    classificacao = "Ritmo Moderado"
    parecer = ("Excelente sessão de manutenção aeróbica.\n"
               "  A FC permaneceu dentro da faixa ideal para ganho\n"
               "  de resistência sem gerar desgaste excessivo.")

else:
    classificacao = "Sessão Intensa / Fartlek"
    parecer = ("Treino de alta exigência cardiovascular.\n"
               "  A FC permaneceu em zona elevada; certifique-se de\n"
               "  garantir tempo adequado de descanso para supercompensação.")

print(f'\n{linhas}')
print('[ ANÁLISE TÉCNICA E RECOMENDAÇÃO ]')
print(f'• Classificação do Treino: {classificacao}')
print(f'• Parecer: {parecer}')
print(linhas)
print(iguais)