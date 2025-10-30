import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logging.info("Script started")
logging.warning("Missing value encountered")

# Error Handling with try/except:
try:
    price = float("20")
except ValueError:
    logging.error("Failed to convert price")

# Combine both:
try:
    df = pd.read_csv("/home/user/repositorio/sales.csv")
except FileNotFoundError:
    logging.error("File not found")
    exit(1)