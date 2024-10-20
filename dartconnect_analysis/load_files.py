import csv
import os
import glob
import logging

from pandas.plotting import table

from config import report_config
from database import open_database


def identify_report(column_list):
    s_column_list=set(column_list)
    rc = None
    for report in report_config:
        rt_column_list = set(report['Columns'])
        if s_column_list == rt_column_list:
            rc=report
            print(f'{report["ReportType"]} detected')
            break

    return rc

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

    conn, cur = open_database()

    for file in csv_files:
        with open(file, 'r') as f:
            counter=1
            reader=csv.reader(f)
            for row in reader:
                if counter == 1:
                    report = identify_report(row)
                    if report is None:
                        logging.warning(f'Report config not found for {file}')
                        break
                    else:
                        report_type = report['ReportType']
                        table_name = report['TableName']
                        logging.info(f'Report Type {report_type}, Table name {table_name}')
                        col_sql = ''
                        num_cols = len(row)
                        print(num_cols)
                        cols = 0
                        for column in row:
                            cols += 1
                            if cols < num_cols:
                                col_sql += '?, '
                            else:
                                col_sql += '?'
                else:
                    load_csv_to_db(cur, row, table_name, col_sql)

                counter += 1
            conn.commit()
    cur.close()
    conn.close()
# c.execute("INSERT INTO rounds (tournament_id, round_number, round_status) VALUES (?, ?, 'OPEN')",
#                   (self.tournament_id, next_round))

def load_csv_to_db(cur, row, table_name, cols):
    sql = f'INSERT INTO {table_name} VALUES ({cols});'
    cur.execute(sql, tuple(row))
    #print(sql)
    # sql = f'INSERT INTO {table_name} VALUES {[f"{i}" for i in row}'
    # cursor.execute(
    #     f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})",
    #     row
    # )
