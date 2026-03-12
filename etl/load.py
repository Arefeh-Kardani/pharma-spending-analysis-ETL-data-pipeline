import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database
engine = create_engine(
"postgresql://postgres:password@localhost:5433/pharma_sales_db"
)
# Read the cleaned data from the CSV file
df = pd.read_csv("../data/processed/cleaned_data.csv")

# Load the cleaned data into the PostgreSQL database
df.to_sql(
    "cleaned_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded!")