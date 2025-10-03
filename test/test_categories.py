import pytest 
from unittest.mock import patch, MagicMock
from repositories.categories import add_category, display_categories, get_categories, delete_category


def test_add_category_with_data():
    fake_categories = [{"nombre": "transporte"}]
    expected = [{"nombre": "transporte"}, {"nombre": "alimentos"}]

    with patch("repositories.categories.load_data", return_value=fake_categories), \
        patch("repositories.categories.save_data") as mock_save:

        result = add_category("alimentos")

        mock_save.assert_called_once_with(expected, "categories.json")
        assert result == expected


def test_add_category_no_data(capsys):

    with patch("repositories.categories.load_data", return_value=[]):
        result = add_category("alimentos")
        captured = capsys.readouterr()
        assert "📭 No hay categorias registradas." in captured.out
        assert result is None


def test_display_categories(capsys):
    fake_categories = [{"nombre": "Alimentos"}, {"nombre": "Transporte"}]

    display_categories(fake_categories)
    captured = capsys.readouterr()
    assert "Alimentos" in captured.out
    assert "Transporte" in captured.out


def test_get_categories_with_data():
    fake_categories = [{"nombre": "Ocio"}]

    with patch("repositories.categories.load_data", return_value=fake_categories):
        result = get_categories()
        assert result == fake_categories


def test_get_categories_no_data(capsys):
    with patch("repositories.categories.load_data", return_value=[]):
        result = get_categories()
        captured = capsys.readouterr()
        assert "📭 No hay categorias registradas." in captured.out
        assert result is None


def test_delete_category_success():
    fake_categories = [{"nombre": "Alimentos"}, {"nombre": "Transporte"}]
    expected = [{"nombre": "Transporte"}]

    with patch("repositories.categories.load_data", return_value=fake_categories), \
         patch("repositories.categories.save_data") as mock_save:

        result = delete_category("Alimentos")

        mock_save.assert_called_once_with(expected, "categories.json")
        assert result == expected


def test_delete_category_no_data(capsys):
    with patch("repositories.categories.load_data", return_value=[]):
        result = delete_category("Alimentos")
        captured = capsys.readouterr()
        assert "📭 No hay categorias para eliminar." in captured.out
        assert result is None


def test_delete_category_not_found(capsys):
    fake_categories = [{"nombre": "Transporte"}]

    with patch("repositories.categories.load_data", return_value=fake_categories):
        result = delete_category("Alimentos")
        captured = capsys.readouterr()
        assert "No existe una categoria con el nombre Alimentos" in captured.out
        assert result is None