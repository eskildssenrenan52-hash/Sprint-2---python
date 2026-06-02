# ChargeGrid Intelligence

## Integrantes

* Renan Eskildssen – RM 571097
* Lucas Barros – RM 571528
* Kaique da Silva Assis - 572718
* Vinicius Cristal de Oliveira - RM 572049
* Andre Debiazzi — RM 569062

# Descrição do Projeto

O ChargeGrid Intelligence é uma prova de conceito desenvolvida para a Sprint 2 do Challenge GoodWe.

O objetivo do projeto é simular o gerenciamento inteligente de energia em estações de carregamento de veículos elétricos, evitando sobrecargas na rede elétrica e calculando automaticamente os valores de recarga dos veículos.

A solução foi desenvolvida utilizando Python e demonstra conceitos de:

* Controle de demanda
* Balanceamento de carga
* Tarifação e pagamento
* Inteligência artificial baseada em regras

# Problema

Quando muitos veículos elétricos são carregados ao mesmo tempo, o consumo de energia pode ultrapassar o limite da instalação.

Isso pode causar:

* Sobrecarga da rede elétrica
* Aumento dos custos de energia
* Multas por excesso de demanda contratada
* Redução da eficiência do sistema

# Solução

O sistema monitora a quantidade de veículos conectados e distribui a energia disponível entre eles.

Quando o número de veículos conectados ultrapassa o limite definido, o sistema reduz automaticamente a potência distribuída para evitar sobrecarga.

Além disso, o sistema calcula o valor da recarga de cada veículo com base no consumo informado pelo usuário e no tipo de tarifa selecionada.

# Funcionalidades

## Controle de Demanda

* Monitora a quantidade de veículos conectados.
* Distribui a energia disponível entre os veículos.

## Balanceamento de Carga

* Reduz automaticamente a potência quando há muitos veículos conectados.

## Inteligência Artificial Simples

* Detecta situações de sobrecarga.
* Toma decisões automáticas para proteger a instalação.

## Tarifação e Pagamento

* Permite selecionar tarifa normal ou tarifa de pico.
* Calcula o valor pago por cada veículo.
* Exibe o valor total arrecadado pela estação.
* 
# Fluxo do Sistema

1. O usuário informa a quantidade de veículos conectados.
2. O sistema calcula a potência disponível para cada veículo.
3. A inteligência artificial verifica possíveis sobrecargas.
4. O usuário escolhe o tipo de tarifa.
5. O sistema registra o consumo de cada veículo.
6. O valor da recarga é calculado automaticamente.
7. O sistema exibe um resumo da operação.

# Estrutura do Projeto

ChargeGrid-Intelligence
│
├── README.md
├── python.py
└── imagens
# Resultados Esperados

O sistema deve:

* Simular uma estação de carregamento.
* Controlar a distribuição de energia.
* Identificar situações de sobrecarga.
* Calcular tarifas de recarga.
* Demonstrar conceitos utilizados pela ChargeGrid em ambientes reais.
