# цель рассчитать среднюю стоимость 
# одного квадратного метра жилья в заданном районе по имеющимся данным.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Загрузка данных из CSV-файла
df = pd.read_csv('apartments.csv')

# Просмотр первых 5 строк данных
print(df.head())

# Проверка на пропуски
print(df.isnull().sum())

# Удаление строк с пропущенными значениями
df = df.dropna()

# Проверка на дубликаты
duplicates = df.duplicated().sum()
print(f'Количество дубликатов: {duplicates}')

# Удаление дубликатов
df = df.drop_duplicates()

# Фильтрация данных: оставляем только положительные значения
df = df[(df['Площадь (м²)'] > 0) & (df['Стоимость (руб.)'] > 0)]

# Рассчет стоимости за квадратный метр
df['Стоимость за кв.м'] = df['Стоимость (руб.)'] / df['Площадь (м²)']

# Сохранение очищенных данных
df.to_csv('cleaned_apartments.csv', index=False)

# Рассчитываем среднее значение стоимости за квадратный метр
average_price_per_sqm = df['Стоимость за кв.м'].mean()

print(f"Средняя стоимость за квадратный метр: {average_price_per_sqm:.2f} руб.")

# Рассчитываем дополнительные статистики
median_price_per_sqm = df['Стоимость за кв.м'].median()
std_dev_price_per_sqm = df['Стоимость за кв.м'].std()

print(f"Медиана стоимости за квадратный метр: {median_price_per_sqm:.2f} руб.")
print(f"Стандартное отклонение стоимости за квадратный метр: {std_dev_price_per_sqm:.2f} руб.")


import matplotlib.pyplot as plt
import seaborn as sns

# Настройка стиля визуализации
sns.set(style="whitegrid")

# Визуализация распределения цены за квадратный метр
plt.figure(figsize=(10, 6))
sns.histplot(df['Стоимость за кв.м'], bins=20, kde=True)
plt.title("Распределение стоимости за квадратный метр")
plt.xlabel("Стоимость за квадратный метр (руб.)")
plt.ylabel("Частота")
plt.axvline(average_price_per_sqm, color='red', linestyle='dashed', linewidth=1, label='Среднее значение')
plt.axvline(median_price_per_sqm, color='blue', linestyle='dashed', linewidth=1, label='Медиана')
plt.legend()
plt.show()









