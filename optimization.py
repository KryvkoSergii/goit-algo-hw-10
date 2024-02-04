import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Оголошення змінних рішення
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat=pulp.LpInteger)
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat=pulp.LpInteger)

# Об'єктивна функція (максимізація виробництва)
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Оптимальний план:")
print(f"Лимонад: {pulp.value(lemonade)} units")
print(f"Фруктовий сік: {pulp.value(fruit_juice)} units")
print(f"Загальне виробництво: {pulp.value(model.objective)} units")