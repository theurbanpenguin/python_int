# pip install pandas openpyxl
import pandas as pd

# Specify the path to your Excel file
file_path = 'sample_data.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Generate statistical data from the DataFrame
statistical_summary = df.describe()

# Display the statistical summary
print(statistical_summary)