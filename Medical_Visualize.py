import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\Medicaldataset.csv')
print(df)

df.info()
print(df.info())

df.isnull().sum()
print(df.isnull().sum())

df.describe()
print(df.describe())

df.duplicated().sum()
print(df.duplicated().sum())

# regular data
regular_data = np.array([10, 20, 30, 40, 50])
print(f'Mean of regular data: {regular_data.mean()}') # Output: 30

#Data with an outlier
outlier_data = np.array([10, 20, 30, 40, 500]) # 500 is an outlier
print(f'Mean of data with an outlier: {outlier_data.mean()}') # Output: 120

# Data Visualization
# Generate random data for the histogram
data = np.random.randn(1000)

# Creating a customized histogram with a density plot
sns.histplot(data, bins=30, kde=True, color='navy', edgecolor='pink')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')

# Display the plot
plt.show()