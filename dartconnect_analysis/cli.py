import config
import logging
import argparse
import os
import glob
import pandas


parser = argparse.ArgumentParser()
parser.add_argument("--action", choices=['load'], default='load_files', required=True)
parser.add_argument("--load_files", default='./downloads/', help="Directory or file to load")
parser.add_argument("--debug", action='store_true', help="Additional logging", default=False)

args = parser.parse_args()

log_level = os.environ.get('LOG_LEVEL', logging.INFO)

logging.basicConfig(
    level=logging.DEBUG if args.debug else log_level,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

def load_main():
    files = args.load_files
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
        print(file)

def main():
    print("Made it to main")
    if args.action == 'load':
        load_main()
    else:
        raise NotImplementedError



if __name__ == "__main__":
    main()