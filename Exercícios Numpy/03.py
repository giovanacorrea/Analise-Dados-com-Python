#Criar uma matrix 3x3 apenas de booleanos 

import numpy as np 

#np.full = Return a new array of given shape and type, filled with fill_value.
data = np.full((3, 3), True, dtype=bool)

print(data)