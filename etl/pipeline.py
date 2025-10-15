from dotenv import load_dotenv
import os
from etl.extract import extract
from etl.transform import transform
from etl.load import load

def run(database_url=None):
    products, stores, customers, transactions = extract()
    dp, ds, dc, dd, fs = transform(products, stores, customers, transactions)
    load(dp, ds, dc, dd, fs, database_url=database_url)

if __name__ == '__main__':
    load_dotenv()
    run(database_url=os.environ.get('DATABASE_URL'))