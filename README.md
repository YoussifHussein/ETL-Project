# Sales Data ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline for processing and consolidating sales data from multiple file formats (CSV and JSON). This project demonstrates data engineering best practices including data cleaning, transformation, and automated logging.

## 📋 Project Overview

This ETL pipeline extracts sales data from multiple source files, performs data transformations to ensure consistency and quality, and loads the cleaned data into a consolidated output file. The pipeline handles various data quality issues including missing values, inconsistent formatting, and duplicate records.

## 🏗️ Architecture


## 🔄 ETL Process Flow

### 1. EXTRACT
- Reads all files from the `input data` directory
- Supports both CSV and JSON file formats
- Dynamically processes multiple files regardless of format

### 2. TRANSFORM
The pipeline performs the following transformations:
- **Data Standardization**: Standardizes product names by converting to proper case
- **Missing Value Handling**:
  - Removes records with null prices (as price is critical for calculations)
  - Fills null quantities with 0
- **Feature Engineering**: Creates a `total_value` column (price × quantity)
- **Deduplication**: Removes duplicate records
- **Data Type Enforcement**: Ensures proper data types for numerical operations

### 3. LOAD
- Saves the cleaned and transformed data to `output data/combined_data.csv`
- Creates the output directory if it doesn't exist
- Exports data without index to maintain clean output

## 📊 Sample Data Transformation

**Before Transformation:**
