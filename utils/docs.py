import webbrowser
from importlib.resources import files 

def open_docs():
    """Abre la documentación HTML del paquete en el navegador."""
    index_path = files("personal_finance").joinpath("docs/index.html")
    webbrowser.open(f"file://{index_path}")
