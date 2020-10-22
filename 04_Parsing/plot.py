import sys
import matplotlib.pyplot as plt

labels = {0:'eng', 1:'rus', 2:'gle',3:'tur',4:'spa'}
x = [0.1, 0.5, 0.3, 0.7, 0.4]  # proportion of OV
y = [0.9, 0.5, 0.7, 0.3, 0.6]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.savefig(sys.argv[1])
plt.show()
