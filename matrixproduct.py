import numpy as np

A= np.array([
   [6,5,3,1],
   [3,6,2,2],
   [3,4,3,1]
]
)

B= np.array( [
  [1.5,1],
  [2,2.5],
  [5,4.5],
  [16,17]
]
)

#Solution multiplication
print(A @ B)