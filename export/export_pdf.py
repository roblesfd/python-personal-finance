from fpdf import FPDF
from datetime import datetime


col_widths = [10, 55, 20, 20, 35, 50] 
pdf = FPDF()
DIR_PATH = "static/"

def export_to_pdf(data, filename="reporte_movimientos.pdf"):
    file_path = DIR_PATH + filename

    if not data:
        print("No hay movimientos para exportar.")
        return

    pdf.add_page()
    set_default_font(weight="B", size=14)
    pdf.cell(0, 10, "Reporte de Movimientos", ln=True, align="C")
    pdf.ln(5)

    # Definir headers
    headers = set_headers()

    # Contenido de la tabla
    set_table_content(data)

    pdf.output(file_path)

    print(f"✅ PDF generado correctamente: {filename}")


def set_headers():
    headers = ["No.", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]
    set_default_font()

    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 8, header, border=1, align="C")
    pdf.ln()

    return headers


def set_table_content(data):
    set_default_font()    
    # filas
    for i, t in enumerate(data):
        row = [
            str(i+1),
            t["fecha"],
            t["tipo"],
            f"{t['monto']:.2f}",
            t["categoria"],
            t["descripcion"]
        ]
        # celdas
        for j, cell in enumerate(row):
            pdf.cell(col_widths[j], 8, cell, border=1)
        pdf.ln()


def set_default_font(style="Arial", weight="", size=11):
    pdf.set_font(style, weight, size)
