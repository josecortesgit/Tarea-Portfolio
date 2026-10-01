from config import IVA, DISCOUNT, CURRENCY

PRICE = 100

total = PRICE + PRICE * IVA
final = total - total * DISCOUNT

print(f"Precio: {PRICE} {CURRENCY}")
print(f"Total con IVA: {total:.2f} {CURRENCY}")
print(f"Precio final con descuento: {final:.2f} {CURRENCY}")
