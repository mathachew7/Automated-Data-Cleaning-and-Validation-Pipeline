import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, None, 30, 29],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}
df = pd.DataFrame(data)

# Clean data
df = df.drop_duplicates()  # Remove duplicates
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Fill missing ages with mean
df['City'] = df['City'].fillna('Unknown')  # Fill missing cities with 'Unknown'

# Save cleaned data
df.to_csv('cleaned_data.csv', index=False)
print("Data cleaning complete. Cleaned data saved as cleaned_data.csv.")


