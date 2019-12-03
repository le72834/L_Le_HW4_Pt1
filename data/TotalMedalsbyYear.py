import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


objects = ('1924', '1928', '1932', '1936', '1948', '1952', '1956', '1960', '1964', '1968', '1972', '1976', '1980', '1984', '1988', '1992', '1994', '1998', '2002', '2006', '2010', '2014')
y_pos = np.arange(len(objects))
performance = [9,12,20,13,18,17,18,18,19,5,18,1,2,4,2,30,30,16,38,21,47,46]


plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.ylabel('Year of Winter Olympics')
plt.title('Proportion of Medals win by Men')


plt.show()