import pandas as pd

def extract_text_from_csv(csv_files, output_txt_file):
    with open(output_txt_file, 'w', encoding='utf-8') as outfile:
        for csv_file in csv_files:
            # Load the CSV file
            df = pd.read_csv(csv_file)
            
            # Check which column contains the text
            if 'TEXT' in df.columns:
                text_column = 'TEXT'
            elif 'SHORT-TEXT' in df.columns:
                text_column = 'SHORT-TEXT'
            else:
                continue  # Skip if there is no recognizable text column
            
            # Extract and write text data into the output text file
            for text in df[text_column].dropna():
                outfile.write(text + '\n')

# List of CSV file paths
csv_files = [
    'CSV1.csv',  # Update with the actual paths
    'CSV2.csv',
    'CSV3.csv',
    'CSV4.csv'
]
output_txt_file = 'combined_texts.txt'

# Extract text from CSVs and combine into one .txt file
extract_text_from_csv(csv_files, output_txt_file)
