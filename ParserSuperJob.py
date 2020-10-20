from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring
from lxml.etree import XMLSyntaxError

import xlsxwriter

URL = 'https://komsomolsk-na-amure.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=java&keywords%5B0%' \
      '5D%5Bskwc%5D=and&keywords%5B0%5D%5Bsrws%5D=7&sbmit=1'

# _1Ttd8 _2CsQi list vakansii
ITEM_PATH = '._2CsQi ._2g1F-'

# s = '._3zucV undefined _3SGgo .f-test-resume-snippet-46283839 .iJCa5 undefined _2nteL ._2wheF _1Ltf7 ._3VUIu ' \
#             '._2g1F- ._3zucV ._3-1ww undefined _3SGgo _3zucV _3-1ww undefined _3SGgo'
#
# DESCR_PATH = '.section-info .left-sect'
# TEACH_PATH = '#teach_slider .reader_desc .name'


def parser_courses():
    f = urlopen(URL)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)

#     courses = []
    for elem in list_doc.cssselect(ITEM_PATH):
        print(elem)
#         a = elem.cssselect('a')[0]
#         href = a.get('href')
#         name = a.text
#         p = elem.csselct('p')[0]
#         load = p.text
#         url = urljoin(URL, href)
#
#         course = {'name': name, 'load': load, 'url': url}
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
#     return course
#
#
# def export_excel(filename, courses):
#     workbook = xlsxwriter.Workbook(filename)
#     worksheet = workbook.add_worksheet()
#
#     bold = workbook.add_format({'bold': True})
#     field_names = ('Название', 'Описание', 'URL', 'Преподователи')
#     for i, field in enumerate(field_names):
#         worksheet.write(0, i, field, bold)
#
#     field = ('name', 'lead', 'url')
#     for row, course in enumerate(courses, start=1):
#         for col, field in enumerate(field):
#             worksheet.write


def main():
    courses = parser_courses()


if __name__ == '__main__':
    main()
