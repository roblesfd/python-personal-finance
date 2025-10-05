import pytest
from unittest.mock import patch
from repositories.json_category_repo import JsonCategoryRepository

@pytest.fixture
def repo():
    return JsonCategoryRepository()

@pytest.fixture
def sample_categories():
    return [
        {"nombre": "comida"},
        {"nombre": "transporte"},
        {"nombre": "ocio"}
    ]

# ---------- TESTS ----------

@patch("repositories.json_category_repo.load_data")
def test_get_all_returns_data(mock_load, repo, sample_categories):
    mock_load.return_value = sample_categories
    result = repo.get_all()
    assert result == sample_categories
    mock_load.assert_called_once_with("categories.json")

@patch("repositories.json_category_repo.load_data")
def test_get_all_returns_empty_when_none(mock_load, repo):
    mock_load.return_value = None
    result = repo.get_all()
    assert result == []

@patch("repositories.json_category_repo.save_data")
def test_save_calls_save_data_and_returns(mock_save, repo, sample_categories):
    result = repo.save(sample_categories)
    mock_save.assert_called_once_with(sample_categories, "categories.json")
    assert result == sample_categories

@patch.object(JsonCategoryRepository, "get_all")
@patch.object(JsonCategoryRepository, "save")
def test_delete_removes_category(mock_save, mock_get_all, repo, sample_categories):
    mock_get_all.return_value = sample_categories
    result = repo.delete("transporte")
    # Debe eliminar una categoría
    assert len(result) == 2
    assert all(c["nombre"] != "transporte" for c in result)
    mock_save.assert_called_once_with(result)

@patch("repositories.json_category_repo.tabulate", return_value="tabla_mock")
def test_display_prints_table(mock_tabulate, repo, sample_categories, capsys):
    repo.display(sample_categories)
    captured = capsys.readouterr()
    assert "tabla_mock" in captured.out
    mock_tabulate.assert_called_once()
