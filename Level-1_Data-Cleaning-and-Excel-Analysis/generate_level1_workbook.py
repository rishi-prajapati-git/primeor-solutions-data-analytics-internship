"""
Automated professional Excel Workbook generator for Primeor Solutions Internship Project.
Creates 'Ecommerce_Analysis_Level1.xlsx' with:
1. 'Project Overview' - Executive Summary & project metadata
2. 'Cleaned Dataset' - Complete 51,271 records with formatted headers & data
3. 'Basic Excel Analysis' - Task 2 KPI cards and analysis tables with native Excel formulas
4. 'Pivots & Visuals' - Task 3 Pivot Summary Tables with embedded high-resolution visual charts
"""

import os
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image

def generate_excel_workbook():
    csv_path = os.path.join('dataset', 'cleaned', 'cleaned_ecommerce_dataset.csv')
    excel_path = os.path.join('Level-1_Data-Cleaning-and-Excel-Analysis', 'Ecommerce_Analysis_Level1.xlsx')
    charts_dir = os.path.join('Level-1_Data-Cleaning-and-Excel-Analysis', 'Task-3_Pivot-Tables-and-Charts', 'charts')

    print("Loading cleaned dataset...")
    df = pd.read_csv(csv_path)
    total_rows = len(df)
    print(f"Loaded {total_rows} rows.")

    wb = openpyxl.Workbook()

    # Define design styles
    header_font = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
    header_fill = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid') # Navy Blue
    title_font = Font(name='Segoe UI', size=16, bold=True, color='1F4E79')
    subtitle_font = Font(name='Segoe UI', size=11, italic=True, color='595959')
    kpi_title_font = Font(name='Segoe UI', size=10, bold=True, color='595959')
    kpi_value_font = Font(name='Segoe UI', size=18, bold=True, color='1F4E79')
    kpi_fill = PatternFill(start_color='EBF1F5', end_color='EBF1F5', fill_type='solid')
    sub_header_fill = PatternFill(start_color='2F5597', end_color='2F5597', fill_type='solid')
    zebra_fill = PatternFill(start_color='F9FAFB', end_color='F9FAFB', fill_type='solid')

    thin_border_side = Side(border_style='thin', color='D9D9D9')
    thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    thick_bottom = Border(bottom=Side(border_style='medium', color='1F4E79'))

    # ==========================================
    # SHEET 1: PROJECT OVERVIEW
    # ==========================================
    ws_intro = wb.active
    ws_intro.title = 'Project Overview'
    ws_intro.views.sheetView[0].showGridLines = True

    ws_intro['B2'] = "PRIMEOR SOLUTIONS - DATA ANALYTICS INTERNSHIP"
    ws_intro['B2'].font = Font(name='Segoe UI', size=18, bold=True, color='1F4E79')
    ws_intro['B3'] = "E-Commerce Global Sales & Profitability Analysis Workbook"
    ws_intro['B3'].font = subtitle_font

    info_data = [
        ("Candidate Name", "Rishi Prajapati"),
        ("Project Scope", "Level 1: Data Understanding, Cleaning & Excel Analysis"),
        ("Dataset", "Global E-Commerce Sales Transactions (2011 - 2014)"),
        ("Cleaned Records", f"{total_rows:,} transactions (Deduplicated & Cleaned)"),
        ("Key Tools Used", "Microsoft Excel, Python (pandas, openpyxl, seaborn)"),
        ("Submission Date", "November 2026")
    ]
    ws_intro['B5'] = "PROJECT METADATA"
    ws_intro['B5'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')

    for idx, (label, val) in enumerate(info_data, start=6):
        ws_intro[f'B{idx}'] = label
        ws_intro[f'B{idx}'].font = Font(name='Segoe UI', size=11, bold=True)
        ws_intro[f'C{idx}'] = val
        ws_intro[f'C{idx}'].font = Font(name='Segoe UI', size=11)
        ws_intro[f'B{idx}'].border = thin_border
        ws_intro[f'C{idx}'].border = thin_border

    # Navigation summary
    ws_intro['B14'] = "WORKBOOK STRUCTURE & SHEET GUIDE"
    ws_intro['B14'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')
    sheet_guide = [
        ("Cleaned Dataset", "Fully cleansed and standardized raw transactional dataset (51,271 records)."),
        ("Basic Excel Analysis", "Executive KPIs (Total Sales, Profit, Avg Discount) and Top/Bottom performing tables using native Excel formulas."),
        ("Pivots & Visuals", "Pivot summary aggregation tables (Region, Category, Segment, Monthly Trend) with integrated visualizations.")
    ]
    ws_intro['B15'] = "Sheet Name"
    ws_intro['C15'] = "Contents & Tasks Covered"
    ws_intro['B15'].font = header_font
    ws_intro['B15'].fill = header_fill
    ws_intro['C15'].font = header_font
    ws_intro['C15'].fill = header_fill

    for idx, (sname, desc) in enumerate(sheet_guide, start=16):
        ws_intro[f'B{idx}'] = sname
        ws_intro[f'B{idx}'].font = Font(name='Segoe UI', size=11, bold=True)
        ws_intro[f'C{idx}'] = desc
        ws_intro[f'C{idx}'].font = Font(name='Segoe UI', size=11)
        ws_intro[f'B{idx}'].border = thin_border
        ws_intro[f'C{idx}'].border = thin_border

    ws_intro.column_dimensions['B'].width = 25
    ws_intro.column_dimensions['C'].width = 80

    # ==========================================
    # SHEET 2: CLEANED DATASET
    # ==========================================
    print("Writing Cleaned Dataset sheet (51,271 rows)...")
    ws_data = wb.create_sheet('Cleaned Dataset')
    ws_data.views.sheetView[0].showGridLines = True

    # Header
    for c_idx, col_name in enumerate(df.columns, start=1):
        cell = ws_data.cell(row=1, column=c_idx, value=col_name)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')

    # Data
    data_values = df.values.tolist()
    for r_idx, row_data in enumerate(data_values, start=2):
        for c_idx, val in enumerate(row_data, start=1):
            cell = ws_data.cell(row=r_idx, column=c_idx, value=val)
            if c_idx in [15, 18, 19]: # sales, profit, shipping_cost
                cell.number_format = '$#,##0.00'
            elif c_idx == 17: # discount
                cell.number_format = '0.00%'

    for col in ws_data.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(col[0].value or '')), 12)
        ws_data.column_dimensions[col_letter].width = min(max_len + 4, 32)

    # ==========================================
    # SHEET 3: BASIC EXCEL ANALYSIS (TASK 2)
    # ==========================================
    print("Building Basic Excel Analysis sheet with formulas...")
    ws_analysis = wb.create_sheet('Basic Excel Analysis')
    ws_analysis.views.sheetView[0].showGridLines = True

    ws_analysis['B2'] = "LEVEL 1 TASK 2: BASIC EXCEL ANALYSIS"
    ws_analysis['B2'].font = title_font
    ws_analysis['B3'] = "Executive KPIs and Performance Rankings dynamically linked via Excel formulas"
    ws_analysis['B3'].font = subtitle_font

    # KPI 1: Total Sales
    ws_analysis.merge_cells('B5:D5')
    ws_analysis['B5'] = "TOTAL SALES"
    ws_analysis['B5'].font = kpi_title_font
    ws_analysis['B5'].alignment = Alignment(horizontal='center')
    ws_analysis['B5'].fill = kpi_fill
    ws_analysis.merge_cells('B6:D6')
    ws_analysis['B6'] = f"=SUM('Cleaned Dataset'!O2:O{total_rows+1})"
    ws_analysis['B6'].font = kpi_value_font
    ws_analysis['B6'].alignment = Alignment(horizontal='center')
    ws_analysis['B6'].number_format = '$#,##0.00'
    ws_analysis['B6'].fill = kpi_fill

    # KPI 2: Total Profit
    ws_analysis.merge_cells('F5:H5')
    ws_analysis['F5'] = "TOTAL PROFIT"
    ws_analysis['F5'].font = kpi_title_font
    ws_analysis['F5'].alignment = Alignment(horizontal='center')
    ws_analysis['F5'].fill = kpi_fill
    ws_analysis.merge_cells('F6:H6')
    ws_analysis['F6'] = f"=SUM('Cleaned Dataset'!R2:R{total_rows+1})"
    ws_analysis['F6'].font = kpi_value_font
    ws_analysis['F6'].alignment = Alignment(horizontal='center')
    ws_analysis['F6'].number_format = '$#,##0.00'
    ws_analysis['F6'].fill = kpi_fill

    # KPI 3: Average Discount
    ws_analysis.merge_cells('J5:L5')
    ws_analysis['J5'] = "AVERAGE DISCOUNT"
    ws_analysis['J5'].font = kpi_title_font
    ws_analysis['J5'].alignment = Alignment(horizontal='center')
    ws_analysis['J5'].fill = kpi_fill
    ws_analysis.merge_cells('J6:L6')
    ws_analysis['J6'] = f"=AVERAGE('Cleaned Dataset'!Q2:Q{total_rows+1})"
    ws_analysis['J6'].font = kpi_value_font
    ws_analysis['J6'].alignment = Alignment(horizontal='center')
    ws_analysis['J6'].number_format = '0.00%'
    ws_analysis['J6'].fill = kpi_fill

    # Top 5 Products by Sales
    ws_analysis['B9'] = "TOP 5 PRODUCTS BY SALES"
    ws_analysis['B9'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')
    top_sales_headers = ["Rank", "Product Name", "Total Sales ($)"]
    for c_i, h in enumerate(top_sales_headers, start=2):
        cell = ws_analysis.cell(row=10, column=c_i, value=h)
        cell.font = header_font
        cell.fill = sub_header_fill
        cell.alignment = Alignment(horizontal='center')

    top_5_sales = df.groupby('product_name')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(5)
    for idx, row in enumerate(top_5_sales.itertuples(), start=1):
        r = 10 + idx
        ws_analysis.cell(row=r, column=2, value=idx).alignment = Alignment(horizontal='center')
        ws_analysis.cell(row=r, column=3, value=row.product_name)
        c_val = ws_analysis.cell(row=r, column=4, value=row.sales)
        c_val.number_format = '$#,##0.00'
        for col_i in range(2, 5):
            ws_analysis.cell(row=r, column=col_i).border = thin_border

    # Top 5 Loss-Making Products
    ws_analysis['F9'] = "TOP 5 LOSS-MAKING PRODUCTS"
    ws_analysis['F9'].font = Font(name='Segoe UI', size=12, bold=True, color='C00000')
    top_loss_headers = ["Rank", "Product Name", "Total Net Loss ($)"]
    for c_i, h in enumerate(top_loss_headers, start=6):
        cell = ws_analysis.cell(row=10, column=c_i, value=h)
        cell.font = header_font
        cell.fill = PatternFill(start_color='C00000', end_color='C00000', fill_type='solid')
        cell.alignment = Alignment(horizontal='center')

    top_5_loss = df.groupby('product_name')['profit'].sum().reset_index().sort_values(by='profit', ascending=True).head(5)
    for idx, row in enumerate(top_5_loss.itertuples(), start=1):
        r = 10 + idx
        ws_analysis.cell(row=r, column=6, value=idx).alignment = Alignment(horizontal='center')
        ws_analysis.cell(row=r, column=7, value=row.product_name)
        c_val = ws_analysis.cell(row=r, column=8, value=row.profit)
        c_val.number_format = '$#,##0.00'
        for col_i in range(6, 9):
            ws_analysis.cell(row=r, column=col_i).border = thin_border

    # Region-wise Sales Analysis
    ws_analysis['B18'] = "REGION-WISE SALES ANALYSIS"
    ws_analysis['B18'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')
    reg_headers = ["Region", "Total Sales ($)", "Sales Contribution (%)"]
    for c_i, h in enumerate(reg_headers, start=2):
        cell = ws_analysis.cell(row=19, column=c_i, value=h)
        cell.font = header_font
        cell.fill = sub_header_fill
        cell.alignment = Alignment(horizontal='center')

    region_sales = df.groupby('region')['sales'].sum().reset_index().sort_values(by='sales', ascending=False)
    for idx, row in enumerate(region_sales.itertuples(), start=1):
        r = 19 + idx
        ws_analysis.cell(row=r, column=2, value=row.region)
        c_sales = ws_analysis.cell(row=r, column=3, value=row.sales)
        c_sales.number_format = '$#,##0.00'
        c_pct = ws_analysis.cell(row=r, column=4, value=f"=C{r}/$B$6")
        c_pct.number_format = '0.00%'
        for col_i in range(2, 5):
            ws_analysis.cell(row=r, column=col_i).border = thin_border

    # Total row for Region-wise sales
    tot_row = 19 + len(region_sales) + 1
    ws_analysis.cell(row=tot_row, column=2, value="Grand Total").font = Font(name='Segoe UI', size=11, bold=True)
    c_tot_s = ws_analysis.cell(row=tot_row, column=3, value=f"=SUM(C20:C{tot_row-1})")
    c_tot_s.font = Font(name='Segoe UI', size=11, bold=True)
    c_tot_s.number_format = '$#,##0.00'
    c_tot_p = ws_analysis.cell(row=tot_row, column=4, value=f"=SUM(D20:D{tot_row-1})")
    c_tot_p.font = Font(name='Segoe UI', size=11, bold=True)
    c_tot_p.number_format = '0.00%'
    for col_i in range(2, 5):
        ws_analysis.cell(row=tot_row, column=col_i).border = thick_bottom

    ws_analysis.column_dimensions['B'].width = 18
    ws_analysis.column_dimensions['C'].width = 38
    ws_analysis.column_dimensions['D'].width = 24
    ws_analysis.column_dimensions['E'].width = 5
    ws_analysis.column_dimensions['F'].width = 18
    ws_analysis.column_dimensions['G'].width = 44
    ws_analysis.column_dimensions['H'].width = 24

    # ==========================================
    # SHEET 4: PIVOTS & CHARTS (TASK 3)
    # ==========================================
    print("Building Pivots & Charts sheet...")
    ws_pivots = wb.create_sheet('Pivots & Visuals')
    ws_pivots.views.sheetView[0].showGridLines = True

    ws_pivots['B2'] = "LEVEL 1 TASK 3: PIVOT TABLES & VISUAL CHARTS"
    ws_pivots['B2'].font = title_font
    ws_pivots['B3'] = "Aggregated Business Summary Tables and Visual Charts"
    ws_pivots['B3'].font = subtitle_font

    # Table 1: Category Profit Summary
    ws_pivots['B5'] = "PROFIT BY CATEGORY"
    ws_pivots['B5'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')
    cat_headers = ["Category", "Total Sales ($)", "Total Profit ($)", "Profit Margin"]
    for c_i, h in enumerate(cat_headers, start=2):
        cell = ws_pivots.cell(row=6, column=c_i, value=h)
        cell.font = header_font
        cell.fill = sub_header_fill
        cell.alignment = Alignment(horizontal='center')

    cat_df = df.groupby('category').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values(by='profit', ascending=False)
    for idx, row in enumerate(cat_df.itertuples(), start=1):
        r = 6 + idx
        ws_pivots.cell(row=r, column=2, value=row.category)
        c_s = ws_pivots.cell(row=r, column=3, value=row.sales)
        c_s.number_format = '$#,##0.00'
        c_p = ws_pivots.cell(row=r, column=4, value=row.profit)
        c_p.number_format = '$#,##0.00'
        c_m = ws_pivots.cell(row=r, column=5, value=f"=D{r}/C{r}")
        c_m.number_format = '0.00%'
        for col_i in range(2, 6):
            ws_pivots.cell(row=r, column=col_i).border = thin_border

    # Table 2: Segment-wise Sales Analysis
    ws_pivots['B12'] = "SEGMENT-WISE SALES & PROFIT"
    ws_pivots['B12'].font = Font(name='Segoe UI', size=12, bold=True, color='1F4E79')
    seg_headers = ["Customer Segment", "Total Sales ($)", "Total Profit ($)", "Sales Share"]
    for c_i, h in enumerate(seg_headers, start=2):
        cell = ws_pivots.cell(row=13, column=c_i, value=h)
        cell.font = header_font
        cell.fill = sub_header_fill
        cell.alignment = Alignment(horizontal='center')

    seg_df = df.groupby('segment').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values(by='sales', ascending=False)
    for idx, row in enumerate(seg_df.itertuples(), start=1):
        r = 13 + idx
        ws_pivots.cell(row=r, column=2, value=row.segment)
        c_s = ws_pivots.cell(row=r, column=3, value=row.sales)
        c_s.number_format = '$#,##0.00'
        c_p = ws_pivots.cell(row=r, column=4, value=row.profit)
        c_p.number_format = '$#,##0.00'
        c_m = ws_pivots.cell(row=r, column=5, value=f"=C{r}/'Basic Excel Analysis'!$B$6")
        c_m.number_format = '0.00%'
        for col_i in range(2, 6):
            ws_pivots.cell(row=r, column=col_i).border = thin_border

    # Embed charts into sheet
    img_region = Image(os.path.join(charts_dir, 'sales_by_region.png'))
    img_region.width = 480
    img_region.height = 300
    ws_pivots.add_image(img_region, 'G5')

    img_category = Image(os.path.join(charts_dir, 'profit_by_category.png'))
    img_category.width = 460
    img_category.height = 290
    ws_pivots.add_image(img_category, 'B19')

    img_segment = Image(os.path.join(charts_dir, 'segment_wise_sales.png'))
    img_segment.width = 380
    img_segment.height = 360
    ws_pivots.add_image(img_segment, 'G19')

    img_trend = Image(os.path.join(charts_dir, 'monthly_sales_trend.png'))
    img_trend.width = 860
    img_trend.height = 320
    ws_pivots.add_image(img_trend, 'B37')

    ws_pivots.column_dimensions['B'].width = 24
    ws_pivots.column_dimensions['C'].width = 20
    ws_pivots.column_dimensions['D'].width = 20
    ws_pivots.column_dimensions['E'].width = 18

    # Save complete workbook
    print("Saving complete formatted Excel workbook...")
    wb.save(excel_path)
    print(f"Excel workbook successfully generated and saved to: {excel_path}")

if __name__ == '__main__':
    generate_excel_workbook()
