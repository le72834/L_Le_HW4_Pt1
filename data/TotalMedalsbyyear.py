import matplotlib.pyplot as plt

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

pops = [ 9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 68, 91, 90]

plt.plot(years, pops, color=(225/225, 100/225, 100/225), linewidth=6.0)

plt.ylabel("Total of Medals")
plt.xlabel("Years of Winter Olympic")
plt.title("Proportion of Medals 1924-2014", pad=20)

# show the chart
plt.show()