
import pandas as pd
import os

def run_preprocessing(input_path):
    # Load data
    df = pd.read_csv(input_path, encoding='ISO-8859-1')
    
    # Cleaning
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    # Save hasil bersih
    output_name = "OnlineRetail_preprocessed.csv"
    df.to_csv(output_name, index=False)
    print(f"Automasi Berhasil! File tersimpan: {output_name}")

if __name__ == "__main__":
    run_preprocessing('OnlineRetail.csv')
