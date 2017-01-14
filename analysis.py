#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import graphlab as gl
import sqlite3

# Loading train triplets
conn = sqlite3.connect("msd.sqlite3")
plays_df = gl.SFrame.from_sql(conn, "SELECT * FROM train")

# Total entries
total_entries = plays_df.num_rows()

# Percentage number of plays of songs
number_listens = []
for i in range(10):
	number_listens.append(float(plays_df[plays_df["plays"] == i+1].num_rows())/total_entries*100)

# Bar plot of the analysis
n = len(number_listens)
x = range(n)
width = 1/1.5
plt.bar(x, number_listens, width, color="blue")
plt.xlabel("Plays"); plt.ylabel("%")
plt.title("the percentage of times the songs were played")
plt.grid(b=True, which="major", color="k", linestyle="-")
plt.grid(b=True, which="minor", color="r", linestyle="-", alpha=0.2)
plt.minorticks_on()
plt.savefig("percentage_song_plays.png")
