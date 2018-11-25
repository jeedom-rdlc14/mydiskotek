#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
table2Pdf.py
Created on 12|04
           -----
           20|18

@author: Rdlc_Dev(Alain)
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.linecharts import SampleHorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

#from config import STATIC_ROOT
from myapp.pdfUtils import get_random_colors

legendcolors = get_random_colors(10)

class PdfPrint:

    # initialize class
    def __init__(self, buffer, pageSize, orientation):
        self.buffer = buffer
        # default format is A4
        if orientation == 'paysage':
            if pageSize == 'A4':
                self.pageSize = landscape(A4)
            elif pageSize == 'Letter':
                self.pageSize = landscape(letter)
        elif orientation == 'portrait':
            if pageSize == 'A4':
                self.pageSize = A4
            elif pageSize == 'Letter':
                self.pageSize = letter
    
        self.width, self.height = self.pageSize

    def pageNumber(self, canvas, doc):
        number = canvas.getPageNumber()
        canvas.drawCentredString(145*mm, 10*mm, str(number))

    def report(self, disks, title, today):
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=32,
            leftMargin=32,
            topMargin=32,
            bottomMargin=32,
            pagesize=self.pageSize)

        # a collection of styles offer by the library
        styles = getSampleStyleSheet()
        # add custom paragraph style
        styles.add(ParagraphStyle(
            name="TableHeaderCenter", fontSize=11, alignment=TA_CENTER, fontName="Times-Roman"))
        styles.add(ParagraphStyle(
            name="ParagraphTitle", fontSize=11, alignment=TA_CENTER, fontName="Times-Roman"))
        styles.add(ParagraphStyle(
            name="Justify", alignment=TA_JUSTIFY, fontName="Times-Roman"))
        styles.add(ParagraphStyle(
            name="Left", alignment=TA_LEFT, fontName="Times-Roman"))
        # list used for elements added into document
        data = []
        data.append(Paragraph(title, styles['Title']))
        # insert a blank space
        data.append(Spacer(1, 12))
        table_data = []
        
        data.append(Paragraph(u'Liste des albums au : {0} '.format(today.strftime('%d-%m-%Y')), styles['Left']))
        data.append(Spacer(1, 12))
        
        # table header    
        table_data.append([
            Paragraph('Artiste', styles['TableHeaderCenter']),
            Paragraph('Album', styles['TableHeaderCenter']),
            Paragraph('Release', styles['TableHeaderCenter']),
            Paragraph('Année', styles['TableHeaderCenter']),
            Paragraph('Stockage', styles['TableHeaderCenter']),
            Paragraph('Place', styles['TableHeaderCenter'])])
        
        for album in disks:
            artist = album['artists']
            artiste = artist[0].get('name') 
            storage = album['storage']
            rangement = storage['nom']
            position = int(storage['position'])
            
            table_data.append(
                [Paragraph(artiste, styles['Left']),
                u"{0}".format(album['title']),
                u"{0}".format(str(int(album['id']))),
                u"{0}".format(str(int(album['year']))),
                u"{0}".format(rangement),
                u"{0}".format(str(position))])        
        # create table
        #album_table = Table(table_data, colWidths=[doc.width/6.0]*6)
        album_table = Table(table_data, colWidths=[150.0,430.0,58.0,44.0,58.0,40.0])
        album_table.hAlign = 'LEFT'
        album_table.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.blue),
             ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('BACKGROUND', (0, 0), (-1, 0), colors.yellow)]))
        data.append(album_table)
        
        # create document                   
        doc.build(data, onFirstPage=self.pageNumber, onLaterPages=self.pageNumber)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf
