# Sistema de gerenciamento de energia para estações de carregamento de veículos elétricos

# Renan Eskildssen – RM 571097, Lucas Barros – RM 571528, Kaique da Silva Assis - 572718, Vinicius Cristal de Oliveira - RM 572049, Andre Debiazzi — RM 569062

# Limite máximo de energia disponível

limite_energia = 100

print("=========================================")
print("=== CHARGEGRID INTELLIGENCE ===")
print("=========================================")

# Quantidade de veículos conectados

veiculos = int(input("Digite a quantidade de veículos: "))

# Calcula a potência por veículo

potencia = limite_energia / veiculos

# Inteligência Artificial simples (baseada em regras)

if veiculos > 3:
    print("\nALERTA DE SOBRECARGA")
    print("A IA detectou muitos veículos conectados.")
    print("Potência reduzida automaticamente em 20%.")
    potencia = potencia * 0.8
    status = "Sobrecarga Controlada"
else:
    print("\nTudo funcionando normalmente.")
    print("A IA não identificou riscos.")


status = "Operação Normal"


# Resumo de energia

print("\n=========================================")
print("=== RESUMO DE ENERGIA ===")
print("=========================================")
print("Limite de energia:", limite_energia, "kW")
print("Veículos conectados:", veiculos)
print("Potência por veículo:", potencia, "kW")
print("Status do sistema:", status)
print("=========================================")

# Tarifação

print("\nEscolha o tipo de tarifa:")
print("1 - Horário normal (R$ 0,80 por kWh)")
print("2 - Horário de pico (R$ 1,50 por kWh)")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    tarifa = 0.80
    tipo_tarifa = "Horário Normal"
else:
    tarifa = 1.50
    tipo_tarifa = "Horário de Pico"

valor_total = 0

print("\n=========================================")
print("=== TARIFAÇÃO DOS VEÍCULOS ===")
print("=========================================")

for i in range(1, veiculos + 1):
    consumo = float(input("Digite o consumo do veículo " + str(i) + " em kWh: "))
    valor = consumo * tarifa
    print("-----------------------------------------")
    print("Veículo:", i)
    print("Consumo:", consumo, "kWh")
    print("Valor a pagar: R$", valor)
    print("-----------------------------------------")
    valor_total = valor_total + valor

print("=========================================")
print("=== RESUMO DA TARIFAÇÃO ===")
print("=========================================")
print("Tipo de tarifa:", tipo_tarifa)
print("Valor por kWh: R$", tarifa)
print("Quantidade de veículos:", veiculos)
print("Valor total arrecadado: R$", valor_total)
print("=========================================")

print("\nSistema finalizado com sucesso.")
