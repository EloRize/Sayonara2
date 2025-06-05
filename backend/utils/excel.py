from fastapi.responses import FileResponse
import openpyxl
import csv
import tempfile

# Для простоты сохраняем формулы и форматирование благодаря openpyxl, который сохраняет стили

def stream_excel(path: str):
    return FileResponse(path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename='Кураторская.xlsx')


def process_csv(xlsx_path: str, file):
    wb = openpyxl.load_workbook(xlsx_path)
    ws_curator = wb['Куратор'] if 'Куратор' in wb.sheetnames else wb.active

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp.flush()
        tmp.seek(0)
        reader = csv.DictReader(open(tmp.name, encoding='utf-8'))
        for row in reader:
            date = row.get('Дата создания')
            packaging = row.get('Упаковка')
            ws_curator.append([date, None, None, None, None, packaging])
    wb.save(xlsx_path)
