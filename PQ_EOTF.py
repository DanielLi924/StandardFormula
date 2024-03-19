import numpy as np
import matplotlib.pyplot as plt

m1 = 0.1593017578125
m2 = 78.84375
c2 = 18.8515625
c3 = 18.6875
c1 = c3 - c2 + 1

def EOTF_PQ(E1):
    Y = (np.maximum((E1)**(1/m2) - c1 , 0)/(c2 - c3*E1**(1/m2)))**(1/m1)
    Fd = 10000 * Y
    return Fd

E1_values = np.linspace(0,1,10000)

y_values = EOTF_PQ(E1_values)

key_points = [203, 1000, 10000]

fig = plt.figure(figsize=(16,9),dpi=300)

# Create a plot for the sine wave
plt.plot(E1_values, y_values, label='PQ_EOTF')

# Add labels and title
plt.xlabel('non-linear colour value')
plt.ylabel('the luminance of a displayed linear component')
plt.title('Plot of PQ_EOTF')

# Add a legend
plt.legend()

plt.xlim(0,1)
plt.ylim(0,10000)



for points in key_points:
    plt.hlines(points,0,10000, linestyle='--', colors = 'red', alpha=0.5)

plt.scatter([0] * len(key_points), key_points, marker='o', color='red', label='Key Points')

save_path = 'D:/Hobby/Film/Stuff'

fig.savefig(save_path, dpi=300)

# Show the plot
plt.show()