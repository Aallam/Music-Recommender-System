#!/usr/bin/env python
import sqlite3
import graphlab as gl

# Load datasets
conn = sqlite3.connect("msd.sqlite3")
listens = gl.SFrame.from_sql(conn, "SELECT * FROM train")

# Build model
training_data, validation_data = gl.recommender.util.random_split_by_user(listens, "userID", "songID")

# Train the model
model = gl.recommender.ranking_factorization_recommender.create(training_data, user_id="userID", item_id="songID", target="plays")

# Recommend songs to users
rmse_data = model.evaluate_rmse(validation_data, target="plays")

# Print the results
print rmse_data
