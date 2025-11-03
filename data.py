import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из первого файла (только 2 столбца)
df1 = pd.read_csv('Кривая_разгона_по_каналу_возмущения.csv',
                 delimiter=';',
                 decimal=',',
                 encoding='utf-8',
                 header=None,
                 skiprows=0,
                 usecols=[0, 1],  # Только Время и Вход1
                 names=['Время', 'Вход1'])  # Только два столбца

# Чтение данных из второго файла (только 2 столбца)
df2 = pd.read_csv('Кривая_разгона_по_каналу_регулирования.csv',
                 delimiter=';',
                 decimal=',',
                 encoding='utf-8',
                 header=None,
                 skiprows=0,
                 usecols=[0, 1],  # Только Время и Вход1
                 names=['Время', 'Вход1'])  # Только два столбца

# Обработка данных для первого файла
df1 = df1.apply(lambda x: pd.to_numeric(x.astype(str).str.strip(), errors='coerce'))
df1 = df1.dropna()

# Обработка данных для второго файла
df2 = df2.apply(lambda x: pd.to_numeric(x.astype(str).str.strip(), errors='coerce'))
df2 = df2.dropna()

print(f"Загружено {len(df1)} строк из файла возмущения")
print(f"Загружено {len(df2)} строк из файла регулирования")

# Фильтруем данные для первого графика (только с 1950 секунд)
df1_filtered = df1[df1['Время'] >= 1950]

# Первый график: данные из файла возмущения (начиная с 1950 секунд)
plt.figure(figsize=(12, 6))
plt.plot(df1_filtered['Время'], df1_filtered['Вход1'], 'b-', label='Вход 1', linewidth=1)
plt.xlabel('Время, с')
plt.ylabel('Значения')
plt.title('График из файла: Кривая_разгона_по_каналу_возмущения.csv (после нанесения возмущения)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Второй график: данные из файла регулирования (полный график)
plt.figure(figsize=(12, 6))
plt.plot(df2['Время'], df2['Вход1'], 'b-', label='Вход 1', linewidth=1)
plt.xlabel('Время, с')
plt.ylabel('Значения')
plt.title('График из файла: Кривая_разгона_по_каналу_регулирования.csv')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Для первого графика отображено {len(df1_filtered)} строк (с 1950 секунд)")