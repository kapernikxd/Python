from urllib import request
from bs4 import BeautifulSoup
from time import sleep

from lxml.html import fromstring
import xlsxwriter



'''
Открывает файл, где лежат url и читает данные
'''

def file_open():
    file = open('urls.txt')
    return [urls.strip() for urls in file]


'''
Парсит Тайт страниц
'''
def parse(urls):

    result = []
    for url in urls:

        date = {'url': url}

        html = request.urlopen(url).read().decode('utf8')
        try:
            soup = BeautifulSoup(html, 'html.parser')
            sleep(2)
            title = soup.find('title').string
            try:
                descrption = soup.select('meta[name="description"]')[0].attrs["content"]
            except:
                descrption = "0"
            try:
                h1 = soup.select('h1')[0].string
            except:
                h1 = "0"

        except:
            title = 'Пропуск'
            descrption = "0"
            h1 = "0"

        date['Тайтл'] = title
        date['Дескрипшин'] = descrption
        date['Заголовок'] = h1

        result.append(date)
    return result





##-------------------------- Загрузка в файл данных


def export_excel(filename, result):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})


    field_names = ('Ссылка', 'Тайтл', 'Дескрипшн', 'H1')
    for i, field in enumerate(field_names):
        worksheet.write(0, i, field, bold)

        fields = ('url', 'Тайтл', 'Дескрипшин', 'Заголовок')

    for row, course in enumerate(result, start=1):
        for col, field in enumerate(fields):
            worksheet.write(row, col, course[field])


    workbook.close()





all_result = parse(file_open())
export_excel('Метатаги-(сайтов).xls', all_result)


#End
