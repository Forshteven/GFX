"""Модуль для работы с файлом xlsx, включающим один лист"""
from openpyxl.reader.excel import load_workbook
from datetime import datetime, timedelta
import re

def pars_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

wb = load_workbook("data.xlsx", data_only=True)
sheet = wb['Данные по ГМО']

names = []
start_dates = []
finish_dates = []
time_deltas = []

for i in range(1, 100):
    name = sheet["A" + str(i)].value
# Часть кода для случая, когда указаны даты начала работ и их продолжительности, но не указаны даты окончания работ
#     start_date = sheet[f'B{i}'].value
#     duration_str = sheet[f'D{i}'].value
#     if isinstance(start_date, datetime):
#         start_dates.insert(0, start_date.date())
#         finish_date = start_date.date() + timedelta(days=duration_str)
#         finish_dates.insert(0, finish_date)
#     elif start_date is not None and duration_str is not None:
#         start_date_parsed = pars_date(start_date)
#         finish_date_parsed = pars_date(start_date) + timedelta(days=duration_str)
#         names.insert(0, name)
#         start_dates.insert(0, start_dates_parsed)
#         finish_dates.insert(0, finish_dates_parsed)
#     else:
#         continue
# Часть кода для случая, когда указаны даты начала и окончания работ
    start_date = sheet[f'B{i}'].value
    finish_date = sheet[f'C{i}'].value
    if isinstance(start_date and finish_date, datetime):
        start_dates.insert(0, start_date.date())
        finish_dates.insert(0,finish_date.date())
    elif start_date is not None and finish_date is not None:
        start_date_parsed = pars_date(start_date)
        finish_date_parsed = pars_date(finish_date)
        start_dates.insert(0, start_date_parsed)
        finish_dates.insert(0, finish_date_parsed)
    else:
        continue
    names.insert(0, name)












