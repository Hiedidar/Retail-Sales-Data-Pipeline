-- star schema DDL (PostgreSQL dialect shown)
CREATE TABLE dim_product (
  product_id VARCHAR PRIMARY KEY,
  name TEXT,
  category TEXT,
  price NUMERIC(10,2),
  promotion_flag INTEGER
);

CREATE TABLE dim_store (
  store_id VARCHAR PRIMARY KEY,
  store_name TEXT,
  city TEXT,
  region TEXT
);

CREATE TABLE dim_customer (
  customer_id VARCHAR PRIMARY KEY,
  gender TEXT,
  age_group TEXT,
  income_level TEXT
);

CREATE TABLE dim_date (
  date_id DATE PRIMARY KEY,
  year INTEGER,
  month INTEGER,
  day INTEGER,
  weekday INTEGER,
  quarter INTEGER
);

CREATE TABLE fact_sales (
  transaction_id VARCHAR PRIMARY KEY,
  date_id DATE REFERENCES dim_date(date_id),
  product_id VARCHAR REFERENCES dim_product(product_id),
  customer_id VARCHAR REFERENCES dim_customer(customer_id),
  store_id VARCHAR REFERENCES dim_store(store_id),
  quantity INTEGER,
  unit_price NUMERIC(10,2),
  promotion_applied INTEGER,
  revenue NUMERIC(12,2)
);
