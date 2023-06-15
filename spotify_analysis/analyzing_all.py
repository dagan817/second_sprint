import pandas as pd
import matplotlib.pyplot as plt

# Load the data using Pandas
data = pd.read_csv('spotify_top_50.csv')

# Perform data cleaning

# Handling missing values
data.dropna(inplace=True)

# Removing duplicate samples
data.drop_duplicates(inplace=True)

# Removing duplicate features
data = data.loc[:, ~data.columns.duplicated()]

# Treating outliers
# Assuming outliers are present in numeric columns 'Danceability', 'Loudness (dB)', and 'Duration (ms)'
# We can treat outliers using various methods like Winsorization, z-score, or manual capping.
# For simplicity, I am using manual capping for this example.

# Capping outliers for 'Danceability'
danceability_upper_limit = data['Danceability'].quantile(0.95)
data.loc[data['Danceability'] > danceability_upper_limit, 'Danceability'] = danceability_upper_limit

# Capping outliers for 'Loudness (dB)'
loudness_lower_limit = data['Loudness (dB)'].quantile(0.05)
loudness_upper_limit = data['Loudness (dB)'].quantile(0.95)
data.loc[data['Loudness (dB)'] < loudness_lower_limit, 'Loudness (dB)'] = loudness_lower_limit
data.loc[data['Loudness (dB)'] > loudness_upper_limit, 'Loudness (dB)'] = loudness_upper_limit

# Capping outliers for 'Duration (ms)'
duration_upper_limit = data['Duration (ms)'].quantile(0.95)
data.loc[data['Duration (ms)'] > duration_upper_limit, 'Duration (ms)'] = duration_upper_limit

# Exploratory Data Analysis

# How many observations are there in this dataset?
num_observations = data.shape[0]
print("Number of observations:", num_observations)

# How many features this dataset has?
num_features = data.shape[1]
print("Number of features:", num_features)

# Which of the features are categorical?
categorical_features = data.select_dtypes(include='object').columns.tolist()
print("Categorical features:", categorical_features)

# Which of the features are numeric?
numeric_features = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("Numeric features:", numeric_features)

# Are there any artists that have more than 1 popular track? If yes, which and how many?
popular_tracks_by_artist = data['Artist'].value_counts()
artists_with_multiple_popular_tracks = popular_tracks_by_artist[popular_tracks_by_artist > 1]
print("Artists with more than 1 popular track:")
print(artists_with_multiple_popular_tracks)

# Who was the most popular artist?
most_popular_artist = popular_tracks_by_artist.idxmax()
print("Most popular artist:", most_popular_artist)

# How many artists in total have their songs in the top 50?
total_artists = len(popular_tracks_by_artist)
print("Total number of artists:", total_artists)

# Are there any albums that have more than 1 popular track? If yes, which and how many?
popular_tracks_by_album = data['Album'].value_counts()
albums_with_multiple_popular_tracks = popular_tracks_by_album[popular_tracks_by_album > 1]
print("Albums with more than 1 popular track:")
print(albums_with_multiple_popular_tracks)

# How many albums in total have their songs in the top 50?
total_albums = len(popular_tracks_by_album)
print("Total number of albums:", total_albums)

# Which tracks have a danceability score above 0.7?
high_danceability_tracks = data[data['Danceability'] > 0.7]['Track Name']
print("Tracks with danceability score above 0.7:")
print(high_danceability_tracks)

# Which tracks have a danceability score below 0.4?
low_danceability_tracks = data[data['Danceability'] < 0.4]['Track Name']
print("Tracks with danceability score below 0.4:")
print(low_danceability_tracks)

# Which tracks have their loudness above -5?
loud_tracks = data[data['Loudness (dB)'] > -5]['Track Name']
print("Tracks with loudness above -5:")
print(loud_tracks)

# Which tracks have their loudness below -8?
quiet_tracks = data[data['Loudness (dB)'] < -8]['Track Name']
print("Tracks with loudness below -8:")
print(quiet_tracks)

# Which track is the longest?
longest_track = data[data['Duration (ms)'] == data['Duration (ms)'].max()]['Track Name']
print("Longest track:")
print(longest_track)

# Which track is the shortest?
shortest_track = data[data['Duration (ms)'] == data['Duration (ms)'].min()]['Track Name']
print("Shortest track:")
print(shortest_track)

# Which genre is the most popular?
most_popular_genre = data['Genre'].value_counts().idxmax()
print("Most popular genre:", most_popular_genre)

# Which genres have just one song on the top 50?
genres_with_one_song = data['Genre'].value_counts()[data['Genre'].value_counts() == 1].index.tolist()
print("Genres with just one song on the top 50:")
print(genres_with_one_song)

# How many genres in total are represented in the top 50?
total_genres = len(data['Genre'].unique())
print("Total number of genres:", total_genres)

# Which features are strongly positively correlated?
corr_threshold = 0.7
positive_corr = data.corr().unstack().sort_values(ascending=False)
strong_positive_corr = positive_corr[(positive_corr > corr_threshold) & (positive_corr < 1.0)]
print("Strongly positively correlated features:")
print(strong_positive_corr)

# Which features are strongly negatively correlated?
negative_corr = data.corr().unstack().sort_values()
strong_negative_corr = negative_corr[(negative_corr < -corr_threshold) & (negative_corr > -1.0)]
print("Strongly negatively correlated features:")
print(strong_negative_corr)

# Which features are not correlated?
uncorrelated_features = data.corr().unstack().sort_values().drop_duplicates()
print("Uncorrelated features:")
print(uncorrelated_features)

# Danceability score comparison between genres
genres = ['Pop', 'Hip-Hop/Rap', 'Dance/Electronic', 'Alternative/Indie']
danceability_scores = data[data['Genre'].

# Danceability score comparison between genres
genres = ['Pop', 'Hip-Hop/Rap', 'Dance/Electronic', 'Alternative/Indie']
danceability_scores = data[data['Genre'].isin(genres)]['Danceability']

# Plotting the danceability scores
plt.figure(figsize=(8, 6))
plt.boxplot(danceability_scores, labels=genres)
plt.title('Danceability Score Comparison between Genres')
plt.ylabel('Danceability Score')
plt.xlabel('Genre')
plt.show()

# Loudness score comparison between genres
loudness_scores = data[data['Genre'].isin(genres)]['Loudness (dB)']

# Plotting the loudness scores
plt.figure(figsize=(8, 6))
plt.boxplot(loudness_scores, labels=genres)
plt.title('Loudness Score Comparison between Genres')
plt.ylabel('Loudness (dB)')
plt.xlabel('Genre')
plt.show()

# Acousticness score comparison between genres
acousticness_scores = data[data['Genre'].isin(genres)]['Acousticness']

# Plotting the acousticness scores
plt.figure(figsize=(8, 6))
plt.boxplot(acousticness_scores, labels=genres)
plt.title('Acousticness Score Comparison between Genres')
plt.ylabel('Acousticness Score')
plt.xlabel('Genre')
plt.show()

# Explanations and analysis improvement suggestions
print("Explanations:")
print("Danceability Score Comparison:")
print("The boxplots show the distribution of danceability scores for each genre, allowing visual comparison of the median, quartiles, and potential outliers.")

print("\nLoudness Score Comparison:")
print("The boxplots display the distribution of loudness scores for each genre, facilitating a visual comparison of the median, quartiles, and potential outliers.")

print("\nAcousticness Score Comparison:")
print("The boxplots illustrate the distribution of acousticness scores for each genre, enabling a visual comparison of the median, quartiles, and potential outliers.")

print("\nAnalysis Improvement Suggestions:")
print("1. Perform statistical tests such as ANOVA or Kruskal-Wallis to determine if there are significant differences in scores between the genres.")
print("2. Include histograms or density plots to provide a more detailed understanding of the score distributions within each genre.")
print("3. Analyze other features such as energy, tempo, or valence to gain insights into their variations across different genres.")
print("4. Expand the analysis to include more genres and explore their comparisons in terms of various features.")
print("5. Investigate how different features correlate with each other across genres, for example, the relationship between danceability and energy within each genre.")
