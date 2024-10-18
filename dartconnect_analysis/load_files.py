import csv
import os
import glob
import logging
from config import report_config

def identify_report_type(column_list):
    s_column_list=set(column_list)
    report_type = None
    for report in report_config:
        rt_column_list = set(report['Columns'])
        if s_column_list == rt_column_list:
            report_type=report['ReportType']
            print(f'{report_type} detected')
            break

    return report_type


def process_files(files):
    if files.startswith('.'):
        file_path = os.path.join(os.getcwd(), files)
    else:
        file_path = files
    if files.endswith('.csv'):
        pass
    else:
        file_path = os.path.join(file_path, '*')

    csv_files = glob.glob(file_path)

    for file in csv_files:
        with open(file, 'r') as f:
            counter=1
            reader=csv.reader(f)
            for row in reader:
                if counter == 1:
                    report_type = identify_report_type(row)
                    if report_type is None:
                        logging.warning(f'Report config not found for {file}')
                counter += 1


def load_csv_to_postgresql(conn, cursor, csv_file, table_name):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row if it exists

        for row in reader:
            cursor.execute(
                f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})",
                row
            )

    conn.commit()
