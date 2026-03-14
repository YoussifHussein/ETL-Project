import pandas as pd
import glob
import os
import logging #logging module to log the execution of the script and any errors that may occur during the ETL process

logging.basicConfig( 
    filename='etl_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("Starting pipline execution")
logging.info("--ETL JOB STARTED--")
try:
    all_dataframes = []
    files = glob.glob(os.path.join('input data/*'))  #glob to find all files in the input data folder
    print(f"Found {len(files)} files to process.")
    for file in files:
        if file.endswith(".csv"):
            print(f"Processing file: {file}")
            df = pd.read_csv(file)
            all_dataframes.append(df)
        elif file.endswith(".json"):
            print(f"Processing file: {file}")
            df = pd.read_json(file)
            all_dataframes.append(df)
    if len(all_dataframes)>0:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        print(f"Combined dataframe shape: ")
    else:
        raise ValueError("No valid files found to process.")
    if combined_df['price'].isnull().sum() > 0:
        combined_df.dropna(subset=['price'], inplace=True)
        combined_df['quantity'] = combined_df['quantity'].fillna(0)
        combined_df['total_value'] = combined_df['price'] * combined_df['quantity']
        combined_df.drop_duplicates(inplace=True)
    print("Transformation process completed successfully.")
    logging.info("--ETL JOB COMPLETED SUCCESSFULLY--")
    if not os.path("output data"):
        os.makedirs("output data")
    output_path = "output data"
    combined_df.to_csv(os.path.join(output_path, "combined_data.csv"), index=False)
    print(f"Combined data saved to")
    logging.info(f"Combined saving completed successfully at")
except Exception as e:
    print(f"An error occurred during the ETL process: {e}")
    logging.error(f"An error occurred during the ETL process: {e}")
              
