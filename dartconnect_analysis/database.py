import psycopg2
import logging
from config import report_config, column_mapping


def open_database():
    # Assumes a local postgresql instance running without credentials needed
    conn = psycopg2.connect(
        # host="your_host",
        database="dca"
        # user="your_user",
        # password="your_password"
    )
    cursor = conn.cursor()
    conn.autocommit = False
    conn.commit()
    return conn, cursor


def close_database(conn, cursor):
    cursor.close()
    conn.commit()
    conn.close()


def configure_database():
    # Major data quality issues such as columns without names, duplicate column names
    # So please excuse the whacky stuff :)

    conn, cur = open_database()
    for table in report_config:
        table_name = table['TableName']
        logging.info(f'Working on {table_name}')
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        column_counter = 0
        columns_processed = {}

        for column in table['Columns']:
            cm = column_mapping[column]
            cn = cm['ColumnName']
            if cn not in columns_processed:
                columns_processed[cn] = 1
            else:
                columns_processed[cn] += 1

            uq_column_counter = columns_processed[cn]
            logging.info(f'table: {table_name} cn: {cn} occurence: {uq_column_counter}')
            if uq_column_counter > 1:
                cn = f'{cn}_{uq_column_counter}'
            dt = cm['DataType']
            column_counter += 1
            if column_counter > 1:
                sql += ','
            sql += f'\n\t{cn} {dt}'

        sql += f'\n);\n'
        cur.execute(sql)
        conn.commit()
        logging.info(f'Executed: {sql}')
