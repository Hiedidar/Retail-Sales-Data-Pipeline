from sqlalchemy import create_engine
import os

def load(dim_product, dim_store, dim_customer, dim_date, fact_sales, database_url=None):
    # default to sqlite for demo
    if database_url is None:
        database_url = os.environ.get('DATABASE_URL', 'sqlite:///data/retail_dw.db')
    engine = create_engine(database_url, echo=False)

    # write dims then fact (replace for demo)
    dim_product.to_sql('dim_product', engine, if_exists='replace', index=False)
    dim_store.to_sql('dim_store', engine, if_exists='replace', index=False)
    dim_customer.to_sql('dim_customer', engine, if_exists='replace', index=False)
    dim_date.to_sql('dim_date', engine, if_exists='replace', index=False)
    fact_sales.to_sql('fact_sales', engine, if_exists='replace', index=False)
    print('Loaded to', database_url)

if __name__ == '__main__':
    import etl.extract as ex, etl.transform as tr
    p,s,c,t = ex.extract()
    dp, ds, dc, dd, fs = tr.transform(p,s,c,t)
    load(dp, ds, dc, dd, fs)
