import csv
from datetime import datetime

input_file = 'csv_files/data.csv'
output_file1 = 'csv_files/output1.csv'
output_file2 = 'csv_files/output2.csv'

input_date_format = '%m/%d/%Y %H:%M'

output_date_format = '%Y-%m-%d %H:%M:%S'

with open(input_file, 'r', encoding='ISO-8859-1') as input_csv, open(output_file1, 'w', newline='') as output_csv1, open(output_file2, 'w', newline='') as output_csv2:
    reader = csv.reader(input_csv)
    writer1 = csv.writer(output_csv1)
    writer2 = csv.writer(output_csv2)


    header = next(reader)
    header.extend(['year', 'month', 'quarter'])
    writer1.writerow(header)
    writer2.writerow(header)
    # Split the rows into two halves
    rows = list(reader)
    total_rows = len(rows)
    half_rows = total_rows // 2

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
        if i < half_rows:
            writer1.writerow(row)
        else:
            writer2.writerow(row)

print('Conversion and split complete.')
