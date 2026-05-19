import numpy as np
import matplotlib.pyplot as plt

heart_rate = [72, 75, 78, 80, 120, 110, 85, 78, 76, 74]

print("Average heart rate:", np.mean(heart_rate))
print("Max heart rate:", np.max(heart_rate))
print("Min heart rate:", np.min(heart_rate))

plt.plot(heart_rate)
plt.title("Heart Rate Over Time")
plt.xlabel("Time")
plt.ylabel("BPM")
plt.show()