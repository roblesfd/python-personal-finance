from datetime import datetime
from functools import reduce
from pprint import pprint

from repositories.base_transaction_repo import BaseTransactionRepository
from export.export_csv import export_to_csv
from export.export_pdf import export_to_pdf


class TransactionHandler:

    def __init__(self, repo: BaseTransactionRepository):
        self.repo = repo

    def handle_add(self, args):
        """Handler para comando add

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        transaction = {
            "tipo": args.tipo,
            "monto": args.monto,
            "categoria": args.categoria,
            "descripcion": args.descripcion,
            "fecha": datetime.now().isoformat()
        }
        transactions = self.repo.get_all()
        transactions.append(transaction)
        self.repo.save(transactions)


    def handle_list(self, args):
        """Handler para comando list

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        transactions = self.repo.get_all()
        pprint(transactions)


    def handle_report(self, args):
        """Handler para comando report

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """

        start_date = datetime.strptime(args.desde, "%Y-%m-%d") if args.desde else datetime.min
        end_date = datetime.strptime(args.hasta, "%Y-%m-%d") if args.hasta else datetime.max

        filters = [
            (lambda tx: self.filter_by_category(tx, args.categoria)) if args.categoria else None,
            (lambda tx: self.filter_by_type(tx, args.tipo)) if args.tipo else None,
            (lambda tx: self.filter_by_date(tx, start_date, end_date)) if (args.desde or args.hasta) else None,
        ]

        transactions = reduce(lambda acc, f: f(acc) if f else acc, filters, self.repo.get_all())
        
        balance = self.repo.calculate_balance(transactions)
        print("Reporte de movimientos")
        self.repo.display(transactions)
        print(f"Balance total: {balance}")


    def handle_export(self, args):
        """Handler para comando export

        Args:
            args (list[str]): Lista de argumentos de CLI 
        """
        transactions = self.repo.get_all()
        if args.format == "csv":
            export_to_csv(transactions, "movimientos.csv")
        elif args.format == "pdf":
            export_to_pdf(transactions, "movimientos.pdf")


