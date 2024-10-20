import sqlite3
import logging
import json
from config import report_config, column_mapping


def open_database():
    # Assumes a local postgresql instance running without credentials needed
    conn = sqlite3.connect('dca.sqlite3')

    # conn = psycopg2.connect(
    #     # host="your_host",
    #     database="dca"
    #     # user="your_user",
    #     # password="your_password"
    # )
    cursor = conn.cursor()
    return conn, cursor


def close_database(conn, cursor):
    cursor.close()
    conn.commit()
    conn.close()


def configure_database():
    # Major data quality issues such as columns without names, duplicate column names
    # So please excuse the whacky stuff :)
    generated_sql = {}

    conn, cur = open_database()
    for table in report_config:
        table_name = table['TableName']
        logging.info(f'Working on {table_name}')
        if table_name in table_ddl_map:
            sql = table_ddl_map[table_name]
        else:
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

            generated_sql[table_name] = sql

        cur.execute(f'DROP TABLE IF EXISTS {table_name};')
        cur.execute(sql)
        conn.commit()
        logging.info(f'Executed: \n{sql}')

    for i in generated_sql.keys():
        print(f'"{i}": """\n{generated_sql[i]}""",')

table_ddl_map = {
    "cricket_match_summary": """
        CREATE TABLE IF NOT EXISTS cricket_match_summary (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            match_date DATE,
            match_day VARCHAR(64),
            division VARCHAR(64),
            season VARCHAR(128),
            away_at_home VARCHAR(64),
            team_name VARCHAR(256),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            legs_count INTEGER,
            leg_wins_count INTEGER,
            leg_wins_pct DECIMAL(5,2),
            unknown VARCHAR(64),
            marks_count INTEGER,
            darts_count INTEGER,
            mpr DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            high_turn INTEGER,
            eq_9m_count INTEGER,
            hat_tricks_count INTEGER,
            unknown_3 VARCHAR(64),
            report_url VARCHAR(256),
            event_url VARCHAR(64)
        );
    """,
    "x01_match_summary": """
        CREATE TABLE IF NOT EXISTS x01_match_summary (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            match_date DATE,
            match_day VARCHAR(64),
            division VARCHAR(64),
            season VARCHAR(128),
            away_at_home VARCHAR(64),
            team_name VARCHAR(256),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            legs_count INTEGER,
            leg_wins_count INTEGER,
            leg_wins_pct DECIMAL(5,2),
            unknown VARCHAR(64),
            points_total INTEGER,
            darts_count INTEGER,
            ppr DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            high_turn INTEGER,
            eq_180_count INTEGER,
            high_double_out INTEGER,
            high_double_in INTEGER,
            unknown_3 VARCHAR(64),
            report_url VARCHAR(256),
            event_url VARCHAR(64)
        );
    """,
    "cricket_match_counts": """
        CREATE TABLE IF NOT EXISTS cricket_match_counts (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            match_date DATE,
            match_day VARCHAR(64),
            division VARCHAR(64),
            season VARCHAR(128),
            away_at_home VARCHAR(64),
            team_name VARCHAR(256),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            legs_count INTEGER,
            gte_5m_count INTEGER,
            gte_6m_count INTEGER,
            triples_count INTEGER,
            bulls_count INTEGER,
            dbulls_count INTEGER,
            unknown VARCHAR(64),
            gte_5m_count_per_leg DECIMAL(5,2),
            gte_6m_count_per_leg DECIMAL(5,2),
            avg_triples_per_leg DECIMAL(5,2),
            bulls_count_per_leg DECIMAL(5,2),
            dbulls_count_per_leg DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            gte_5m_count_no_tb INTEGER,
            gte_6m_count_no_tb INTEGER,
            triples_count_no_tb INTEGER,
            bulls_count_no_tb INTEGER,
            dbulls_count_no_tb INTEGER,
            unknown_3 VARCHAR(64),
            report_url VARCHAR(256),
            event VARCHAR(64)
        );
    """,
    "x01_match_counts": """
        CREATE TABLE IF NOT EXISTS x01_match_counts (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            match_date DATE,
            match_day VARCHAR(64),
            division VARCHAR(64),
            season VARCHAR(128),
            away_at_home VARCHAR(64),
            team_name VARCHAR(256),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            legs_count INTEGER,
            gte_100_points INTEGER,
            gte_100_count INTEGER,
            eq_180_count INTEGER,
            unknown VARCHAR(64),
            gte_100_pts_per_leg DECIMAL(5,2),
            gte_100_count_per_leg DECIMAL(5,2),
            avg_double_out DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            gte_100_points_no_tb INTEGER,
            gte_100_count_no_tb INTEGER,
            avg_double_out_no_tb DECIMAL(5,2),
            eq_180_count_no_tb INTEGER,
            unknown_3 VARCHAR(64),
            gte_95_points INTEGER,
            gte_95_count INTEGER,
            unknown_4 VARCHAR(64),
            report_url VARCHAR(256),
            event_url VARCHAR(64)
        );
    """,
    "cricket_season_summary": """
        CREATE TABLE IF NOT EXISTS cricket_season_summary (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            team_name VARCHAR(256),
            division VARCHAR(64),
            season VARCHAR(128),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            matches_count INTEGER,
            legs_count INTEGER,
            leg_wins_count INTEGER,
            leg_wins_pct DECIMAL(5,2),
            unknown VARCHAR(64),
            points_total INTEGER,
            darts_count INTEGER,
            mpr DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            high_turn INTEGER,
            eq_9m_count INTEGER,
            hat_tricks_count INTEGER
        );
    """,
    "x01_season_summary": """
        CREATE TABLE IF NOT EXISTS x01_season_summary (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            team_name VARCHAR(256),
            division VARCHAR(64),
            season VARCHAR(128),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            matches_count INTEGER,
            legs_count INTEGER,
            leg_wins_count INTEGER,
            leg_wins_pct DECIMAL(5,2),
            unknown VARCHAR(64),
            points_total INTEGER,
            darts_count INTEGER,
            ppr DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            high_turn INTEGER,
            eq_180_count INTEGER,
            high_double_out INTEGER,
            high_double_in INTEGER,
            best_leg INTEGER
        );
    """,
    "cricket_season_counts": """
        CREATE TABLE IF NOT EXISTS cricket_season_counts (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            team_name VARCHAR(256),
            division VARCHAR(64),
            season VARCHAR(128),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            matches_count INTEGER,
            legs_count INTEGER,
            gte_5m_count INTEGER,
            gte_6m_count INTEGER,
            triples_count INTEGER,
            bulls_count INTEGER,
            dbulls_count INTEGER,
            unknown VARCHAR(64),
            gte_5m_count_per_leg DECIMAL(5,2),
            gte_6m_count_per_leg DECIMAL(5,2),
            avg_triples_per_leg DECIMAL(5,2),
            bulls_count_per_leg DECIMAL(5,2),
            dbulls_count_per_leg DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            gte_5m_count_no_tb INTEGER,
            gte_6m_count_no_tb INTEGER,
            triples_count_no_tb INTEGER,
            bulls_count_no_tb INTEGER,
            dbulls_count_no_tb INTEGER
    );
    """,
    "x01_season_counts": """
        CREATE TABLE IF NOT EXISTS x01_season_counts (
            report VARCHAR(128),
            league_id VARCHAR(64),
            dc_membership VARCHAR(64),
            gender CHAR(1),
            team_name VARCHAR(256),
            division VARCHAR(64),
            season VARCHAR(128),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            matches_count INTEGER,
            legs_count INTEGER,
            gte_100_points INTEGER,
            gte_100_count INTEGER,
            eq_180_count INTEGER,
            unknown VARCHAR(64),
            gte_100_pts_per_leg DECIMAL(5,2),
            gte_100_count_per_leg DECIMAL(5,2),
            avg_double_out DECIMAL(5,2),
            unknown_2 VARCHAR(64),
            gte_100_points_no_tb INTEGER,
            gte_100_points_no_tb_2 INTEGER,
            avg_double_out_no_tb DECIMAL(5,2),
            unknown_3 VARCHAR(64),
            eq_180_pts_per_match DECIMAL(5,2),
            eq_180_pts_per_match_no_tb DECIMAL(5,2),
            unknown_4 VARCHAR(64),
            gte_95_points INTEGER,
            gte_95_count INTEGER
        );
    """,
    "membership_and_email": """
        CREATE TABLE IF NOT EXISTS membership_and_email (
            league_id VARCHAR(64),
            division VARCHAR(64),
            match_count INTEGER,
            player_email VARCHAR(256),
            player_name VARCHAR(256),
            team_division VARCHAR(256),
            host_names VARCHAR(64),
            start_date DATE,
            last_date DATE
        );
    """,
    "host_device_information": """
        CREATE TABLE IF NOT EXISTS host_device_information (
            league_id VARCHAR(64),
            division VARCHAR(64),
            host_name VARCHAR(64),
            host_email VARCHAR(64),
            member_level VARCHAR(64),
            player_email VARCHAR(256),
            player_name VARCHAR(256),
            start_date DATE,
            last_date DATE
        );
    """,
    "leg_export": """
        CREATE TABLE IF NOT EXISTS leg_export (
            report VARCHAR(128),
            league_id VARCHAR(64),
            member_level VARCHAR(64),
            gender CHAR(1),
            team_name VARCHAR(256),
            division VARCHAR(64),
            season VARCHAR(128),
            email VARCHAR(256),
            last_name_fi VARCHAR(64),
            blank VARCHAR(64),
            dc VARCHAR(64),
            first_name VARCHAR(64),
            player_format CHAR(1),
            game_format VARCHAR(64),
            leg_outcome CHAR(1),
            started_leg BOOLEAN,
            cork CHAR(1),
            unknown VARCHAR(64),
            points_total INTEGER,
            darts_count INTEGER,
            avg_three_darts DECIMAL(5,2),
            high_turn INTEGER,
            high_double_out INTEGER,
            high_double_in INTEGER,
            unknown_2 VARCHAR(64),
            set_number INTEGER,
            game_number INTEGER,
            unknown_3 VARCHAR(64),
            match_date DATE,
            away_at_home VARCHAR(64),
            report_url VARCHAR(256),
            event_url VARCHAR(64)
        );
    """
}