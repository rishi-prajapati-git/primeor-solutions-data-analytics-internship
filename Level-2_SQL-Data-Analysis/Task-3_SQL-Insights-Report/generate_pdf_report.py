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
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (on page 2)
        if self._pageNumber > 1:
            self.drawString(45, 750, "Primeor Solutions — SQL Data Analysis & Business Intelligence Report")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(45, 742, 567, 742)
            
        # Footer (both pages)
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(567, 30, page_text)
        self.drawString(45, 30, "Confidential — Prepared by Rishi Prajapati (Data Analytics Intern)")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(45, 40, 567, 40)
        self.restoreState()

def generate_pdf():
    pdf_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "Level2_SQL_Business_Insights_Report.pdf"))
    charts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "charts"))
    
    # 0.6 inch margins (43.2 pt)
    doc = SimpleDocTemplate(
        pdf_filename,
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
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=8
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=5
    )
    
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        leftIndent=12,
        spaceAfter=4
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1A202C")
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell,
        fontName='Helvetica-Bold'
    )
    
    story = []
    
    # ---------------- PAGE 1 ----------------
    story.append(Paragraph("E-Commerce SQL Analytics & Business Insights", title_style))
    story.append(Paragraph("Primeor Solutions — Data Analytics Internship | Level 2 Milestone Report<br/><b>Analyst:</b> Rishi Prajapati &nbsp;|&nbsp; <b>Total Transactions:</b> 51,271 &nbsp;|&nbsp; <b>Coverage:</b> Global (2011–2014)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#3182CE"), spaceBefore=0, spaceAfter=8))
    
    story.append(Paragraph("Executive Summary & Core Business Metrics", h1_style))
    exec_text = (
        "This empirical report summarizes relational SQL querying across <b>51,271 transactional records</b>. "
        "Global operations achieved <b>$12,635,222.00</b> in total revenue and <b>$1,467,721.69</b> in net profit (11.62% net margin). "
        "However, excessive frontline discounting resulted in <b>12,534 unprofitable orders (24.45%)</b>, draining <b>-$518,633.91</b> "
        "from enterprise gross margins. Below is the direct synthesis addressing the core internship questions."
    )
    story.append(Paragraph(exec_text, body_style))
    
    story.append(Paragraph("1. Primary Internship Evaluation Questions", h1_style))
    q_data = [
        [Paragraph("Evaluation Question", table_cell_bold), Paragraph("SQL Analytical Finding", table_cell_bold), Paragraph("Leadership Impact & Strategic Action", table_cell_bold)],
        [
            Paragraph("<b>Which market generates highest revenue?</b>", table_cell),
            Paragraph("<b>APAC (Asia-Pacific)</b> is #1 globally with <b>$3,581,785.00</b> (28.35% revenue share) and $437,023.52 profit (12.20% margin). Followed by <b>EU</b> ($2.94M, 23.25%).", table_cell),
            Paragraph("APAC & EU generate over 51.6% of global turnover. Establish localized bulk distribution hubs to improve supply chain velocity.", table_cell)
        ],
        [
            Paragraph("<b>Which categories are least profitable?</b>", table_cell),
            Paragraph("<b>Furniture</b> is the lowest margin category at <b>6.97%</b> ($29 avg profit/order). Specifically, the <b>Tables</b> sub-category produced catastrophic losses of <b>-$64,113.55</b>.", table_cell),
            Paragraph("Impose strict discount caps (max 15%) on Tables and bulky freight items to permanently stop negative unit economics.", table_cell)
        ],
        [
            Paragraph("<b>Which shipping mode is most commonly used?</b>", table_cell),
            Paragraph("<b>Standard Class</b> captures <b>60.00%</b> of all volume (30,764 orders, $7.57M sales volume, $19.96 avg shipping cost).", table_cell),
            Paragraph("Leverage high 60% concentration to negotiate corporate bulk carrier rates, saving an estimated 5–8% on fulfillment costs.", table_cell)
        ]
    ]
    q_table = Table(q_data, colWidths=[130, 195, 197])
    q_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F7FAFC")]),
    ]))
    story.append(q_table)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("2. Global Market Revenue vs. Profit Distribution", h1_style))
    mkt_chart = os.path.join(charts_dir, "market_revenue_profit.png")
    if os.path.exists(mkt_chart):
        story.append(Image(mkt_chart, width=515, height=185))
        
    story.append(PageBreak()) # ---------------- PAGE 2 ----------------
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("3. Root Cause Analysis: Negative Profit Orders & Discount Dilution", h1_style))
    loss_text = (
        "SQL segmentation of loss-making transactions uncovered that unprofitable sales carried an average discount "
        "rate of <b>45.08%</b>, compared to just <b>4.38%</b> on profitable transactions. Discounts exceeding 40% "
        "resulted in an 82%+ likelihood of net financial loss, heavily exacerbated by long-distance logistics surcharges."
    )
    story.append(Paragraph(loss_text, body_style))
    
    loss_data = [
        [Paragraph("Segment Metric", table_cell_bold), Paragraph("Profitable Orders", table_cell_bold), Paragraph("Loss-Making Orders", table_cell_bold), Paragraph("Analytical Insight", table_cell_bold)],
        [Paragraph("Order Count & Share", table_cell), Paragraph("38,737 (75.55%)", table_cell), Paragraph("12,534 (24.45%)", table_cell), Paragraph("Nearly 1 in 4 orders loses money", table_cell)],
        [Paragraph("Cumulative Net Profit ($)", table_cell), Paragraph("+$1,986,355.60", table_cell), Paragraph("-$518,633.91", table_cell), Paragraph("Drains $518.6k from gross margin", table_cell)],
        [Paragraph("Average Applied Discount", table_cell), Paragraph("4.38%", table_cell), Paragraph("45.08%", table_cell), Paragraph("10.3x higher discount on loss orders", table_cell)],
        [Paragraph("Average Shipping Cost", table_cell), Paragraph("$26.21", table_cell), Paragraph("$26.68", table_cell), Paragraph("Fixed logistics amplify deep discount losses", table_cell)],
    ]
    loss_table = Table(loss_data, colWidths=[125, 125, 125, 147])
    loss_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#C53030")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#FFF5F5")]),
    ]))
    story.append(loss_table)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("4. Assortment Profitability & Fulfillment Breakdown", h1_style))
    ship_chart = os.path.join(charts_dir, "ship_mode_distribution.png")
    cat_chart = os.path.join(charts_dir, "category_profit_margin.png")
    if os.path.exists(cat_chart) and os.path.exists(ship_chart):
        chart_table_data = [
            [Image(cat_chart, width=255, height=155), Image(ship_chart, width=255, height=155)]
        ]
        ct = Table(chart_table_data, colWidths=[260, 260])
        ct.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(ct)
        story.append(Spacer(1, 6))
        
    story.append(Paragraph("5. Strategic Recommendations for Business Leadership", h1_style))
    recs = [
        "<b>1. Enforce Hard Discount Ceilings:</b> Cap promotional discounts at 15% on Furniture/Tables. Recovering 25% of current discount leakage adds ~$130k directly to operating profit.",
        "<b>2. VIP Customer Profitability Audit:</b> Large enterprise buyers like Sean Miller ($35k sales, -$397 profit) must be switched to contracted price tiers with minimum 8% margin floors.",
        "<b>3. Q4 Demand Pre-Contracting:</b> Global monthly volume surges by 2.5x between September and December. Lock in advance freight capacity by July to avoid high spot shipping rates.",
        "<b>4. Postal & 3PL Consolidation:</b> With 60% of shipments flowing through Standard Class, negotiating tiered volumetric agreements can yield significant cost reductions."
    ]
    for r in recs:
        story.append(Paragraph(r, bullet_style))
        
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"2-Page Professional PDF Report successfully generated at: {pdf_filename}")

if __name__ == '__main__':
    generate_pdf()
