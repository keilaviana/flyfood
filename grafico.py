import numpy as np
import matplotlib.pyplot as plt

data = np.array([[4,0.0012145],[6,0.0072722],[8,0.1710264],[10,35.1644134],[11,1772.0471663]])
plt.plot(data[:, 0], data[:, 1])
plt.show()