#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pdfFile.py
Created on 16|06
           -----
           20|18

@author: Rdlc_Dev(Alain)
"""


import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

def pdf(filein):
    txt = open(filein, 'r').read()
    docpdf = SimpleDocTemplate(fileout, 
                               pagesize = A4)
    style = getSampleStyleSheet()
    style.add(ParagraphStyle(name='Chinese', fontName='STSong-Light', fontSize=12, leading=14, wordWrap = 'CJK'))

    story = []
    paragraphs = txt.split("\n")
    for para in paragraphs:
        story.append(Paragraph(para, style["Chinese"]))
        story.append(Spacer(0, cm * .3))
    docpdf.build(story)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Utilisation : <script> textfile pdffile')
        sys.exit(1)
    else :
        filein = sys.argv[1]
        fileout = sys.argv[2]
        pdf(filein)