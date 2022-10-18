a = int(input("Ваша сумма заказа:"))
total = a * 0.2 + a * 0.18
taxes = a * 0.2
tips = a * 0.18
print(f'{taxes:.2f}',",",f'{tips:.2f}',",",f'{total:.2f}')