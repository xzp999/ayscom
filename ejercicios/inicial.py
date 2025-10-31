from defcsv import load_sales
 
def main():
    print("Hello")
    df = load_sales()
    print(df)
 
if __name__ == "__main__":
    main()
