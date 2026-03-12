# Step 1: Import pandas
import pandas as pd

# Step 2: Define the transform function
def transform_data(path):
    df = pd.read_csv(path)
    # Make all column names lowercase
    df.columns = df.columns.str.lower()
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Fill missing values with 0
    df = df.fillna(0)
    
    return df

# Step 3: Apply the transform function
df_clean = transform_data("../data/raw/data.csv")

# Step 4: Preview the cleaned data
df_clean.head()

# Step 5: Save cleaned data to processed folder
def save_clean_data(df, path):
    df.to_csv(path, index=False)

save_clean_data(df_clean, "../data/processed/cleaned_data.csv")