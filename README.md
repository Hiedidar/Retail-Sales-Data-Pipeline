# Retail Data Pipeline (demo)

A modern data engineering project simulating an end-to-end retail analytics system — from raw sales data ingestion to a business intelligence dashboard in Metabase.

Built with:
Python · Pandas · PostgreSQL · Docker · Metabase

## Project Overview

This project demonstrates how to design and deploy a Retail Sales Data Pipeline that:

- Extracts and transforms raw transactional data
- Loads clean data into a PostgreSQL data warehouse
- Enbles visual analytics in Metabase

## Architecture Overivew

           +-------------+
           |  Raw CSVs   |
           +------+------+          ETL (Python)
                  |
                  v
        +---------+----------+
        |  Transform & Load  |
        |  (Pandas + SQLA)   |
        +---------+----------+
                  |
                  v
          +-------+--------+
          |  PostgreSQL DW  |
          +-------+--------+
                  |
                  v
            +-----+------+
            |  Metabase   |
            |  Dashboards |
            +-------------+

## Contents
- `data/` : CSV samples (products, stores, customers, transactions)
- `etl/` : extract/transform/load scripts (pure Python/pandas)
- `sql/` : star schema DDL (schema.sql)
- `airflow_dag/` : example Airflow DAG (skeleton)
- `tests/` : basic data quality tests
- `dashboards/` : placeholder for Power BI files / screenshots

## Quick start (local demo using SQLite)
1. Create a Python venv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Run the ETL pipeline (defaults to sqlite at `data/retail_dw.db`):
   ```bash
   python etl/pipeline.py
   ```

3. Run tests:
   ```bash
   python run_tests.py
   ```

4. Open `data/transactions.csv` or connect Power BI to `data/retail_dw.db` to build dashboards.


## Author

- Ayomide Emmanuel
- 💼 Data Engineer & Microsoft Dynamics 365 Developer
- 🔗 LinkedIn (http://linkedin.com/in/ayomide-shonekan-84323b165)
- 📦 GitHub (https://github.com/Hiedidar)

## Future Improvements
- Automate ETL runs with Airflow or Prefect
- Add dbt for transformation layer
- Integrate Power BI or Superset dashboards
