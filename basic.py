#!/usr/bin/env python
import graphlab as gl
import graphlab.aggregate as agg
import sqlite3

# Loading the DB
conn = sqlite3.connect("msd.sqlite3")

plays_df = gl.SFrame.from_sql(conn, "SELECT * FROM train")
songs_df = gl.SFrame.from_sql(conn, "SELECT * FROM song")

# Get the most listened songs
songs_total_listens = plays_df.groupby(key_columns='songID', operations={"plays": agg.SUM("plays")})

# Join songs with data
songs_total_listens = songs_total_listens.join(songs_df, on="songID", how="inner").sort("plays", ascending=False)
print "# Top Songs with most total lisens:"
print songs_total_listens.print_rows()
