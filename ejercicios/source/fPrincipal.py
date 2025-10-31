# main.py
from ejPython import get_connection
from extract import read_csv, read_csv_with_pd
from loadd import load_clean_sales
from loger import logger
from transform import convert_to_numeric
from utils import drop_duplicates, to_lowercase

csv_file = "sales.csv"

def main():
    # print(read_csv(csv_file))
    sales_df = read_csv_with_pd(csv_file)

    # Clean and transform

    sales_df["Price"] = convert_to_numeric(sales_df["Price"])

    sales_df["Product"] = to_lowercase(sales_df["Product"])
    sales_df["Total"] = sales_df["Price"] * sales_df["Quantity"]
    
    clean_sales_df = drop_duplicates (sales_df)

    load_clean_sales(clean_sales_df)


if __name__ == "__main__":
    logger.info("Application started.")
    main()
    logger.info("Application finished.")
 