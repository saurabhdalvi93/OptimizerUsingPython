import pandas as pd
import numpy as np

df = pd.read_excel(
    r'C:\Users\Saurabh.DESKTOP-DTU5AD3\Desktop\DataScience\Optimizer Project\Python files\sum1.xlsx')
df.columns = ['BP', 'BQ', 'SP', 'SQ']
print("Table ::")
print(df)
print()
# -------------------------------------------* Program For Price Ladder *--------------------------------------#

a = []
a.extend(df['BP'].tolist())
print('BP =', a)
b = []
b.extend(df['SP'].tolist())
print('SP =', b)

newlist = sorted(np.unique(a+b))
price_list = [x for x in newlist if np.isnan(x) == False]
print()
print("Price List :: ", price_list)
print()

df1 = pd.DataFrame(columns=['CBQ', 'Price', 'CSQ', 'MinCumQty'])

for price in price_list:
    print("price===>", price)

  # to find the value of CBQ
    CBQ = df.loc[df['BP'] >= price, 'BQ'].sum()
    print('CBQ =', CBQ)

  # to find the value of CSQ
    CSQ = df.loc[df['SP'] <= price, 'SQ'].sum()
    print('CSQ =', CSQ)

    if (CBQ < CSQ):
        minCumQty = CBQ
        print('MinCumQty =', minCumQty)

    else:
        minCumQty = CSQ
        print('MinCumQty =', minCumQty)

    df1 = df1.append({'CBQ': CBQ, 'Price': price, 'CSQ': CSQ,
                     'MinCumQty': minCumQty}, ignore_index=True)

print()
print("Price Ladder ::")
print(df1)

tradeQty = df1.MinCumQty.max()
print('Trade Qty ::', tradeQty)

tradePrice = df1.loc[df1['MinCumQty'] == tradeQty, 'Price']
print('Trade Price ::', tradePrice)
