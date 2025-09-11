"""Кусок кода для переборки ячеек xlsx файла, когда после количества дней следует слово день (дней, дня)"""
import re
if start_date is not None and duration_str is not None:
    time_delta = re.search(r'\d{2}', duration_str)
    days = int(time_delta.group(0))