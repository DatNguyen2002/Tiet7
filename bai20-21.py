import numpy as np

np.random.randint(0, 2) # Ngẫu nhiên số nguyên trong khoảng [0, 2)
coins = np.random.randint(2, size=1000)
print(coins.shape)