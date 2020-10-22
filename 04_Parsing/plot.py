import sys
import matplotlib.pyplot as plt

labels = {0:'Tamil', 1:'Hindi', 2:'Telugu',3:'Moksha',4:'Afrikaans',5:'Sanskrit',6:'Polish',7:'Spanish',8:'Urdu',9:'Japanese'}
x = [1.00, 0.75, 0.98, 0.09, 0.25, 0.85, 0.25, 0.27, 0.95, 1.00]  # proportion of OV
y = [0.00, 0.25, 0.02, 0.91, 0.75, 0.17, 0.75, 0.73, 0.05, 0.00]  # proportion of VO
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
