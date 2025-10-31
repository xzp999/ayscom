from transformador import procesar_csv # type: ignore

def main():
    print("Hello")
    df = procesar_csv()
    print(df)

if __name__ == "__main__":
    main()
