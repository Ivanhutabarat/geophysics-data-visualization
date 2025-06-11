import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/gravity_data.csv')
plt.plot(data['Location'], data['Gravity'], marker='o')
plt.xlabel('Location')
plt.ylabel('Gravity (m/s²)')
plt.title('Gravity Data Visualization')
plt.show()
