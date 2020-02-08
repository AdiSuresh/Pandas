import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")
df.describe()
spendings = np.array(df["spendings"])
sales = np.array(df["sales"])
plt.scatter(spendings, sales)
plt.xlabel("Spendings")
plt.ylabel("Sales")
plt.show()
