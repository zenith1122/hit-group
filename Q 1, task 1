import csv
import os

# Path to the directory containing CSV files
csv_directory = 'C:/Users/Admin/Documents/GitHub/hit-group'

# Output file name for the combined text
output_txt_file = 'combined_text.txt'

def extract_text_from_csv(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        text_column = 'text'  # Assuming the column name is 'text', change it accordingly

        extracted_text = [row[text_column] for row in csv_reader if text_column in row]

    return extracted_text

def combine_and_write_to_txt(directory, output_file):
    all_text = []

    # Iterate over all CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(directory, filename)
            text_from_csv = extract_text_from_csv(csv_file_path)
            all_text.extend(text_from_csv)

    # Write all extracted text to a single text file
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for text_entry in all_text:
            txt_file.write(text_entry + '\n')

if __name__ == "__main__":
    combine_and_write_to_txt(csv_directory, output_txt_file)



pip install spacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz

pip install transformers

git clone https://github.com/dmis-lab/biobert.git
cd biobert
mkdir weights
cd weights
wget https://github.com/dmis-lab/biobert/raw/master/v1.1.0/PMID/weights.tar.gz
tar -zxvf weights.tar.gz
