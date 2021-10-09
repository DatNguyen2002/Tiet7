import numpy as np

coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8])
np.random.binomial(20, 0.5) # Số mặt ngửa nhận được khi tung đồng xu 10 lần
