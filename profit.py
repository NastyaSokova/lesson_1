profit = float(input("Введите выручку "))
costs = float(input("Введите издержки "))
if profit > costs:
    print(f"Работа с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    countworkers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника  {profit / countworkers:.2f}")
elif profit == costs:
    print("Работа в ноль")
else:
    print("Работа в убыток")