import pandas as pd

# Load the data using Pandas
data = pd.read_csv('spotifytoptracks.csv')

# Perform data cleaning

# Handling missing values
data.dropna(inplace=True)

# Removing duplicate samples and features
data.drop_duplicates(inplace=True)

# Treating the outliers (if necessary)

# Exploratory Data Analysis

# How many observations are there in this dataset?
num_observations = len(data)
print("Number of observations:", num_observations)

# How many features this dataset has?
num_features = len(data.columns)
print("Number of features:", num_features)

# Identify categorical and numeric features
categorical_features = ['artist', 'album', 'track_name', 'track_id', 'genre']
numeric_features = ['energy', 'danceability', 'key', 'loudness', 'acousticness', 'speechiness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

# Are there any artists that have more than 1 popular track? If yes, which and how many?
popular_artists = data['artist'].value_counts()
popular_artists = popular_artists[popular_artists > 1]
num_popular_artists = len(popular_artists)
print("Number of artists with more than 1 popular track:", num_popular_artists)
print("Popular artists with their track count:")
print(popular_artists)

# Who was the most popular artist?
most_popular_artist = popular_artists.idxmax()
print("Most popular artist:", most_popular_artist)

# How many artists in total have their songs in the top 50?
num_artists_in_top_50 = len(data['artist'].unique())
print("Number of artists in total in the top 50:", num_artists_in_top_50)

# Are there any albums that have more than 1 popular track? If yes, which and how many?
popular_albums = data['album'].value_counts()
popular_albums = popular_albums[popular_albums > 1]
num_popular_albums = len(popular_albums)
print("Number of albums with more than 1 popular track:", num_popular_albums)
print("Popular albums with their track count:")
print(popular_albums)

# How many albums in total have their songs in the top 50?
num_albums_in_top_50 = len(data['album'].unique())
print("Number of albums in total in the top 50:", num_albums_in_top_50)

# Which tracks have a danceability score above 0.7?
tracks_above_07_danceability = data[data['danceability'] > 0.7]['track_name']
print("Tracks with danceability score above 0.7:")
print(tracks_above_07_danceability)

# Which tracks have a danceability score below 0.4?
tracks_below_04_danceability = data[data['danceability'] < 0.4]['track_name']
print("Tracks with danceability score below 0.4:")
print(tracks_below_04_danceability)

# Which tracks have their loudness above -5?
tracks_above_neg5_loudness = data[data['loudness'] > -5]['track_name']
print("Tracks with loudness above -5:")
print(tracks_above_neg5_loudness)

# Which tracks have their loudness below -8?
tracks_below_neg8_loudness = data[data['loudness'] < -8]['track_name']
print("Tracks with loudness below -8:")
print(tracks_below_neg8_loudness)

# Which track is the longest?
longest_track = data[data['duration_ms'] == data['duration_ms'].max()]['track_name'].iloc[0]
print("Longest track:", longest_track)

# Which track is the shortest?
shortest_track = data[data['duration_ms'] == data['duration_ms'].min()]['track_name'].iloc[0]
print("Shortest track:", shortest_track)

# Which genre is the most popular?
most_popular_genre = data['genre'].value_counts().idxmax()
print("Most popular genre:", most_popular_genre)

# Which genres have just one song on the top 50?
genres_with_single_song = data['genre'].value_counts()[data['genre'].value_counts() == 1]
print("Genres with just one song on the top 50:")
print(genres_with_single_song)

# How many genres in total are represented in the top 50?
num_genres_in_top_50 = len(data['genre'].unique())
print("Number of genres in total in the top 50:", num_genres_in_top_50)

# Calculate correlation matrix
correlation_matrix = data[numeric_features].corr()

# Identify strongly positively correlated features
strong_pos_corr_features = correlation_matrix[correlation_matrix > 0.7].stack().dropna().index
print("Features strongly positively correlated:")
print(strong_pos_corr_features)

# Identify strongly negatively correlated features
strong_neg_corr_features = correlation_matrix[correlation_matrix < -0.7].stack().dropna().index
print("Features strongly negatively correlated:")
print(strong_neg_corr_features)

# Identify features that are not correlated
uncorrelated_features = correlation_matrix[(correlation_matrix >= -0.2) & (correlation_matrix <= 0.2)].stack().dropna().index
print("Features that are not correlated:")
print(uncorrelated_features)

# Compare danceability score between genres
danceability_by_genre = data[data['genre'].isin(['Pop', 'Hip-Hop/Rap', 'Dance/Electronic', 'Alternative/Indie'])].groupby('genre')['danceability'].mean()
print("Average danceability score by genre:")
print(danceability_by_genre)

# Compare loudness score between genres
loudness_by_genre = data[data['genre'].isin(['Pop', 'Hip-Hop/Rap', 'Dance/Electronic', 'Alternative/Indie'])].groupby('genre')['loudness'].mean()
print("Average loudness score by genre:")
print(loudness_by_genre)

# Compare acousticness score between genres
acousticness_by_genre = data[data['genre'].isin(['Pop', 'Hip-Hop/Rap', 'Dance/Electronic', 'Alternative/Indie'])].groupby('genre')['acousticness'].mean()
print("Average acousticness score by genre:")
print(acousticness_by_genre)

# Provide suggestions for improving the analysis

# You can further explore the relationships between different features using visualizations such as scatter plots, box plots, or histograms.
# Consider analyzing the distribution of each feature to identify any outliers or anomalies.
# You can perform hypothesis testing or statistical analysis to identify significant differences between genres or other categorical variables.
# Consider incorporating other external datasets or features that may provide additional insights or context to the analysis.
# It is important to ensure the data quality and accuracy by verifying the sources and conducting data validation or cross-checks.
# Document your analysis steps, assumptions, and any limitations to facilitate reproducibility and transparency.