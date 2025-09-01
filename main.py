"""Модуль для работы с файлом xlsx, включающим один лист"""
from openpyxl.reader.excel import load_workbook
from datetime import datetime, timedelta
import re

def pars_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

wb = load_workbook("График строительства гидроузла на 2025-2026.xlsx", data_only=True)
sheet = wb.active

names = []
start_dates = []
finish_dates = []
time_deltas = []

for i in range(24, 150):
    name = sheet["B" + str(i)].value
    start_date = sheet[f'H{i}'].value
    finish_date = sheet[f'I{i}'].value

# Часть кода для случая, когда указаны даты начала работ и их продолжительности, но не указаны даты окончания работ
    # duration_str = sheet[f'I{i}'].value
    # if start_date is not None and duration_str is not None:
    #     time_delta = re.search(r'\d{2}', duration_str)
    #     days = int(time_delta.group(0))
    #     start_date = datetime.strftime(start_date, '%d-%m-%Y')
    #     start_dates_parsed = pars_date(start_date)
    #     finish_dates_parsed = pars_date(start_date) + timedelta(days=days)
    # else:
    #     continue
# Часть кода для случая, когда указаны даты начала и окончания работ
    if  isinstance(start_date, datetime) and isinstance(finish_date, datetime):
        start_date = datetime.strftime(start_date, '%d-%m-%Y')
        finish_date = datetime.strftime(finish_date, '%d-%m-%Y')
        start_dates_parsed = pars_date(start_date)
        finish_dates_parsed = pars_date(finish_date)
    else:
        continue

    names.insert(0, name)
    start_dates.insert(0, start_dates_parsed)
    finish_dates.insert(0, finish_dates_parsed)










