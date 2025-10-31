# main.py
from masi import logger

def main():
    print("Hello")

if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")