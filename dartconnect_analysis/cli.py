import logging
import argparse
import os
from database import configure_database
from load_files import process_files


parser = argparse.ArgumentParser()
parser.add_argument("--action", choices=['load', 'configure-db'], default='load', required=True)
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
    logging.info(f"Running in {args.action} mode")
    if args.action == 'load':
        process_files(args.load_files)
    elif args.action == 'configure-db':
        configure_database()
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()