from pprint import pprint
from openpyxl.reader.excel import load_workbook
from datetime import datetime
import pandas as pd

def pars_date(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y').date()

wb = load_workbook("C:/Users/KNV/PycharmProjects/fifteenth/data.xlsx", data_only=True)
excel_file = pd.ExcelFile("C:/Users/KNV/PycharmProjects/fifteenth/data.xlsx")
sheets_data = [excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names]

names = []
start_dates = []
finish_dates = []
time_deltas = []

# for sheet in sheets_data:
#     names_str = []
#     start_dates_str = []
#     finish_dates_str = []
#     first_col = sheets_data[sheet].iloc[:, 0].tolist()
#     names.extend(first_col)
#     second_col = sheets_data[sheet].iloc[:, 1].tolist()
#     start_dates_str.extend(second_col)
#     third_col = sheets_data[sheet].iloc[:, 2].tolist()
#     finish_dates_str.extend(third_col)
#     for name in names_str:
#         names.append(name)
#     for elem in start_dates_str:
#         start_dates.append(pars_date(elem))
#     for item in finish_dates_str:
#         finish_dates.append(pars_date(item))

print(len(names))
print(len(start_dates))
print(len(finish_dates))
print(len(sheets_data))