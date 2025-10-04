from fpdf import FPDF
from datetime import datetime


col_widths = [10, 55, 20, 20, 35, 50] 
pdf = FPDF()
DIR_PATH = "static/"

def export_to_pdf(transactions: list[dict], filename="reporte_movimientos.pdf") -> None:
    """Exporta la lista de transacciones a un archivo pdf

    Args:
        transactions (list[dict]): Lista de transacciones a mostrar
        filename (str, optional): Nombre del archivo a exportar. Defaults to "reporte_movimientos.pdf".
    """

    file_path = DIR_PATH + filename

    if not transactions:
        print("No hay movimientos para exportar.")
        return

    pdf.add_page()
    set_default_font(weight="B", size=14)
    pdf.cell(0, 10, "Reporte de Movimientos", ln=True, align="C")
    pdf.ln(5)

    # Definir headers
    headers = set_headers()

    # Contenido de la tabla
    set_table_content(transactions)

    pdf.output(file_path)

    print(f"✅ PDF generado correctamente: {filename}")


def set_headers() -> list[str] : 
    """Define los nombres de columnas en el encabezado de la tabla

    Returns:
        list[str]: Lista de headers para la tabla
    """

    headers = ["No.", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]
    set_default_font()

    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 8, header, border=1, align="C")
    pdf.ln()

    return headers


def set_table_content(transactions: list[dict])  -> None:
    """Define el contenido (transactions) de la tabla con filas y columnas 

    Args:
        transactions (list[dict]): Lista de transacciones a mostrar
    """

    set_default_font()    
    # filas
    for i, t in enumerate(transactions):
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


def set_default_font(style="Arial", weight="", size=11) -> None:
    """Define opciones de fuente predeterminada para la tabla

    Args:
        style (str, optional): Estilo de fuente. Defaults to "Arial".
        weight (str, optional): Peso de la fuente. Defaults to "".
        size (int, optional): Tamaño de la fuente. Defaults to 11.
    """
    
    pdf.set_font(style, weight, size)
