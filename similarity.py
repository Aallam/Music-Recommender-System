#!/usr/bin/env python
import graphlab as gl
import sqlite3

# Load dataset
conn = sqlite3.connect("msd.sqlite3")
listens = gl.SFrame.from_sql(conn, "SELECT * FROM train")

# Create Training set and test set
train_data, test_data = gl.recommender.util.random_split_by_user(listens, "userID", "songID")

# Train the model
model = gl.item_similarity_recommender.create(train_data, "userID", "songID")

# Evaluate the model
rmse_data = model.evaluate_rmse(test_data, target="plays")

# Print the results
print rmse_data
