import csv
from datetime import datetime

# Define input and output file paths
input_file = 'data.csv'
output_file1 = 'output1.csv'
output_file2 = 'output2.csv'

# Define the format of the input date
input_date_format = '%m/%d/%Y %H:%M'

# Define the format of the output date
output_date_format = '%Y-%m-%d %H:%M:%S'

# Read the input file and split the rows into two halves
with open(input_file, 'r', encoding='ISO-8859-1') as input_csv, open(output_file1, 'w', newline='') as output_csv1, open(output_file2, 'w', newline='') as output_csv2:
    reader = csv.reader(input_csv)
    writer1 = csv.writer(output_csv1)
    writer2 = csv.writer(output_csv2)

    # Write the header row to each output file
    header = next(reader)
    header.extend(['year', 'month', 'quarter'])
    writer1.writerow(header)
    writer2.writerow(header)
    # Split the rows into two halves
    rows = list(reader)
    total_rows = len(rows)
    half_rows = total_rows // 2

    # Convert the date field to the output format and write each half of the rows to a different output file
    for i, row in enumerate(rows):
        # Convert the date field to the output format
        input_date = datetime.strptime(row[4], input_date_format)
        output_date = datetime.strftime(input_date, output_date_format)
        row[4] = output_date
        year = input_date.year
        month = input_date.month
        quarter = (month - 1) // 3 + 1

        # Add the new columns to the row and write it to the output file
        row.extend([year, month, quarter])
        # Write the row to the appropriate output file
        if i < half_rows:
            writer1.writerow(row)
        else:
            writer2.writerow(row)

print('Conversion and split complete.')
