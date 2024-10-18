import config
import logging
import argparse
import os
import glob
import pandas
from config import report_config
from load_files import process_files


parser = argparse.ArgumentParser()
parser.add_argument("--action", choices=['load'], default='load', required=True)
parser.add_argument("--load_files", default='./downloads/', help="Directory or file to load")
parser.add_argument("--debug", action='store_true', help="Additional logging", default=False)

args = parser.parse_args()

log_level = os.environ.get('LOG_LEVEL', logging.INFO)

logging.basicConfig(
    level=logging.DEBUG if args.debug else log_level,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    print("Made it to main")
    if args.action == 'load':
        process_files(args.load_files)
    else:
        raise NotImplementedError



if __name__ == "__main__":
    main()