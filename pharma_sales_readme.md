![Pharma Dashboard](assets/pharma_spending_banner.png)

# 💊 Pharmaceutical Sales Analytics -- ETL Data Pipeline

## 📊 Project Overview

This project analyzes **global pharmaceutical spending trends** using a
complete **data analytics pipeline** built with Python, SQL, and
Tableau.

The goal of this project is to demonstrate **core data analyst skills**,
including:

-   Data extraction from public datasets
-   Data cleaning and transformation (**ETL**)
-   Database design and **SQL analytics**
-   Data visualization and dashboard creation

The dataset contains **pharmaceutical spending by country and year**,
enabling analysis of trends in:

-   Healthcare spending
-   Drug market dynamics
-   Global pharmaceutical investment patterns

This project is designed as a **portfolio project for entry-level data
analyst roles**.

------------------------------------------------------------------------

# 🧠 Business Questions

This analysis answers several key questions:

-   Which countries spend the **most on pharmaceuticals per capita**?
-   How has **pharmaceutical spending changed over time**?
-   Which countries spend the **largest share of GDP on
    pharmaceuticals**?

------------------------------------------------------------------------

# 🏗️ Project Architecture

The project follows a standard **ETL data pipeline** architecture:

Raw Dataset ↓ Python ETL Pipeline ↓ Cleaned Dataset ↓ PostgreSQL
Database ↓ SQL Analytics ↓ Tableau Dashboard

------------------------------------------------------------------------

# 🛠️ Tech Stack

  Tool             Purpose
  ---------------- ------------------------------------
  Python           Data extraction and transformation
  Pandas           Data cleaning and processing
  PostgreSQL       Data storage
  SQL              Analytical queries
  Tableau Public   Data visualization
  GitHub           Version control

------------------------------------------------------------------------

# 📂 Project Structure

    pharma-sales-etl-project/

    data/
       raw/
          data.csv
       processed/
          cleaned_data.csv

    etl/
       extract.py
       transform.py
       load.py

    sql/
       schema.sql
       analysis_queries.sql

    notebooks/
       exploration.ipynb

    tableau/
       pharma_spending_analysis.twbx

    README.md

Key files:

-   Raw dataset → `data/raw/data.csv`
-   Cleaned dataset → `data/processed/cleaned_data.csv`
-   SQL queries → `sql/analysis_queries.sql`
-   Tableau dashboard → `tableau/pharma_spending_analysis.twbx`

------------------------------------------------------------------------

# 📥 Data Source

Dataset: **OECD Pharmaceutical Drug Spending Dataset**

Public repository:
https://github.com/datasets/pharmaceutical-drug-spending

The dataset includes:

-   Location
-   Time
-   Pharmaceutical spending per capita
-   Pharmaceutical spending as % of GDP
-   Pharmaceutical spending as % of healthcare spending

------------------------------------------------------------------------

# 🔄 ETL Pipeline

## 1️⃣ Extract

    df = pd.read_csv("data/raw/data.csv")

Script: `etl/extract.py`

## 2️⃣ Transform

Cleaning steps:

-   Standardizing column names
-   Removing duplicates
-   Handling missing values
-   Preparing dataset for SQL storage

Example:

    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    df = df.fillna(0)

Cleaned data stored in:

`data/processed/cleaned_data.csv`

Script: `etl/transform.py`

## 3️⃣ Load

    engine = create_engine("postgresql://postgres:password@localhost:5432/pharma_sales_db")

    df.to_sql(
        "pharma_sales",
        engine,
        if_exists="replace",
        index=False
    )

Script: `etl/load.py`

------------------------------------------------------------------------

# 🗄️ Database Schema

    CREATE TABLE pharma_sales (
        country TEXT,
        year INT,
        percent_healthxp FLOAT,
        percent_gdp FLOAT,
        spending_per_capita FLOAT,
        total_spend FLOAT
    );

Schema file: `sql/schema.sql`

------------------------------------------------------------------------

# 📈 SQL Analysis

Queries stored in:

`sql/analysis_queries.sql`

Example:

### Top pharmaceutical spending countries

    SELECT location,
    ROUND(SUM(total_spend)::NUMERIC, 2) AS total_spending
    FROM cleaned_data
    GROUP BY location
    ORDER BY total_spending DESC
    LIMIT 10;

### Spending trends over time

    SELECT time,
    ROUND(AVG(usd_cap)::NUMERIC, 2) AS avg_capital
    FROM cleaned_data
    GROUP BY time
    ORDER BY time
    LIMIT 10;

### Countries with highest pharma spending share of GDP

    SELECT location,
    ROUND(pc_gdp::NUMERIC, 2) AS percent_gdp
    FROM cleaned_data
    ORDER BY percent_gdp DESC
    LIMIT 10;

------------------------------------------------------------------------

# 📊 Tableau Dashboard

The Tableau dashboard provides insights into:

-   Global pharmaceutical spending
-   Spending trends over time
-   Top spending countries
-   Pharmaceutical spending as share of GDP

Dashboard visualizations include:

-   Global map of pharmaceutical spending
-   Time series analysis
-   Country comparisons
-   Healthcare spending ratios

Dashboard file:

`tableau/pharma_spending_analysis.twbx`

------------------------------------------------------------------------

# 🔍 Key Insights

-   Pharmaceutical spending varies significantly between countries.
-   High-income countries spend more per capita on medicines.
-   Pharmaceutical spending as share of GDP has steadily increased over
    time.

------------------------------------------------------------------------

# 🚀 How to Run the Project

## 1 Clone repository

    git clone https://github.com/yourusername/pharma-sales-etl-project.git

## 2 Install dependencies

    pip install -r requirements.txt

## 3 Run ETL pipeline

    python etl/extract.py
    python etl/transform.py
    python etl/load.py

## 4 Run SQL queries

Execute queries from:

`sql/analysis_queries.sql`

## 5 Open Tableau dashboard

Open:

`tableau/pharma_spending_analysis.twbx`

------------------------------------------------------------------------

# 📚 Skills Demonstrated

-   Data pipeline design
-   ETL development
-   Data cleaning with Python
-   SQL database management
-   Analytical SQL queries
-   Data visualization
-   GitHub project structuring

------------------------------------------------------------------------

# 👤 Author

**Arefeh Kardani**

Background in **Pharmaceutical Biology** transitioning into **Data
Analytics**.

Interested in:

-   Healthcare analytics
-   Pharmaceutical data
-   Data-driven decision making
