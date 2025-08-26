from openpyxl.reader.excel import load_workbook
from datetime import datetime

wb = load_workbook("График производства работ.xlsx", data_only=True)
sheet = wb.active
print(f"Активный лист: {sheet.title}")

names = []
start_dates = []
finish_dates = []

def pars_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

for i in range(25, 130):
    name = sheet["B" + str(i)].value
    start_date = sheet[f'R{i}'].value
    finish_date = sheet[f'S{i}'].value
    if start_date is not None and finish_date is not None:
        start_date = datetime.strftime(start_date, '%d-%m-%Y')
        finish_date = datetime.strftime(finish_date, '%d-%m-%Y')
        start_dates_parsed = pars_date(start_date)
        finish_dates_parsed = pars_date(finish_date)
        names.insert(0, name)
        start_dates.insert(0, start_dates_parsed)
        finish_dates.insert(0, finish_dates_parsed)









