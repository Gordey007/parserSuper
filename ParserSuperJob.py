from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.parse   import quote

from lxml.html import fromstring
from lxml.etree import XMLSyntaxError

import xlsxwriter

print('Ввидете что искать')
search = input()
URL = 'https://komsomolsk-na-amure.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=' + quote(search)\
      + '&keywords%5B0%5D%5Bskwc%5D=and&keywords%5B0%5D%5Bsrws%5D=7&sbmit=1'

print(URL)
URL2 = 'https://komsomolsk-na-amure.superjob.ru'

# _1Ttd8 _2CsQi list vakansii
ITEM_PATH = '._2CsQi ._2g1F- ._34bJi'

# _3dPok
ITEM_PATH2 = '._2CsQi ._2g1F- .YYC5F '

# icMQ_ YYC5F f-test-link-Inzhener_mehanik_tehnik f-test-link- _3dPok

# s = '._3zucV undefined _3SGgo .f-test-resume-snippet-46283839 .iJCa5 undefined _2nteL ._2wheF _1Ltf7 ._3VUIu ' \
#             '._2g1F- ._3zucV ._3-1ww undefined _3SGgo _3zucV _3-1ww undefined _3SGgo'
#
# DESCR_PATH = '.section-info .left-sect'
# TEACH_PATH = '#teach_slider .reader_desc .name'


def parser_vacancies():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

    date = []
    for elem in list_doc.cssselect(ITEM_PATH):
        # print(elem)
        span = elem.cssselect('span')[0]
        date.append(span.text)
        # print(date)

    url = []
    for elem in list_doc.cssselect(ITEM_PATH2):
        a = elem.cssselect('a')[0]
        url.append(urljoin(URL2, a.get('href')))
        # href = a.get('href')
        # print(urljoin(URL2, href))

#         p = elem.csselct('p')[0]
#         load = p.text
#         url = urljoin(URL, href)

    vacancies = []
    i = 0
    # vacancy = {}
    for item in date:
        vacancy = {'date': item, 'url': url[i]}
        # vacancy['date'] = item
        # vacancy['url'] = url[i]
        vacancies.append(vacancy)
        i += 1

    # for item in vacancies:
    #     print(item)

    return vacancies

#
#         details_html = urlopen(url).read().decode('utf-8')
#
#         try:
#             details_doc = fromstring(details_html)
#         except XMLSyntaxError:
#             continue
#
#         descr_elem = details_doc.cssselect(DESCR_PATH)
#         descr = descr_elem.text_content()
#
#         teach_elem = details_doc.cssselect(TEACH_PATH)
#         teach = [teach_elem.text for teach_elem in teach_elem]
#
#         #course['descr'] = descr
#         course['teach'] = teach
#         courses.append(course)


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


def main():
    export_excel('vacancies.xlsx', parser_vacancies())


if __name__ == '__main__':
    main()
