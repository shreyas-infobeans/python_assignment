import pandas as pd

df = pd.read_csv('sample_data.csv')
print(df)
print(df.head(5))
print(df.dtypes)
print(df.describe())
rows, cols = df.shape
print(rows,cols)
df.columns = ['Index','Height', 'Weight']
df['Height_in_meters'] = df['Height'] * 0.0254
filtered_df = df[df['Weight'] > 150]
print(filtered_df)












