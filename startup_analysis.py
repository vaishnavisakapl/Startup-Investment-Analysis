import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('startup_investment_data.csv')

# Display basic information
print("Dataset Info:")
print(df.info())
print("\nDataset Head:")
print(df.head())

# Handling missing data (if any)
df.fillna(method='ffill', inplace=True)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Analysis: Total funding by domain
funding_by_domain = df.groupby('Domain')['Funding Amount (USD)'].sum().reset_index()
print("\nTotal Funding by Domain:")
print(funding_by_domain)

# Analysis: Number of startups by funding stage
stage_counts = df['Funding Stage'].value_counts()
print("\nStartups by Funding Stage:")
print(stage_counts)

# Visualization: Funding by domain
plt.figure(figsize=(10,6))
plt.bar(funding_by_domain['Domain'], funding_by_domain['Funding Amount (USD)'])
plt.title('Total Funding by Domain')
plt.xlabel('Domain')
plt.ylabel('Funding Amount (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Number of startups by funding stage
plt.figure(figsize=(8,5))
stage_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Startups by Funding Stage')
plt.ylabel('')
plt.tight_layout()
plt.show()
