import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import timedelta
import matplotlib.dates as mdates
from sympy.printing.pretty.pretty_symbology import line_width

from main import names, start_dates, finish_dates, number_of_men

start_dates = [pd.Timestamp(date) for date in start_dates]
finish_dates = [pd.Timestamp(date) for date in finish_dates]

# Определяем временной диапазон для анализа занятости
min_start = min(start_dates)
max_finish = max(finish_dates)

# Массив дат для представления временного диапазона
dates_range = pd.date_range(min_start, max_finish, freq='10D')

# Суммарная занятость сотрудников по каждой дате
total_employees_by_day = {}

# Проходим по каждому событию и добавляем численность сотрудников
for idx, event in enumerate(names):
    for dt in dates_range:
        if start_dates[idx] <= dt <= finish_dates[idx]:
            total_employees_by_day[dt] = total_employees_by_day.get(dt, 0) + number_of_men[idx]

# Преобразуем словарь в список пар "дата-значение"
employees_data = [(k, v) for k, v in sorted(total_employees_by_day.items())]

# Подготовка данных для графика
employees_df = pd.DataFrame(employees_data, columns=['Date', 'Total Employees'])

# Основная фигура и ось для графика работ
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Основной график работ
width = 0.5
color = "tab:blue"

for i, event in enumerate(names):
    ax.broken_barh([(start_dates[i], finish_dates[i] - start_dates[i])],
                   (i - width / 2, width),
                   facecolors=color)
    days_word = 'день' if int((finish_dates[i] - start_dates[i]).days) % 10 == 1 and int(
        (finish_dates[i] - start_dates[i]).days) != 11 else (
                    'дня' if int((finish_dates[i] - start_dates[i]).days) % 10 in range(2, 5) and int(
                        (finish_dates[i] - start_dates[i]).days) not in range(11, 16) else 'дней')
    x_text = start_dates[i] + (finish_dates[i] - start_dates[i]) / 2
    y_text = i + 0.5
    ax.text(x_text, y_text, f'{start_dates[i].strftime("%d.%m.%Y")} - {finish_dates[i].strftime("%d.%m.%Y")}, '
                               f'{(finish_dates[i] - start_dates[i]).days} {days_word}, '
              f'{number_of_men[i]} чел.', ha='center', va='center', fontsize=4)

# Настраиваем основную ось X и Y
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names)
start_date = min(start_dates)-timedelta(days=15)
ax.set_xlim(left=start_date, right=max(finish_dates)+timedelta(days=15))
ax.set_title('График работ по монтажу ГМО Городецкого гидроузла')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=90, fontsize=6)
plt.ylim([-1, len(names)])
plt.yticks(fontsize=6)
plt.grid(True, which='both', color='black', linewidth=1)
plt.subplots_adjust(left=0.35, right=0.95, bottom=0.1, top=0.95)
sns.set_style("whitegrid")

# Вторая ось для отображения общей численности сотрудников
ax2 = ax.twinx()

# Строим столбчатую диаграмму (вертикальные столбики)
ax2.bar(employees_df['Date'], employees_df['Total Employees'], align='center',
        color="tab:green", alpha=0.35, width=10,
        label='Общая численность рабочих')

# Аннотируем количество сотрудников над каждым столбцом
for index, row in employees_df.iterrows():
    ax2.annotate(str(row['Total Employees']), xy=(row['Date'], row['Total Employees']),
                  xytext=(0, 3), textcoords="offset points", ha='center', fontsize=5, color="tab:green")
# Оформление второй оси
ax2.set_ylabel('Общее количество рабочих', rotation=90, labelpad=5)
ax2.tick_params(axis='y', colors='tab:green')

max_total_employees = max(total_employees_by_day.values())
plt.yticks(np.arange(0, max_total_employees + 5, step=5), fontsize=6)
plt.grid(visible=True, linewidth=0.5)

plt.show()