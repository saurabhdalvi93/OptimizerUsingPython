import pandas as pd
import numpy as np
import xlsxwriter as xl

df = pd.read_excel (r'C:\Users\Saurabh.DESKTOP-DTU5AD3\Desktop\Optimizer Project\Python files\sum.xlsx') 
df.columns = ['BP','BQ','SP','SQ']
print("Table ::")
print(df)

#-------------------------------------------* Program For Price Ladder *--------------------------------------#


a = []
a.extend(df['BP'].tolist())
#print('a =',a)
b = []
b.extend(df['SP'].tolist())

newlist = sorted(np.unique(a+b))
price_list = [x for x in newlist if np.isnan(x) == False]
print()
print("Price List :: ",price_list)

df1 = pd.DataFrame(columns = ['CBQ', 'Price', 'CSQ', 'MinCumQty'])

for price in price_list:
    #print('-------> Price =', price)
    c = []
    d = []
  
  # to find the value of CBQ
    for i in list(df.BP):
        if (i >= price):
            Total = df.loc[df['BP'] >= i, 'BQ'].sum()
            c.append(Total)
    CBQ = max(c)
    #print('CBQ =',CBQ)

       
  # to find the value of CSQ
    for j in list(df.SP):
        if (j <= price):
            Total1 = df.loc[df['SP'] <= j, 'SQ'].sum()
            d.append(Total1)
    CSQ = max(d)
    #print('CSQ =',CSQ)

    if(CBQ<CSQ):
        minCumQty = CBQ
        #print('MinCumQty =',minCumQty)
    
    else:
        minCumQty = CSQ
        #print('MinCumQty =',minCumQty)
        
    df1 = df1.append({'CBQ' : CBQ, 'Price' : price, 'CSQ' : CSQ, 'MinCumQty' : minCumQty}, 
                ignore_index = True)    
        
print("Price Ladder ::")
print(df1)

tradeQty = df1.MinCumQty.max()
print('Trade Qty ::',tradeQty)

tradePrice = df1.loc[df1['MinCumQty'] == tradeQty, 'Price']
print('Trade Price ::',tradePrice)


