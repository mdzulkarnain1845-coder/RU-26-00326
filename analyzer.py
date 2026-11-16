import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("temps.csv")
df.columns = df.columns.str.strip()
temperatures = df['Temp_C'].values

mean_val = np.mean(temperatures)
median_val = np.median(temperatures)
max_val = np.max(temperatures)
min_val = np.min(temperatures)
std_dev_val = np.std(temperatures)

hot_days_df = df[df['Temp_C'] > 35]

print("\n---PROJECT RESULT---")
print(f"Mean: {mean_val:.2f} | Median: {median_val:.2f} | Max: {max_val:.2f} | Min: {min_val:.2f} | Std Dev: {std_dev_val:.2f}")

print("\n---HOT DAYS (>35℃)---")
if not hot_days_df.empty:
    for index, row in hot_days_df.iterrows():
        print(f"Hot day: {row['Date']}")
else:
    print("No days above 35℃.")

plt.figure(figsize=(8 , 5))
plt.plot(df['Date'], df['Temp_C'], marker='o', color='red', linestyle='-', linewidth=2)

plt.title('Temperature Data Analyzer', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature in ℃', fontsize=12)
plt.grid(True)

plt.figure(figsize=(8 , 5))
plt.hist(df['Temp_C'].dropna(), bins=5, color='skyblue', edgecolor='black')

plt.title('Temperature Frequency (Histogram)', fontsize=14)
plt.xlabel('Temperature in ℃', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()












