import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def main():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()