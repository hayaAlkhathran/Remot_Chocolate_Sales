import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Hello from chocolate-sales-pro!")
    #read csv file
    df = pd.read_csv('Chocolate Sales.csv')
    #show first 5 row of the dataset
    print(df.head())


    #top 5 best selling products
    df['Amount'] = df['Amount'].replace(r'[\$,]', '', regex=True).astype(float)
    top_products = df.groupby('Product')['Amount'].sum().sort_values(ascending=False).head(5)
    print(top_products)
    
    
    #sort country by revenue
    df.groupby('Country')['Amount'].sum().sort_values(ascending=False).plot(kind='bar')
    plt.title("Amount by Country")
    plt.ylabel("Amount")
    plt.show()


    

if __name__ == "__main__":
    main()
