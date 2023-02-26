import pandas as pd
import numpy as np

df = pd.read_excel (r'C:\Users\Saurabh.DESKTOP-DTU5AD3\Desktop\Optimizer Project\Python files\sum.xlsx') 
df.columns = ['BP','BQ','SP','SQ']
print(df)

a = []
a.extend(df['BP'].tolist())
print(a)

b = []
b.extend(df['SP'].tolist())
print(b)

price = sorted(np.unique(a+b))

print(price)





            
            

       
