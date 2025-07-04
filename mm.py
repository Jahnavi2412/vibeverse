import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Step 1: Load MovieLens dataset
movies_df = pd.read_csv('movieorig.csv')  # Movie data (movieId, title, genre)
ratings_df = pd.read_csv('.csv')  # Ratings data (userId, movieId, rating)

# Step 2: Create a user-item matrix (pivot table)
user_movie_matrix = ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Step 3: Calculate the similarity matrix using cosine similarity
cosine_sim = cosine_similarity(user_movie_matrix.T)  # Transpose the matrix to calculate movie-to-movie similarity

# Step 4: Create a KNN model for item-based recommendation
knn = NearestNeighbors(n_neighbors=10, metric='cosine')
knn.fit(cosine_sim)

# Step 5: Function to recommend movies for a given movie
def recommend_movies(movie_id, knn_model, cosine_sim, top_n=10):
    # Find the index of the movie in the user-movie matrix
    movie_index = user_movie_matrix.columns.get_loc(movie_id)
    
    # Get nearest neighbors (similar movies) for the given movie
    distances, indices = knn_model.kneighbors([cosine_sim[movie_index]], n_neighbors=top_n + 1)
    
    # Get the movie IDs of the nearest neighbors
    recommended_movie_ids = [user_movie_matrix.columns[i] for i in indices.flatten()[1:]]  # Exclude the movie itself
    
    # Get movie titles for the recommended movie IDs
    recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movie_ids)]
    
    return recommended_movies[['movieId', 'title']]

# Step 6: Example usage - Get recommendations for a specific movie (movieId = 1)
movie_id_to_recommend = 1  # Example movie ID, you can choose any movie from the dataset
recommended_movies = recommend_movies(movie_id_to_recommend, knn, cosine_sim)

# Step 7: Print the recommended movies
print("Recommended movies for movie ID", movie_id_to_recommend)
print(recommended_movies)
