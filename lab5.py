import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

print("Shape of dataset:", df.shape)
print(df.info())

type_counts = df['type'].value_counts()
type_counts.plot(kind='bar', title='Movies vs TV Shows', color=['skyblue', 'salmon'])
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='barh', title='Top 10 Content-Producing Countries')
plt.xlabel('Number of Titles')
plt.gca().invert_yaxis()
plt.show()

year_trend = df['release_year'].value_counts().sort_index()
year_trend.plot(title='Number of Releases Over Time')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index[:10])
plt.title('Top 10 Ratings Distribution')
plt.show()

movie_df = df[df['type'] == 'Movie']
movie_df['duration_int'] = movie_df['duration'].str.extract('(\d+)').astype(float)
sns.histplot(movie_df['duration_int'], bins=20)
plt.title('Movie Duration Distribution')
plt.xlabel('Duration (minutes)')
plt.show()
