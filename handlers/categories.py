from repositories.categories import add_category, display_categories, get_categories, delete_category
from repositories.base_category_repo import CategoryRepository

class CategoryHandler:

    def __init__(self, repo: CategoryRepository):
        self.repo = repo


    def handle_list(self, args):
        """Handler para comando listcat

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        categories = self.repo.get_all()
        return categories

    def handle_delete(self, args):
        """Handler para comando deletecat

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        updated_categories = self.repo.delete(args.category)
        print(f"Se ha eliminado la categoría '{args.category}' ")
        return updated_categories
    

    def handle_display(self, args):
        """Handler para comando displaycat

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        categories = self.repo.get_all()
        self.repo.display(categories)

