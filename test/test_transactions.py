import pytest

from unittest.mock import patch 
from datetime import datetime, timedelta

from transaction.transactions import add_transaction, display_transactions, get_transactions, calculate_balance, filter_by_category, filter_by_type, filter_by_date


def test_add_transaction():
    fake_transaction = {
        "fecha": "2025-09-25T12:00:00",
        "tipo": "ingreso",
        "monto": 100,
        "categoria": "sueldo",
        "descripcion": "Pago mensual"
    }

    with patch("transaction.transactions.get_transactions", return_value=[]), \
        patch("transaction.transactions.save_data") as mock_save, \
        patch("builtins.print") as mock_print:

        add_transaction(fake_transaction)

        mock_save.assert_called_once_with([fake_transaction], 'data.json')
        mock_print.assert_any_call("✅ Movimiento registrado correctamente.", fake_transaction)


def test_display_transactions():
    fake_transactions = [
        {"fecha": "2025-09-25", "tipo": "ingreso", "monto": 100, "categoria": "sueldo", "descripcion": "Pago"},
        {"fecha": "2025-09-26", "tipo": "gasto", "monto": 50, "categoria": "comida", "descripcion": "Cena"},
    ]

    with patch("builtins.print") as mock_print:
        display_transactions(fake_transactions)
        
        assert mock_print.call_count == 1


def test_get_transactions_with_data():
    fake_data = [{"tipo": "ingreso", "monto": 100}]

    with patch("transaction.transactions.load_data", return_value=fake_data):
        result = get_transactions()
        assert result == fake_data


def test_get_transactions_no_data():
    with patch("transaction.transactions.load_data", return_value=[]), \
         patch("builtins.print") as mock_print:
        result = get_transactions()
        assert result is None
        mock_print.assert_any_call("📭 No hay movimientos registrados.")


def test_calculate_balance():
    fake_transactions = [
        {"tipo": "ingreso", "monto": 100},
        {"tipo": "gasto", "monto": 40},
    ]
    result = calculate_balance(fake_transactions)
    assert result == 60


def test_filter_by_category():
    fake_transactions = [
        {"categoria": "sueldo"},
        {"categoria": "comida"},
    ]
    result = filter_by_category(fake_transactions, "sueldo")
    assert len(result) == 1
    assert result[0]["categoria"] == "sueldo"


def test_filter_by_type():
    fake_transactions = [
        {"tipo": "ingreso"},
        {"tipo": "gasto"},
    ]
    result = filter_by_type(fake_transactions, "gasto")
    assert len(result) == 1
    assert result[0]["tipo"] == "gasto"


def test_filter_by_date():
    today = datetime.now()
    fake_transactions = [
        {"fecha": (today - timedelta(days=1)).isoformat(), "tipo": "ingreso"},
        {"fecha": (today + timedelta(days=1)).isoformat(), "tipo": "gasto"},
    ]
    start = today - timedelta(days=2)
    end = today

    result = filter_by_date(fake_transactions, start, end)
    assert len(result) == 1