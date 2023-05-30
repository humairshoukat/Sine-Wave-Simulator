import numpy as np
import matplotlib.pyplot as plt

A = int(input("Enter Amplitude of the Sinewave:"))
f = int(input("Enter Frequency of the Sinewave:"))
ph = int(input("Enter phase angle of the sinewave:"))
#ts = int(input("Enter Starting time for the Sinewave:"))
t = int(input("Enter time interval for the Sinewave:"))
sr = 100 # sampling rate
time = np.arange(0, t, 1/ sr) # 0.01 sec
y = A* np.sin(2 * np.pi * f * time + ph)
plt.figure(figsize=(10,4)) 
plt.plot(time, y) 
plt.title("Sine wave") 
plt.xlabel("Time(s)") 
plt.ylabel("Amplitude")
plt.show()