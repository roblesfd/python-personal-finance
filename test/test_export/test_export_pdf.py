import pytest
from unittest.mock import patch 

from export.export_pdf import export_to_pdf


def test_exports_with_data():
    fake_transactions = [
        {"fecha": "2025-09-25", "tipo": "ingreso", "monto": 100, "categoria": "sueldo", "descripcion": "Pago"},
        {"fecha": "2025-09-26", "tipo": "gasto", "monto": 50, "categoria": "comida", "descripcion": "Cena"},
    ]

    with patch("export.export_pdf.export_to_pdf"), \
        patch("builtins.print") as mock_print:

        filename = "fake_movimientos.pdf"
        result = export_to_pdf(fake_transactions, filename)

        mock_print.assert_any_call(f"✅ PDF generado correctamente: {filename}")


def test_no_data_to_export():

    with patch("export.export_pdf.pdf.output") as mock_output, \
        patch("builtins.print") as mock_print:

        result = export_to_pdf([], filename="test.pdf")

        mock_output.assert_not_called()
        mock_print.assert_any_call("No hay movimientos para exportar.")
