# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : PDF_split
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/2/27: Create

from PyPDF2 import PdfFileReader, PdfFileWriter


def splitPDF(file, writePath, perPage):
    sc_pdf = PdfFileReader(open(file, 'rb'))
    count_sc = sc_pdf.getNumPages()
    out_pdf = PdfFileWriter()
    for c in range(count_sc):
        if (c+1) % perPage == 0 and c > 0:
            out_pdf.addPage(sc_pdf.getPage(c))
            with open(writePath + '切分_{}.pdf'.format(c+1), 'wb') as wf:
                out_pdf.write(wf)
            out_pdf = PdfFileWriter()
        else:
            out_pdf.addPage(sc_pdf.getPage(c))


if __name__ == '__main__':
    file = "need split/GEO-Andy.pdf"
    writePath = "split/"
    perPage = 30
    splitPDF(file, writePath, perPage)