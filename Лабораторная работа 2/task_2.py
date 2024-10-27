salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_needed = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(months):
    if month > 0:
        spend *= (1 + increase)

    if salary < spend:
        total_needed += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_needed))