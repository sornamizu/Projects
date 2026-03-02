import pandas as pd

# Load the data
df = pd.read_csv(r'C:\Users\sornambiga\OneDrive\Documents\Projects\Infosys\netflix_titles.csv')

# Get an overview
print("Original shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (fill with mean/median/mode or drop)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save the cleaned data
df.to_csv('cleaned_netflix_titles.csv', index=False)

print("Cleaned shape:", df.shape)
print(df.head())
