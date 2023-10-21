import matplotlib.pyplot as plt
import pandas as pd

# Read your data
df = pd.read_csv('insurance.csv')

# Create the scatter plot
plt.scatter(df['age'], df['charges'])
plt.xlabel('Age')
plt.ylabel('Charges')
plt.title('Age vs Charges')

# Show the plot
plt.show()
