import pandas as pd
from pathlib import Path

def extract(data_dir='data'):
    base = Path(__file__).resolve().parents[1]
    data_path = base / data_dir
    products = pd.read_csv(data_path / 'products.csv')
    stores = pd.read_csv(data_path / 'stores.csv')
    customers = pd.read_csv(data_path / 'customers.csv')
    transactions = pd.read_csv(data_path / 'transactions.csv', parse_dates=['date'])
    return products, stores, customers, transactions

if __name__ == '__main__':
    p, s, c, t = extract()
    print('Extracted: ', len(p), len(s), len(c), len(t))
