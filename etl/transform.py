import pandas as pd

def transform(products, stores, customers, transactions):
    # normalize column names (lowercase)
    products.columns = products.columns.str.lower()
    stores.columns = stores.columns.str.lower()
    customers.columns = customers.columns.str.lower()
    transactions.columns = transactions.columns.str.lower()

    # Build dimension tables
    dim_product = products[['product_id','name','category','price','promotion_flag']].drop_duplicates()
    dim_store = stores[['store_id','store_name','city','region']].drop_duplicates()
    dim_customer = customers[['customer_id','gender','age_group','income_level']].drop_duplicates()

    # dim_date from transactions dates
    transactions['date'] = pd.to_datetime(transactions['date']).dt.date
    dim_date = pd.DataFrame({'date_id': pd.to_datetime(transactions['date']).drop_duplicates().sort_values()})
    dim_date['year'] = dim_date['date_id'].dt.year
    dim_date['month'] = dim_date['date_id'].dt.month
    dim_date['day'] = dim_date['date_id'].dt.day
    dim_date['weekday'] = dim_date['date_id'].dt.weekday + 1
    dim_date['quarter'] = dim_date['date_id'].dt.quarter

    # fact table
    fact_sales = transactions.rename(columns={'date':'date_id'})[
        ['transaction_id','date_id','product_id','customer_id','store_id','quantity','unit_price','promotion_applied','revenue']
    ]

    return dim_product, dim_store, dim_customer, dim_date, fact_sales

if __name__ == '__main__':
    import etl.extract as ex
    p,s,c,t = ex.extract()
    dp, ds, dc, dd, fs = transform(p,s,c,t)
    print('Transformed:', dp.shape, ds.shape, dc.shape, dd.shape, fs.shape)
