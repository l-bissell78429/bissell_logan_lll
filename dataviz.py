import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
installs = []
ratings = []

# open the csv file and parse it
with open("data/googeplaystore.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("pushing text row to categories array")
            categories.append(row)
            line_count += 1
        else:
            ratingsData = row[2]
            ratingsData = ratingsData.replace("NaN", "0")
            ratings.append(float(ratingsData))

            installData = row[5]
            installData = installData.replace(",", "")
            installData = installData.replace("Free", "8")
            installs.append(int(np.char.strip(installData, "+")))
            line_count += 1

print("processed". line_count, "rows of data")
print("first line". ratings[0])
print("last time", ratings[-1])

np_ratings = np.array(ratings)

popular_apps = np_ratings > 4
pop_pct = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(pop_pct)


popular_apps = np_ratings > 2
pop_pct = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)

labels = "Sucks, Meh, Love it!"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ["yellowgreen", "lightcoral", "lightskyblue"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("do we love our apps?")
plt.xlabel("user ratings - google play store app installs")
plt.show()
