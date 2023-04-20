# customer_churn_project

## csv_conversion_split

This script (csv_conversion_split.py) takes a CSV file as input and produces two output CSV files. It converts a specific date field from a given input format to a specified output format, and also adds three new columns to each row - year, month, and quarter. The resulting CSV files are then split into two files based on the number of rows.



## How to use
1. Make sure you have Python 3 installed on your system.

2. Clone or download this repository and navigate to the csv_files directory.

3. Add the input CSV file you want to process to this directory.

4. Open the csv_conversion_split.py file and modify the following variables as needed:

    - `input_file`: the name of your input file.
    - `output_file1`: the name of the first output file (with the first half of rows).
    - `output_file2`: the name of the second output file (with the second half of rows).
    - `input_date_format`: the format of the date field in the input file.
    - `output_date_format`: the desired output format of the date field.
5. Save the modified `csv_conversion_split.py` file.

6. Open a command prompt or terminal window and navigate to the directory where the `csv_conversion_split.py` file is located.
7. Run the following command to execute the script:
    ```bash
    python csv_convrsion_split.py
    ```
8. The resulting output CSV files will be generated in the csv_files directory.
9. You can open and verify the output CSV files using any CSV viewer or editor of your choice.


## Dependencies

- Python 3
- csv module
- datetime module

-----

# SQL queries
- The `CreateTable.sql` file contains SQL code to create a new table named `customer_churn_data` in a database. 

- The `InsertData.sql` file contains SQL code to insert data into the `customer_churn_data` table that was previously created using the `CreateTable.sql` script. This data is retrieved from two separate CSV files hosted on GitHub, and the INSERT statements are executed separately to ensure that each file is processed correctly.
