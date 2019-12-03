import matplotlib.pyplot as plt

hours = [4, 8,]
activities = ['Women Medals', 'Men Medals']
colors = ['green', 'silver',]
plt.pie(hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')

plt.title("Total Medals")
plt.show()