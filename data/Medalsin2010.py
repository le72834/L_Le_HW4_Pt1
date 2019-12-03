import matplotlib.pyplot as plt

labels = ['Women', 'Men']
sizes = [44, 47]
colors = ['lightskyblue', 'lightcoral']
plt.pie(sizes, colors=colors, startangle=90, labels=labels, autopct='%1.1f%%')
plt.title("Medals in 2010")
plt.show()