#!/usr/bin/env python
import sqlite3
import graphlab as gl

# Load datasets
conn = sqlite3.connect("msd.sqlite3")
listens = gl.SFrame.from_sql(conn, "SELECT * FROM train where plays >=2")
songs_df = gl.SFrame.from_sql(conn, "SELECT * FROM song")

# Build model
model = gl.recommender.ranking_factorization_recommender.create(listens, user_id="userID", item_id="songID", target="plays")

# Recommend songs to users
recommendations = model.recommend(users=["fd50c4007b68a3737fe052d5a4f78ce8aa117f3d"])
song_recommendations = recommendations.join(songs_df, on="songID", how="inner").sort("rank")

# Show the results
print song_recommendations
