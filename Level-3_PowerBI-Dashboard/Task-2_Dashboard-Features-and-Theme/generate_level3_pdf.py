import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (on pages > 1)
        if self._pageNumber > 1:
            self.drawString(45, 752, "Primeor Solutions — Executive Power BI Dashboard Architecture & Business Insights")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(45, 745, 567, 745)
            
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(567, 28, page_text)
        self.drawString(45, 28, "Confidential — Prepared by Rishi Prajapati (Data Analytics Intern)")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(45, 38, 567, 38)
        self.restoreState()

def generate_dashboard_pdf():
    pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Level3_PowerBI_Dashboard_Report.pdf"))
    mockups_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../dashboard_mockups"))
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=45
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0B132B"),
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=8
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=6,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=4
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#1A202C")
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # ---------------- PAGE 1: EXECUTIVE OVERVIEW ----------------
    story.append(Paragraph("Power BI Interactive Dashboard Architecture", title_style))
    story.append(Paragraph("Primeor Solutions — Data Analytics Internship | Level 3 Milestone Report<br/><b>Analyst:</b> Rishi Prajapati &nbsp;|&nbsp; <b>Tools:</b> Power BI Desktop / DAX / Power Query &nbsp;|&nbsp; <b>Dataset:</b> 51,271 Records", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#3182CE"), spaceBefore=0, spaceAfter=6))
    
    story.append(Paragraph("Page 1: Executive KPI Overview", h1_style))
    p1_desc = (
        "Designed for senior leadership, Page 1 delivers high-level visibility across core metrics: "
        "<b>Total Sales ($12.64M)</b>, <b>Total Profit ($1.47M, 11.6% margin)</b>, <b>Total Orders (51,271)</b>, and <b>Average Discount (14.29%)</b>. "
        "Dynamic slicers allow cross-filtering by Year (2011–2014), Market Region, and Product Category."
    )
    story.append(Paragraph(p1_desc, body_style))
    
    p1_img = os.path.join(mockups_dir, "Page-1_Executive-Overview.png")
    if os.path.exists(p1_img):
        story.append(Image(p1_img, width=520, height=260))
        story.append(Spacer(1, 4))
        
    # KPI Breakdown Table
    kpi_data = [
        [Paragraph("Executive KPI", table_cell_bold), Paragraph("Value", table_cell_bold), Paragraph("Underlying DAX Formula", table_cell_bold), Paragraph("Business Interpretation", table_cell_bold)],
        [Paragraph("Total Sales", table_cell), Paragraph("<b>$12,635,222.00</b>", table_cell), Paragraph("<code>SUM(sales)</code>", table_cell), Paragraph("Aggregate global gross transactional revenue", table_cell)],
        [Paragraph("Total Profit", table_cell), Paragraph("<b>$1,467,721.69</b>", table_cell), Paragraph("<code>SUM(profit)</code>", table_cell), Paragraph("Healthy enterprise-wide net profit margin of 11.62%", table_cell)],
        [Paragraph("Total Orders", table_cell), Paragraph("<b>51,271</b>", table_cell), Paragraph("<code>DISTINCTCOUNT(order_id)</code>", table_cell), Paragraph("Total valid commercial transactions processed", table_cell)],
        [Paragraph("Average Discount", table_cell), Paragraph("<b>14.29%</b>", table_cell), Paragraph("<code>AVERAGE(discount)</code>", table_cell), Paragraph("Benchmark discount rate across catalog offerings", table_cell)]
    ]
    t1 = Table(kpi_data, colWidths=[90, 80, 160, 190])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
    ]))
    story.append(t1)
    
    story.append(PageBreak()) # ---------------- PAGE 2: SALES ANALYSIS ----------------
    
    story.append(Paragraph("Page 2: Sales & Geographic Trend Analysis", h1_style))
    p2_desc = (
        "Page 2 enables regional directors to evaluate commercial trends across 13 regions and 7 international markets. "
        "The monthly time-series visual highlights recurring Q4 seasonality (September through December peak), while category "
        "performance confirms Technology leads net profitability ($663k profit) over Furniture ($286k profit)."
    )
    story.append(Paragraph(p2_desc, body_style))
    
    p2_img = os.path.join(mockups_dir, "Page-2_Sales-Analysis.png")
    if os.path.exists(p2_img):
        story.append(Image(p2_img, width=520, height=270))
        story.append(Spacer(1, 6))
        
    # Regional summary table
    reg_data = [
        [Paragraph("Primary Market", table_cell_bold), Paragraph("Revenue ($M)", table_cell_bold), Paragraph("Profit ($k)", table_cell_bold), Paragraph("Margin %", table_cell_bold), Paragraph("Operational Evaluation", table_cell_bold)],
        [Paragraph("APAC", table_cell), Paragraph("$3.58M", table_cell), Paragraph("$437.0k", table_cell), Paragraph("12.20%", table_cell), Paragraph("Global revenue leader; core expansion driver", table_cell)],
        [Paragraph("EU", table_cell), Paragraph("$2.94M", table_cell), Paragraph("$372.9k", table_cell), Paragraph("12.70%", table_cell), Paragraph("High margin stability across Western Europe", table_cell)],
        [Paragraph("US", table_cell), Paragraph("$2.30M", table_cell), Paragraph("$286.0k", table_cell), Paragraph("12.45%", table_cell), Paragraph("Steady commercial volume in domestic accounts", table_cell)],
        [Paragraph("LATAM", table_cell), Paragraph("$2.16M", table_cell), Paragraph("$221.3k", table_cell), Paragraph("10.23%", table_cell), Paragraph("Rapid growth with moderate discount dilution", table_cell)]
    ]
    t2 = Table(reg_data, colWidths=[90, 80, 80, 70, 200])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A365D")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
    ]))
    story.append(t2)
    
    story.append(PageBreak()) # ---------------- PAGE 3: PRODUCT & CUSTOMER INSIGHTS ----------------
    
    story.append(Paragraph("Page 3: Assortment Profitability & Key Customer Accounts", h1_style))
    p3_desc = (
        "Page 3 equips category managers to pinpoint margin leakages. The diverging sub-category chart reveals that while "
        "Copiers ($258k profit) and Phones ($217k profit) drive earnings, Tables incurred severe negative losses of <b>-$64,113.55</b>. "
        "Top customer analysis highlights high-value accounts alongside margin-diluting buyers requiring commercial contract renegotiation."
    )
    story.append(Paragraph(p3_desc, body_style))
    
    p3_img = os.path.join(mockups_dir, "Page-3_Product-and-Customer-Insights.png")
    if os.path.exists(p3_img):
        story.append(Image(p3_img, width=520, height=270))
        story.append(Spacer(1, 6))
        
    # Recommendations Table
    rec_data = [
        [Paragraph("Strategic Pillar", table_cell_bold), Paragraph("Observed Vulnerability", table_cell_bold), Paragraph("Dashboard Interactive Action", table_cell_bold)],
        [
            Paragraph("<b>Furniture Margin Repair</b>", table_cell),
            Paragraph("Tables sub-category generated -$64,113.55 net loss due to discounts > 35%.", table_cell),
            Paragraph("Filter by Furniture > Tables on Page 3 to isolate unprofitable country-level distributor contracts.", table_cell)
        ],
        [
            Paragraph("<b>High-Value Account Auditing</b>", table_cell),
            Paragraph("Customer Sean Miller generated $35k sales but -$397 net loss due to high discounts.", table_cell),
            Paragraph("Cross-filter customer accounts on Page 3 to view order-level margin distribution and enforce pricing floors.", table_cell)
        ],
        [
            Paragraph("<b>Q4 Seasonal Logistics</b>", table_cell),
            Paragraph("Sales spike 2.5x from September to December, straining standard fulfillment.", table_cell),
            Paragraph("Drill down into Monthly Trend on Page 2 to forecast carrier capacity and prevent expedited shipping surcharges.", table_cell)
        ]
    ]
    t3 = Table(rec_data, colWidths=[120, 190, 210])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7209B7")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
    ]))
    story.append(t3)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Level 3 Power BI PDF Report successfully created at: {pdf_path}")

if __name__ == '__main__':
    generate_dashboard_pdf()
