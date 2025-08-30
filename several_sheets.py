import pandas as pd
from mpmath import extend

excel_file = pd.ExcelFile("data.xlsx")


names_df = {sheet_name: excel_file.parse(sheet_name, header=None, usecols=[0]) for sheet_name in excel_file.sheet_names}
start_dates_df = {sheet_name: excel_file.parse(sheet_name, header=None, usecols=[1]) for sheet_name in excel_file.sheet_names}
finish_dates_df = {sheet_name: excel_file.parse(sheet_name, header=None, usecols=[2]) for sheet_name in excel_file.sheet_names}

names = []
for df in names_df.values():
    dates_list3 = df.values.ravel().tolist()
    for i in dates_list3:
        names.insert(0, i)
start_dates = []
for df in start_dates_df.values():
    dates_list = pd.to_datetime(df.values.ravel(), errors='coerce', format='%d-%m-%Y').to_list()
    for i in dates_list:
        start_dates.insert(0, i)
finish_dates = []
for df in finish_dates_df.values():
    dates_list2 = pd.to_datetime(df.values.ravel(), errors="coerce", format='%d-%m-%Y').to_list()
    for i in dates_list2:
        finish_dates.insert(0, i)

time_deltas = []

print(help(extend))
