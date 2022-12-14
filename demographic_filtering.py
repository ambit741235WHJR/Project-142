# Importing pandas and plotly.express
import pandas as pd
import plotly.express as px

# Reading articles_en.csv using pandas
df = pd.read_csv('articles_en.csv')

# Sorting the rows based on total_events column and creating an output with top 20 rows
df.sort_values(by='total_events', ascending=False)
output = df[['title', 'url', 'total_events']].head(20).values.tolist()