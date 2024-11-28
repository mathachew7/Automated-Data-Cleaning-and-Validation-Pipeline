import pandas as pd
import json
import logging

# Configure logging
logging.basicConfig(filename="pipeline.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def load_config(config_path="config.json"):
    """Load configuration settings from a JSON file."""
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def validate_data(df):
    """Validate the dataset."""
    if df.empty:
        raise ValueError("Dataset is empty.")
    required_columns = ["Name", "Age", "City"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    logging.info("Data validation passed.")

def clean_data(df, config):
    """Clean the dataset based on the configuration."""
    if config.get("drop_duplicates", False):
        df = df.drop_duplicates()
        logging.info("Dropped duplicate rows.")
    
    for column, strategy in config.get("fill_missing", {}).items():
        if strategy == "mean" and column in df.select_dtypes(include="number").columns:
            df[column] = df[column].fillna(df[column].mean())
            logging.info(f"Filled missing values in {column} with the mean.")
        else:
            df[column] = df[column].fillna(strategy)
            logging.info(f"Filled missing values in {column} with '{strategy}'.")
    return df

def main():
    """Main function to execute the pipeline."""
    # Sample dataset
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, None, 30, 29],
        'City': ['New York', 'Los Angeles', None, 'Chicago']
    }
    df = pd.DataFrame(data)

    # Load the cleaning configuration
    config = load_config()

    # Validate the dataset
    try:
        validate_data(df)
    except ValueError as e:
        logging.error(f"Validation failed: {e}")
        return

    # Clean the dataset
    df_cleaned = clean_data(df, config)

    # Save the cleaned dataset
    output_file = config.get("output_file", "cleaned_data.csv")
    df_cleaned.to_csv(output_file, index=False)
    logging.info(f"Data cleaning complete. Cleaned data saved to {output_file}.")

if __name__ == "__main__":
    main()
