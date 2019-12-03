import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


objects = ('1948', '1956', '1960', '1964', '1968', '1972', '1976', '1988', '1992', '1994', '1998', '2002', '2006', '2010', '2014')
y_pos = np.arange(len(objects))
performance = [2,2,2,2,2,1,2,4,7,10,33,37,47,44,44]


plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.ylabel('Proportion of Medals win by Women')
plt.title('Year of Winter Olympics')

plt.show()