import sys
import pandas as pd
import subprocess
import zipfile
import io

file_path = sys.argv[1]

def load_data(path):
    try:
        with zipfile.ZipFile(path, 'r') as z:
            csv_name = [name for name in z.namelist() if name.endswith('.csv')][0]
            return pd.read_csv(z.open(csv_name), low_memory=False)
    except (zipfile.BadZipFile, IsADirectoryError, IndexError):
        print("Error: The provided file is not a valid ZIP archive containing a CSV file.")
        sys.exit(1)

df = load_data(file_path)
df.to_csv("data_raw.csv", index=False)
print("Data ingestion completed.")

subprocess.run(["python", "preprocess.py", "data_raw.csv"])