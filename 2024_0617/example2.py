import matplotlib.pyplot as plt
import numpy as np

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{absolute:d}pcs - {pct:.1f}%"

values = [5, 6]
labels = ['Rend','Return']
colors = ['green','red']
figure = plt.figure(figsize=(5,5),dpi=72)
axes = figure.add_subplot()
axes.pie(values,colors=colors,
         labels=labels,
         labeldistance=0.4,
         shadow=True,
         autopct=lambda pct: func(pct, values),
         textprops=dict(color="white"))
#axes.set_title('title')

plt.show()