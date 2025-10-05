import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from repositories.json_transaction_repo import JsonTransactionRepository

@pytest.fixture
def repo():
    return JsonTransactionRepository()

@pytest.fixture
def sample_transactions():
    return [
        {
            "fecha": "2025-10-01T12:00:00",
            "tipo": "ingreso",
            "monto": 1000,
            "categoria": "ventas",
            "descripcion": "venta producto"
        },
        {
            "fecha": "2025-10-02T10:00:00",
            "tipo": "gasto",
            "monto": 200,
            "categoria": "compras",
            "descripcion": "compra insumo"
        }
    ]

# ---------- TESTS ----------

@patch("repositories.json_transaction_repo.load_data")
def test_get_all_returns_transactions(mock_load, repo, sample_transactions):
    mock_load.return_value = sample_transactions
    result = repo.get_all()
    assert len(result) == 2
    assert result[0]["tipo"] == "ingreso"

@patch("repositories.json_transaction_repo.load_data")
def test_get_all_empty_prints_message(mock_load, repo, capsys):
    mock_load.return_value = []
    repo.get_all()
    captured = capsys.readouterr()
    assert "No hay movimientos" in captured.out

@patch("repositories.json_transaction_repo.save_data")
@patch("repositories.json_transaction_repo.json_cat_repo")
def test_save_calls_save_data_and_category_repo(mock_cat_repo, mock_save_data, repo, sample_transactions):
    repo.save(sample_transactions)
    mock_cat_repo.save.assert_called_once_with("compras")
    mock_save_data.assert_called_once_with(sample_transactions, "data.json")

def test_calculate_balance(repo, sample_transactions):
    balance = repo.calculate_balance(sample_transactions)
    assert balance == 800  # 1000 ingreso - 200 gasto

def test_filter_by_category(repo, sample_transactions):
    result = repo.filter_by_category(sample_transactions, "ventas")
    assert len(result) == 1
    assert result[0]["categoria"] == "ventas"

def test_filter_by_type(repo, sample_transactions):
    result = repo.filter_by_type(sample_transactions, "gasto")
    assert len(result) == 1
    assert result[0]["tipo"] == "gasto"

def test_filter_by_date(repo, sample_transactions):
    start = datetime(2025, 10, 1)
    end = datetime(2025, 10, 1, 23, 59)
    result = repo.filter_by_date(sample_transactions, start, end)
    assert len(result) == 1
    assert result[0]["fecha"].startswith("2025-10-01")
