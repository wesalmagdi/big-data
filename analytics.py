import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]
df = pd.read_csv(file_path)

# Example insights
with open("insight1.txt", "w") as f:
    f.write(f"Dataset shape: {df.shape}")

with open("insight2.txt", "w") as f:
    f.write(f"Columns: {list(df.columns)}")

with open("insight3.txt", "w") as f:
    f.write(f"Summary:\n{df.describe().to_string()}")

print("Analytics completed.")


subprocess.run(["python", "visualize.py", file_path])