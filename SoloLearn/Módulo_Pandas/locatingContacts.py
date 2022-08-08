import numpy as np 
import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}

#Cria o dataframe e os nomes como index
df = pd.DataFrame(data, index = ['James', 'Billy', 'Bob', 'Amy', 'Tom'])

name = input()
print(df.loc[name])