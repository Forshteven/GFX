from datetime import timedelta

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from main import names, start_dates, finish_dates

fig, ax = plt.subplots(dpi=100)

width = 0.5
color = "tab:blue"

for i, event in enumerate(names):
    ax.broken_barh([(start_dates[i], finish_dates[i] - start_dates[i])],
                   (i - width / 2, width),
                   facecolors=color)
    days_word = 'день' if int((finish_dates[i] - start_dates[i]).days) % 10 == 1 and int((finish_dates[i] - start_dates[i]).days) != 11 \
        else ('дня' if int((finish_dates[i] - start_dates[i]).days) % 10 in range(2, 5) and int((finish_dates[i] - start_dates[i]).days)
        not in range(11, 16) else 'дней')
    x_text = start_dates[i] + (finish_dates[i] - start_dates[i]) / 2
    y_text = i + 0.5
    ax.text(x_text, y_text, f'{start_dates[i].strftime('%d-%m-%Y')} - {finish_dates[i].strftime('%d-%m-%Y')}, '
                            f'{(finish_dates[i] - start_dates[i]).days} {days_word}', ha='center', va='center', fontsize=5)

ax.set_yticks(range(len(names)))
ax.set_yticklabels(names)
start_date = min(start_dates)-timedelta(days=15)
ax.set_xlim(left=start_date, right=max(finish_dates)+timedelta(days=15))
ax.set_title('График работ по монтажу ГМО Красногорского ГУ')
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# Показать график
plt.xticks(rotation=0, fontsize=8)
plt.ylim([-1, len(names)])
plt.yticks(fontsize=8)
plt.grid(True, which='both', color='black', linewidth=1)
plt.subplots_adjust(left=0.43, right=0.98, bottom=0.05, top=0.95)
plt.plot()
plt.show()