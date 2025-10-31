import pandas as pd

def procesar_csv(path):
    # 1. csv to dataframe
    df = pd.read_csv("sales.csv")
    
    # 2. remove duplicate rows
    df = df.drop_duplicates()
    
    # 3. change strings to lowercase
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower()
    
    # 4. create a new column total = quantity * price
    df['total'] = df['quantity'] * df['price']
    
    # 5. print the final dataframe in console
    print(df)
    return df