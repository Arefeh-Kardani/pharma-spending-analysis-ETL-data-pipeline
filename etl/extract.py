# Step 1: Import pandas
import pandas as pd

# Step 2: Define a function to load your CSV
def extract_data(path):
    df = pd.read_csv(path)  # reads the CSV into a table
    return df

# Step 3: Call the function for your data.csv
df = extract_data("../data/raw/data.csv")  # update path to your file

# Step 4: Show the first 5 rows to check it worked
print(df.head())