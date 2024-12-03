# Project Overview

This branch implements a data cleaning and standardization pipeline with the following functionality:

## Features Implemented

### 1. Column Standardization
- Standardizes column names by converting them to lowercase and replacing spaces with underscores.
- Saves the standardized column names to a configuration file (`config.json`).

### 2. Configuration File
- The `config.json` file dynamically specifies:
  - Column names.
  - Rules for handling missing values.
  - Duplicate removal settings.
  - Required columns for validation.

### 3. Dataset Cleaning
- Removes duplicates from the dataset as per the configuration.
- Handles missing values based on strategies defined in `config.json`:
  - Supported strategies: `mean`, `median`, or a default value.
- Validates the dataset to ensure all required columns are present.

### 4. Logging and Debugging
- Detailed logging in `pipeline.log` to track all cleaning operations and errors.
- Debug prints for identifying missing values and strategies applied during cleaning.

## How to Use
1. Run `script.py` to standardize column names and generate `config.json`:
   ```bash
   python script.py <input_file>
