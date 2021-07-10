# use python ParserSuperJob.py
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.parse import quote
from lxml.html import fromstring

import xlsxwriter

ITEM_PATH = '._2CsQi ._2g1F- ._34bJi'
ITEM_PATH2 = '._2CsQi ._2g1F- .YYC5F'
PAGE = '._1BOkc'


def parser_vacancies():
    f = urlopen(url)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

    dates = []
    for elem in list_doc.cssselect(ITEM_PATH):
        span = elem.cssselect('span')[0]
        dates.append(span.text)

    urls = []
    for elem in list_doc.cssselect(ITEM_PATH2):
        a = elem.cssselect('a')[0]
        urls.append(urljoin(url2, a.get('href')))

    vacancies = []
    i = 0
    for item in dates:
        vacancy = {'date': item, 'url': urls[i]}
        vacancies.append(vacancy)
        i += 1

    return vacancies


def export_excel(filename, vacancies):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})
    field_names = ('Дата', 'URL')
    for i, field in enumerate(field_names):
        worksheet.write(0, i, field, bold)

    fields = ('date', 'url')
    for row, vacancy in enumerate(vacancies, start=1):
        for col, field in enumerate(fields):
            worksheet.write(row, col, vacancy[field])

    workbook.close()


print('Ввидете, что искать')
search = input('> ')

print('Ввидете номер города или страны\nКомсомольск-на-амуре - 0\nХабаровск - 1\nrussia - 2')
sity_array = ['komsomolsk-na-amure', 'habarovsk', 'russia']
sity = sity_array[int(input('> '))]

url = 'https://' + sity + '.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=' + quote(search)\
      + '&keywords%5B0%5D%5Bskwc%5D=and&keywords%5B0%5D%5Bsrws%5D=7&sbmit=1'
url2 = 'https://' + sity + '.superjob.ru'

f = urlopen(url)
list_html = f.read().decode('utf-8')
list_doc = fromstring(list_html)

export_excel('Вакансии ' + search + ' ' + sity + '.xlsx', parser_vacancies())
