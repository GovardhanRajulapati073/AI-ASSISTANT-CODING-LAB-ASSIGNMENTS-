import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'salary': [45000, 55000, 60000, 48000, 70000],
    'department': ['HR', 'IT', 'IT', 'Finance', 'IT']
}
df = pd.DataFrame(data)

# Equivalent Pandas query
result = df[df['salary'] > 50000][['name', 'salary']]

print("Original DataFrame:")
print(df)
print("\nFiltered Result (salary > 50000):")
print(result)