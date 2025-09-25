import csv

def export_csv(transactions: list[dict], file: str) -> None:
    if not transactions:
        return
    
    with open(file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)