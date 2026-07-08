import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate 10,000 rows of random data
num_rows = 10000

# Generate random CustomerID (1000 to 11000)
customer_ids = np.random.randint(1000, 11001, num_rows)

# Generate random Names
first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Jessica', 'James', 'Jennifer',
               'William', 'Lisa', 'Richard', 'Mary', 'Joseph', 'Patricia', 'Thomas', 'Barbara', 'Charles', 'Susan']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
              'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']

names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_rows)]

# Generate random Ages (18 to 80)
ages = np.random.randint(18, 81, num_rows)

# Generate random Cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
          'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Seattle', 'Denver', 'Boston', 'Miami', 'Atlanta',
          'Portland', 'Las Vegas', 'Detroit', 'Minneapolis', 'Cleveland', 'New Orleans', 'Sacramento', 'Kansas City']

city_list = [random.choice(cities) for _ in range(num_rows)]

# Generate random PurchaseAmount (10 to 5000)
purchase_amounts = np.random.uniform(10, 5000, num_rows)
purchase_amounts = np.round(purchase_amounts, 2)

# Generate random PurchaseDate (last 2 years)
start_date = datetime.now() - timedelta(days=730)
purchase_dates = [start_date + timedelta(days=random.randint(0, 730)) for _ in range(num_rows)]

# Create DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Name': names,
    'Age': ages,
    'City': city_list,
    'PurchaseAmount': purchase_amounts,
    'PurchaseDate': purchase_dates
})

# Save to Excel
output_file = 'SalesData.xlsx'
df.to_excel(output_file, index=False, sheet_name='SalesData')

print(f"✅ Excel file '{output_file}' created successfully!")
print(f"📊 Total rows: {len(df)}")
print(f"\nFirst few rows:")
print(df.head(10))
