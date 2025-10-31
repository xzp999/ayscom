import pandas as pd
 
def load_sales():
    df = pd.read_csv("sales.csv")
    return df