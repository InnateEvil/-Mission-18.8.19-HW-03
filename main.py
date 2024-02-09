def ticket_cost(age):
    if age < 18:
        return 0
    elif age <= 25:
        return 990
    else:
        return 1390

# Запрашиваем количество билетов
num_tickets = int(input("Введите количество билетов: "))

# Инициализируем переменную для подсчета общей стоимости
total_cost = 0

# Запрашиваем возраст для каждого билета и обновляем общую стоимость
for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i + 1}: "))
    total_cost += ticket_cost(age)

# Проверяем, нужно ли применить скидку
if num_tickets > 3:
    total_cost *= 0.9  # Применяем скидку 10%

print("Сумма к оплате:", total_cost)