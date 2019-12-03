import matplotlib.pyplot as plt

years = [1924, 1928, 1932, 1936, 1948, 1956, 1960, 1964, 1968, 1972, 1976, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

pop_men = [ 0, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9]

plt.plot(years, pops, color=(225/225, 100/225, 100/225), linewidth=6.0)

plt.ylabel("World Population by Billions")
plt.xlabel("Population Growth by Year")
plt.title("Global Popluation Growth 1990-2015", pad=20)

# show the chart
plt.show()