import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = math.ceil((area / 6) * 1.1)
latas_necessarias = math.ceil(litros_necessarios / 18)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)

# Compra apenas de latas de 18 litros
preco_latas = latas_necessarias * 80
print(f"Comprando apenas latas de 18 litros, você precisará de {latas_necessarias} latas, a um custo de R$ {preco_latas:.2f}")

# Compra apenas de galões de 3,6 litros
preco_galoes = galoes_necessarios * 25
print(f"Comprando apenas galões de 3,6 litros, você precisará de {galoes_necessarios} galões, a um custo de R$ {preco_galoes:.2f}")

# Mistura de latas e galões
latas_inteiras_necessarias = litros_necessarios // 18
litros_restantes = litros_necessarios % 18
galoes_necessarios_mistura = math.ceil(litros_restantes / 3.6)

if litros_restantes == 0:
    preco_mistura = latas_inteiras_necessarias * 80
    print(f"Comprando apenas latas de 18 litros, você precisará de {latas_inteiras_necessarias} latas, a um custo de R$ {preco_mistura:.2f}")
else:
    preco_mistura = (latas_inteiras_necessarias * 80) + (galoes_necessarios_mistura * 25)
    print(F"Misturando latas e galões, você precisará de {latas_inteiras_necessarias} latas e {galoes_necessarios_mistura} galões, a um custo de R$ {preco_mistura:.2f}")


