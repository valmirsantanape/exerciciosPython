capital = float(input("Capital de investimento: "))
taxaPercentual = float(input("Taxa aplicada ao mês: "))
taxa = taxaPercentual / 100
tempoMeses = int(input("Tempo do valor investido em meses: "))

juros = capital * tempoMeses * taxa

print("=-" * 30, "\n")

print(f"Considerando o valor investido no periodo de {tempoMeses}", "mês" if tempoMeses == 1 else "meses",  f"renderá de juros o valor de R${juros:.2f}")
print("=-" * 30, "\n")