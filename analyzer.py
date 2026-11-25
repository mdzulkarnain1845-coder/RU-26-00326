import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_temperature_data(temps.csv):
    try:
        df = pd.read_csv(temps.csv)
    except FileNotFoundError:
        print("Error: temps.csv file not found.")
        return

    df.columns = df.columns.str.strip()
    

    df['Temp_C_clean'] = pd.to_numeric(df['Temp_C'], errors='coerce')
    invalid_mask = df['Temp_C_clean'].isna() & df['Temp_C'].notna()
    for idx, row in df[invalid_mask].iterrows():
        print(f"Invalid reading '{row['Temp_C']}' on {row['Date']}. Value ignored (NaN).")
    
    valid_data = df.dropna(subset=['Temp_C_clean'])
    temps = valid_data['Temp_C_clean'].values

    if len(temps) == 0:
        print("Error: No valid temperature readings found.")
        return

    while True:
        print("\n--- MENU ---")
        print("1. Statistics")
        print("2. Detect Outliers")
        print("3. Convert to Fahrenheit and plot")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            mean_val = np.mean(temps)
            median_val = np.median(temps)
            max_val = np.max(temps)
            min_val = np.min(temps)
            std_dev_val = np.std(temps)
            print(f"\nMean: {mean_val:.2f} | Median: {median_val:.2f} | Max: {max_val:.2f} | Min: {min_val:.2f} | Std Dev: {std_dev_val:.2f}")
            
            hot_days = valid_data[valid_data['Temp_C_clean'] > 35]
            if not hot_days.empty:
                dates_str = ", ".join(hot_days['Date'].astype(str))
                print(f"Hot days: {dates_str}")
            else:
                print("No days above 35 C")

        elif choice == '2':
            Q1 = np.percentile(temps, 25)
            Q3 = np.percentile(temps, 75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers =  valid_data[(valid_data['Temp_C_clean'] < lower_bound) |(valid_data['Temp_C_clean'] > upper_bound)]
            print("\n--- Outliers ---")
            if not outliers.empty:
                for _, row in outliers.iterrows():
                    print(f"Outlier on {row['Date']}: {row['Temp_C_clean']} C")
            else:
                print("No outliers detected.")

        elif choice == '3':
            valid_data = valid_data.copy()
            valid_data['Temp_F'] = (valid_data['Temp_C_clean'] * 9/5) + 32
            print("\nTemperatures in Fahrenheit:")
            print(" | ".join([f"{val:.2f} F" for val in valid_data['Temp_F']]))
            

            plt.figure(figsize=(8, 5))
            plt.plot(valid_data['Date'], valid_data['Temp_F'], marker='o', color='orange', linestyle='-', linewidth=2)
            plt.title('Temperature Data Analyzer (Fahrenheit)', fontsize=14)
            plt.xlabel('Date', fontsize=12)
            plt.ylabel('Temperature in F', fontsize=12)
            plt.grid(True)
            plt.show()


            plt.figure(figsize=(8, 5))
            plt.hist(valid_data['Temp_C_clean'], bins=5, color='skyblue', edgecolor='black')
            plt.title('Temperature Frequency (Histogram)', fontsize=14)
            plt.xlabel('Temperature in C', fontsize=12)
            plt.ylabel('Frequency', fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    process_temperature_data("temps.csv")










