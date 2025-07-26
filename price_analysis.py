import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# --- price_analysis.py (Jupyter Notebook Simulation) ---
# Goal: Analyze and visualize book price data obtained from price_scraper.py.

print("--- Starting book price data analysis ---")

# Section 1: Data Loading
# Equivalent to a Jupyter cell
print("\n### Section 1: Data Loading ###")
file_path = "prices.csv"

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found. Make sure you have run price_scraper.py.")
    # In a real scenario, the user would have to run price_scraper.py
    # For demonstration purposes, let's generate it temporarily if missing
    from price_scraper import generate_and_save_prices_data
    generate_and_save_prices_data(file_path)
    print(f"File '{file_path}' has been automatically generated to continue analysis.")

try:
    df = pd.read_csv(file_path, encoding='utf-8')
    print("Data loaded successfully.")
    print("\nData preview (first 5 rows):")
    print(df.head())
    print("\nData information:")
    print(df.info())
except Exception as e:
    print(f"An error occurred while loading data: {e}")
    exit() # Terminate script if data cannot be loaded

# Section 2: Data Cleaning
# Equivalent to a Jupyter cell
print("\n### Section 2: Data Cleaning ###")
print("\nChecking for missing values before cleaning:")
print(df.isnull().sum())

# 2.1 Handling missing values
# For 'Autor' (Author): Fill with 'No data'
df['Autor'].fillna('No data', inplace=True)

# For 'Ocena (1-5)' (Rating (1-5)): Fill with median
# First, ensure the column is numeric
df['Ocena (1-5)'] = pd.to_numeric(df['Ocena (1-5)'], errors='coerce')
median_ocena = df['Ocena (1-5)'].median()
df['Ocena (1-5)'].fillna(median_ocena, inplace=True)
print(f"\nFilled missing 'Ocena (1-5)' with median: {median_ocena}")

# 2.2 Handling incorrect data types and values
# 'Cena (PLN)' (Price (PLN)) column might contain non-numeric values (e.g., 'BRAK')
# Convert to numeric, coercing errors to NaN, then drop rows with NaN in price
df['Cena (PLN)'] = pd.to_numeric(df['Cena (PLN)'], errors='coerce')
initial_rows_before_price_drop = len(df)
df.dropna(subset=['Cena (PLN)'], inplace=True)
if len(df) < initial_rows_before_price_drop:
    print(f"Removed {initial_rows_before_price_drop - len(df)} rows with invalid values in 'Cena (PLN)' column.")

# 2.3 Handling duplicates
initial_rows_before_duplicates = len(df)
df.drop_duplicates(inplace=True)
if len(df) < initial_rows_before_duplicates:
    print(f"Removed {initial_rows_before_duplicates - len(df)} duplicate rows.")

print("\nChecking for missing values after cleaning:")
print(df.isnull().sum())
print("\nData information after cleaning:")
print(df.info())
print("\nData preview after cleaning:")
print(df.head())

# Section 3: Data Exploration
# Equivalent to a Jupyter cell
print("\n### Section 3: Data Exploration ###")

# Basic descriptive statistics
print("\nDescriptive statistics for prices:")
print(df['Cena (PLN)'].describe())

# Most expensive books
print("\n5 most expensive books:")
print(df.sort_values(by='Cena (PLN)', ascending=False).head(5)[['Tytuł', 'Autor', 'Cena (PLN)']])

# Highest rated books
print("\n5 highest rated books:")
print(df.sort_values(by='Ocena (1-5)', ascending=False).head(5)[['Tytuł', 'Autor', 'Ocena (1-5)']])

# Number of books per publisher
print("\nNumber of books per publisher:")
print(df['Wydawnictwo'].value_counts())

# Average price per author
print("\nAverage book price per author:")
print(df.groupby('Autor')['Cena (PLN)'].mean().sort_values(ascending=False).head(10))

# Average rating per publisher
print("\nAverage book rating per publisher:")
print(df.groupby('Wydawnictwo')['Ocena (1-5)'].mean().sort_values(ascending=False).head(10))

# Section 4: Data Visualization
# Equivalent to a Jupyter cell
print("\n### Section 4: Data Visualization ###")

# Plot style settings
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# Plot 1: Price distribution histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Cena (PLN)'], bins=10, kde=True, color='skyblue')
plt.title('Distribution of Book Prices', fontsize=16)
plt.xlabel('Price (PLN)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 2: Number of books per publisher (Top 5)
plt.figure(figsize=(12, 7))
top_publishers = df['Wydawnictwo'].value_counts().head(5)
sns.barplot(x=top_publishers.index, y=top_publishers.values, palette='viridis')
plt.title('Top 5 Publishers by Number of Books', fontsize=16)
plt.xlabel('Publisher', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 3: Average rating per author (Top 5)
plt.figure(figsize=(12, 7))
avg_rating_by_author = df.groupby('Autor')['Ocena (1-5)'].mean().sort_values(ascending=False).head(5)
sns.barplot(x=avg_rating_by_author.index, y=avg_rating_by_author.values, palette='magma')
plt.title('Top 5 Authors by Average Rating', fontsize=16)
plt.xlabel('Author', fontsize=12)
plt.ylabel('Average Rating (1-5)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 4: Box plot of prices by publisher (for top 3)
plt.figure(figsize=(12, 7))
top_3_publishers_names = df['Wydawnictwo'].value_counts().head(3).index
df_top_3_publishers = df[df['Wydawnictwo'].isin(top_3_publishers_names)]
sns.boxplot(x='Wydawnictwo', y='Cena (PLN)', data=df_top_3_publishers, palette='plasma')
plt.title('Distribution of Book Prices for Top 3 Publishers', fontsize=16)
plt.xlabel('Publisher', fontsize=12)
plt.ylabel('Price (PLN)', fontsize=12)
plt.tight_layout()
plt.show()

print("\n--- Data analysis completed ---")